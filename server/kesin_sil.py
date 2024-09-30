from pymavlink import mavutil
import time


def get_gps_loc(master, prev_lat=None, prev_lon=None):
    while True:
        msg = None

        # Kuyruğu boşalt ve son gelen mesajı al
        while True:
            temp = master.recv_match(type='GLOBAL_POSITION_INT', blocking=False)
            if temp is None:
                break
            msg = temp

        # Eğer mesaj yoksa, yeni bir mesaj bekle
        if msg is None:
            msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)

        if msg:
            # En güncel konum verilerini al
            latitude = msg.lat
            longitude = msg.lon

            # Eğer veri öncekiyle aynıysa devam et ve yeni veri bekle
            if latitude == prev_lat and longitude == prev_lon:
                continue
            else:
                # Yeni veriyi döndür
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
        1,  # Arm
        21196,  # Force arm
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

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,  # target_system
        master.target_component,  # target_component
        *rc_channel_values)  # RC channel list, in microseconds.


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
    # Mod değişikliği komutunu gönder
    master.mav.command_long_send(
        master.target_system,  # Hedef sistem ID'si
        master.target_component,  # Hedef bileşen ID'si
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,  # Komut: Mod ayarla
        0,  # Confirmation
        base_mode,  # Param 1: Temel mod
        mode_id,  # Param 2: Özel mod
        0, 0, 0, 0, 0  # Diğer parametreler genellikle 0'dır
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
        # HEARTBEAT mesajını al
        msg = master.recv_match(type='HEARTBEAT', blocking=True)

        if not msg:
            continue

        # Modu al
        mode = mavutil.mode_string_v10(msg)

        # Eğer mod "0x00000000" ise bu durumu es geç
        if mode == "Mode(0x00000000)":
            continue

        # Mod değişikliği olup olmadığını kontrol et
        if mode != last_mode:
            last_mode = mode
            return last_mode
