import matplotlib.pyplot as plt
from pymavlink import mavutil
from matplotlib.animation import FuncAnimation

master = mavutil.mavlink_connection('tcp:localhost:5763')
master.wait_heartbeat()

gps_verileri = []
MAX_POINTS = 1000

fig, ax = plt.subplots(figsize=(10, 10))
line, = ax.plot([], [], 'ro-')


def update(frame):
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    heading_msg = master.recv_match(type='VFR_HUD', blocking=True)
    if msg:
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.alt / 1e3
        gps_verileri.append((lat, lon, alt))
        # Veri miktarını sınırlamak
        if len(gps_verileri) > MAX_POINTS:
            gps_verileri.pop(0)
        enlemler = [data[0] for data in gps_verileri]
        boylamlar = [data[1] for data in gps_verileri]

        line.set_data(boylamlar, enlemler)
        ax.relim()
        ax.autoscale_view()
        plt.axis('equal')


# Burada belirli bir kare sayısı belirtiyoruz (örneğin, 100 kare)
anim = FuncAnimation(fig, update, frames=100, interval=1000)  # Güncellemeyi 1 saniyede bir yapar
plt.xlabel('Boylam')
plt.ylabel('Enlem')
plt.title('Araç Yolu Koordinat Sistemi Üzerinde')
plt.grid(True)
plt.show()
