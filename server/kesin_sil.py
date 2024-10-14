from pymavlink import mavutil
import time


def get_gps_loc(master, prev_lat=None, prev_lon=None):
    while True:
        msg = None

        while True:
            temp = master.recv_match(type='GLOBAL_POSITION_INT', blocking=False)
            if temp is None:
                break
            msg = temp

        if msg is None:
            msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)

        if msg:
            latitude = msg.lat
            longitude = msg.lon

            if latitude == prev_lat and longitude == prev_lon:
                continue
            else:
                return latitude, longitude


def check_arm_status(master):
    msg = master.recv_match(type='HEARTBEAT', blocking=True)
    armed = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
    if armed:
        print("Vehicle is armed")
        return True
    else:
        print("Vehicle is disarmed")
        return False


def force_arm_vehicle(master):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1,
        21196,
        0, 0, 0, 0, 0
    )
    print("Vehicle is force-armed")


def set_throttle(master, channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,
        master.target_component,
        *rc_channel_values)


def disarm_vehicle(master):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        0,  # Disarm
        0,
        0, 0, 0, 0, 0
    )



def cmd_set_home(master, home_location, altitude):
    latitude, longitude = home_location
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_HOME,
        1,
        0, 0, 0, 0,
        latitude, longitude, altitude
    )
    print(f"Home location set edildi: Lat={latitude}, Lon={longitude}, Alt={altitude}")


def auto_mode_start(master, mode_name):
    mode_id = master.mode_mapping()[mode_name]
    base_mode = mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0,
        base_mode,
        mode_id,
        0, 0, 0, 0, 0
    )


def cmd_get_home(connection):
    connection.mav.command_long_send(
        connection.target_system, connection.target_component,
        mavutil.mavlink.MAV_CMD_GET_HOME_POSITION,
        0, 0, 0, 0, 0, 0, 0, 0
    )
    msg = connection.recv_match(type=['COMMAND_ACK'], blocking=True, timeout=5)
    if msg.result != mavutil.mavlink.MAV_RESULT_ACCEPTED:
        print("Home location sorgusu başarısız.")
        return
    msg = connection.recv_match(type=['HOME_POSITION'], blocking=True)
    print(f"Home position: Lat={msg.latitude}, Lon={msg.longitude}, Alt={msg.altitude}")


def get_current_seq_waypoint(master):
    while master:
        msg = master.recv_match(type=['MISSION_CURRENT'], blocking=True)
        return msg.seq


def get_mode(master):
    last_mode = None

    while True:
        msg = master.recv_match(type='HEARTBEAT', blocking=True)

        if not msg:
            continue

        mode = mavutil.mode_string_v10(msg)

        if mode == "Mode(0x00000000)":
            continue

        if mode != last_mode:
            last_mode = mode
            return last_mode
