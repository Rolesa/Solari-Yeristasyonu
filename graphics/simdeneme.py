from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
from pymavlink import mavutil
import time
import math
import dronekit_sitl

# SITL'yi başlatma
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

print(f"Connecting to vehicle on: {connection_string}")
vehicle = connect(connection_string, wait_ready=True)

print("Vehicle connected")


def arm_and_drive(vehicle):
    print("Arming motors")
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Motors armed!")


def get_location_metres(original_location, dNorth, dEast):
    earth_radius = 6378137.0  # Dünya yarıçapı (metre)
    dLat = dNorth / earth_radius
    dLon = dEast / (earth_radius * math.cos(math.pi * original_location.lat / 180))

    newlat = original_location.lat + (dLat * 180 / math.pi)
    newlon = original_location.lon + (dLon * 180 / math.pi)
    return LocationGlobalRelative(newlat, newlon, original_location.alt)


def get_distance_metres(aLocation1, aLocation2):
    dlat = aLocation2.lat - aLocation1.lat
    dlon = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlon*dlon)) * 1.113195e5


def move_and_record(vehicle, north, east, waypoints):
    current_location = vehicle.location.global_relative_frame
    new_location = get_location_metres(current_location, north, east)
    vehicle.simple_goto(new_location)

    while vehicle.mode.name == "GUIDED":
        remaining_distance = get_distance_metres(vehicle.location.global_relative_frame, new_location)
        print(f"Distance to target: {remaining_distance}")
        if remaining_distance < 1:
            print("Reached target")
            break
        time.sleep(1)

    waypoints.append((new_location.lat, new_location.lon, new_location.alt))


def upload_mission(vehicle, waypoints):
    cmds = vehicle.commands
    cmds.clear()

    for waypoint in waypoints:
        lat, lon, alt = waypoint
        cmds.add(Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                         mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,
                         lat, lon, alt))

    cmds.upload()

# Waypoint listesi
waypoints = []

# Aracı arm edip harekete başlatma
arm_and_drive(vehicle)

# 10 metre ileri git ve waypoint kaydet
move_and_record(vehicle, 10, 0, waypoints)

# 10 metre sola git ve waypoint kaydet
move_and_record(vehicle, 0, -10, waypoints)

# Görevi araca yükle
upload_mission(vehicle, waypoints)

# Aracı "AUTO" moduna geçirerek waypoint'leri takip etmesini sağlama
print("Switching to AUTO mode")
vehicle.mode = VehicleMode("AUTO")

# Görev tamamlanana kadar bekleme
while vehicle.mode.name == "AUTO":
    print(f"Current waypoint: {vehicle.commands.next}")
    time.sleep(1)

print("Mission completed")

# Aracı durdurup disarm etme
print("Stopping")
vehicle.mode = VehicleMode("HOLD")

while vehicle.armed:
    print("Waiting for disarm...")
    time.sleep(1)

print("Disarmed")

# Bağlantıyı kapatma
vehicle.close()
print("Vehicle disconnected")

# SITL'yi durdurma
sitl.stop()
print("SITL stopped")
