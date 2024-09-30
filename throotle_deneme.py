from pymavlink import mavutil


master = mavutil.mavlink_connection("tcp:localhost:5763")
master.wait_heartbeat()

rc_channels = master.recv_match(type='RC_CHANNELS', blocking=True)
print(rc_channels)