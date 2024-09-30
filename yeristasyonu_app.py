#####################################################
# Coded by Rolesa
# https://github.com/Rolesa/
# instagram.com/tunahangenc_c
#####################################################




import sys
import threading
import concurrent.futures
import time

import serial
from pymavlink import mavwp
import cv2
import numpy as np
import requests
import torch
import win32file
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Slot, QThread, Signal, QTimer
from ultralytics import YOLO
from ana_server import Server_solari
from server.kesin_sil import *
from yeristasyonu import *
import math



class SharedData:
    def __init__(self):
        self.loadcell_ilet = True


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.tcp_thread = None
        self.thread_engel = None
        self.thread_stop_resume = None
        self.current_status_thread = None
        self.throttle_thread = None
        self.shared_data = SharedData()
        self.mavlink_server = None
        self.connection_text = None
        self.current_seq = None
        self.last_wp = None
        self.start_listener_if_server_started = None
        self.thread = None
        self.Nx = None
        self.Ny = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sensorler_alt_widget.hide()
        self.ui.veriler_alt_widget.hide()
        self.ui.home_btn.setDisabled(True)
        self.ui.home_btn.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.ui.home_btn.setStyleSheet("color: rgb(0,0,0);")
        self.ui.home_btn.clicked.connect(self.change_window)
        self.ui.kamera_btn.clicked.connect(self.change_window)
        self.ui.waypoint_btn.clicked.connect(self.change_window)
        self.ui.viewData.setScaledContents(True)

        self.timer_kaldir = QTimer(self)
        self.timer_kaldir.setSingleShot(True)
        self.timer_kaldir.timeout.connect(self.resume_mission)

        self.timer_indir = QTimer(self)
        self.timer_indir.setSingleShot(True)
        self.timer_indir.timeout.connect(self.resume_mission)

        self.engel_kaldir_timer = QTimer(self)
        self.engel_kaldir_timer.setSingleShot(True)
        self.engel_kaldir_timer.timeout.connect(self.capa_throotle)

        self.bitki_gps_list = []
        self.last_move_x = 0
        self.last_move_y = 0
        self.frame_num = 0
        self.waypoints = []
        self.waypoint_down = []
        self.waypoint_up = []
        ###########################################################
        ########################DHT11##############################
        self.dht11_pipe_address = r'\\.\pipe\shared_pipe'
        self.dht11_port_adress = 5052
        self.server = Server(port=self.dht11_port_adress, address=self.dht11_pipe_address)  # sonradan eklendi (port)
        self.server_thread = ServerThread(self.server)
        self.server_thread.start()
        self.pipe_listener = PipeListener(shared_data=self.shared_data)
        self.pipe_listener_thread = None
        ###########################################################
        self.menubuttons = {
            self.ui.home_btn: {
                "btn": self.ui.home_btn,
                "icon_path": "icons/home.svg",
                "index": 0
            },
            self.ui.kamera_btn: {
                "btn": self.ui.kamera_btn,
                "icon_path": None,
                "index": 1
            },
            self.ui.waypoint_btn: {
                "btn": self.ui.waypoint_btn,
                "icon_path": None,
                "index": 3
            }
        }
        #####################CAM####################################
        self.ProcessCam = Camera(self.shared_data)

        if self.ProcessCam.connection:
            self.debugbar("Connected frame waiting for start")
            self.ProcessCam.raw_data.connect(self.getRaw)
            self.ui.start_btn.setEnabled(True)
            self.ui.stop_btn.setEnabled(False)
            self.ui.close_btn.setEnabled(False)
        else:
            self.debugbar("Connection error to frame Server.. ")
            self.ui.start_btn.setEnabled(False)
            self.ui.close_btn.setEnabled(False)
            self.ui.stop_btn.setEnabled(False)
        self.ui.start_btn.clicked.connect(self.openCam)
        self.ui.stop_btn.clicked.connect(self.stopCam)
        self.ui.close_btn.clicked.connect(self.closeCam)
        #########################################################
        self.pipe_listener.sensor_data.connect(self.dht_label)
        self.pipe_listener.loadcell_data.connect(self.loadcell_label)
        self.pipe_listener.loadcell_data.connect(self.engel_tespit)
        self.ui.mavlink_button.clicked.connect(self.start_mavlink_thread)
        self.ui.mission_wp_send_btn.clicked.connect(self.send_mission_waypoints)
        self.ProcessCam.bitki_gps.connect(self.bitki_gps)
        self.ui.get_gps_button.clicked.connect(self.get_gps)
        self.ui.send_waypoints_button.clicked.connect(self.send_gps)
        self.ui.clear_elemets.clicked.connect(self.clear_elemets)
        self.ui.pushButton_2.clicked.connect(self.resume_stop_mission)
        self.ui.pushButton.clicked.connect(self.disconnect_mavlink)
        self.ui.manual_btn.clicked.connect(self.start_manual_mode)
        self.ui.hold_btn.clicked.connect(self.start_hold_mode)
        self.ui.send_cord_btn.clicked.connect(self.add_gps_manual_cord)
        self.ui.force_arm_btn.clicked.connect(self.arm)
        self.ui.disarm_btn.clicked.connect(self.disarm)
        self.ui.auto_mode_start_btn.clicked.connect(self.start_autonom_mode)
        self.ui.capa_test_up.clicked.connect(self.test_capa_up)
        self.ui.capa_test_down.clicked.connect(self.test_capa_down)


    def on_tcp_thread_finished(self):
        print("TCP operation completed.")

    def set_false_run(self):
        self.current_status_thread.running = False

    def set_true_run(self):
        self.current_status_thread.running = True

    def bitki_gps(self, lat, lon):
        self.ui.konum_Label.setText(str((lat, lon)))
        self.bitki_gps_list.append((lat, lon))

    def waypoint_capa_up_mission(self, seq):
        if self.mavlink_server and self.waypoint_up and int(seq) in self.waypoint_up:
            self.capa_kaldir()

    def waypoint_capa_down_mission(self, seq):
        if self.mavlink_server and self.waypoint_down and int(seq) in self.waypoint_down:
            self.capa_indir()

    def send_mission_waypoints(self):
        wp_kaldir = self.ui.capa_kalk_wp.text().split(',')
        wp_indir = self.ui.capa_in_wp.text().split(',')
        if self.waypoint_up:
            self.waypoint_up.clear()
        if self.waypoint_down:
            self.waypoint_down.clear()
        self.waypoint_down = [int(i) for i in wp_indir]
        self.waypoint_up = [int(i) for i in wp_kaldir]

        self.ui.kalkcak_wp.setText(str(self.waypoint_up))
        self.ui.incek_wp.setText(str(self.waypoint_down))

    def capa_throotle(self):
        self.throttle_thread = ThrottleThread(self.mavlink_server, self)
        self.throttle_thread.start()

    def engel_capa_indir(self):
        auto_mode_start(self.mavlink_server, "AUTO")
        current_time = time.time()
        last_time = time.time()
        while last_time - current_time <= 2:
            last_time = time.time()
        self.server.last.send_message(str(1))
        self.shared_data.loadcell_ilet = True

    def engel_capa_kaldir(self, success):
        if success:
            self.server.last.send_message(str(0))
            self.engel_kaldir_timer.start(5000)

    def resume_mission(self):
        print("tunahan 2 ")
        auto_mode_start(self.mavlink_server, "AUTO")
        self.shared_data.loadcell_ilet = True

    def test_capa_up(self):
        self.server.last.send_message(str(0))

    def test_capa_down(self):
        self.server.last.send_message(str(1))

    def capa_indir(self):
        print("Tunahan")
        auto_mode_start(self.mavlink_server, "HOLD")
        self.server.last.send_message(str(1))
        # self.timer_indir.timeout.connect(self.resume_mission)  # Bu satırı yeniden ekleyin
        self.timer_indir.start(5000)

    def capa_kaldir(self):
        auto_mode_start(self.mavlink_server, "HOLD")
        self.server.last.send_message(str(0))
        self.timer_kaldir.start(5000)

    def arm(self):
        if self.mavlink_server:
            force_arm_vehicle(self.mavlink_server)

    def disarm(self):
        if self.mavlink_server:
            disarm_vehicle(master=self.mavlink_server)

    def start_hold_mode(self):
        if self.mavlink_server:
            auto_mode_start(self.mavlink_server, "HOLD")

    def start_manual_mode(self):
        if self.mavlink_server:
            auto_mode_start(self.mavlink_server, "MANUAL")

    def start_autonom_mode(self):
        if self.mavlink_server:
            auto_mode_start(self.mavlink_server, "AUTO")

    def resume_stop_mission(self):
        if self.ui.lineEdit.text():
            print(f"Resuming mission... {self.ui.lineEdit.text()}")
            self.thread_stop_resume = resume_stop_mission(self.ui.lineEdit.text(), self.mavlink_server)
            self.thread_stop_resume.start()
        else:
            self.thread_stop_resume = resume_stop_mission(self.last_wp, self.mavlink_server)
            self.thread_stop_resume.start()

    def engel_tespit(self, var):
        # Yeni bir thread başlatın
        self.thread_engel = EngelTespitThread(var, self.mavlink_server, self.shared_data)
        self.thread_engel.finished.connect(self.engel_capa_kaldir)
        self.thread_engel.start()

    def on_engel_tespit_finished(self):
        self.ui.label_23.setText("Capalama bitti")

    def disconnect_mavlink(self):
        if self.mavlink_server is not None:
            self.current_status_thread.stop_thread.emit()
            self.mavlink_server.close()
            self.mavlink_server = None
            self.ui.label_22.setText("Kesildi")
            self.ui.label_30.setText("No Mavlink")

    def waypoint_seq_label(self, seq):
        self.ui.current_waypoint_seq.setText(str(seq))
        self.last_wp = seq + 1
        self.current_seq = seq

    def clear_elemets(self):
        if self.waypoints:
            self.waypoints.clear()
            self.ui.waypoint_edit_line.clear()
            self.ui.waypoint_list.clear()

    def send_gps(self):
        if self.waypoints and self.mavlink_server:
            self.shared_data.loadcell_ilet = False
            wp = mavwp.MAVWPLoader()
            for seq, (lat, lon) in enumerate(self.waypoints):
                frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
                altitude = 100
                autocontinue = 1
                current = 0
                param1 = 0

                if seq == 0:
                    current = 1  # İlk waypoint'i current olarak ayarla
                elif seq == len(self.waypoints) - 1:
                    param1 = 0  # Son waypoint'te param1'i sıfırla

                p = mavutil.mavlink.MAVLink_mission_item_int_message(
                    self.mavlink_server.target_system,
                    self.mavlink_server.target_component,
                    seq,
                    frame,
                    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
                    current,
                    autocontinue,
                    param1, 0, 0, 0,
                    int(lat), int(lon), int(altitude)
                )
                wp.add(p)
                print(f"Waypoint {seq} eklendi: Lat={lat}, Lon={lon}, Alt={altitude}")

                # Home location'ı ayarla
            home_location = self.waypoints[0]
            lat, lon = home_location[0], home_location[1]
            print(home_location)

            cmd_set_home(master=self.mavlink_server, home_location=(lat / 1e7, lon / 1e7), altitude=100)
            # cmd_get_home(connection=self.mavlink_server)

            time.sleep(1)

            print(f"Toplam waypoint sayisi: {wp.count()}")

            self.mavlink_server.waypoint_clear_all_send()
            self.mavlink_server.waypoint_count_send(wp.count())

            for i in range(wp.count()):
                print(i)
                self.mavlink_server.mav.send(wp.wp(i))
                print(f'Waypoint {i} gönderildi')
            self.shared_data.loadcell_ilet = True

    def get_gps(self):
        self.shared_data.loadcell_ilet = False
        if self.mavlink_server:
            lat, lon = get_gps_loc(self.mavlink_server)
            if lat is not None and lon is not None:
                self.waypoints.append((lat, lon))
                self.ui.waypoint_edit_line.append(f"Wapoint eklendi: Latitude: {lat}, Longitude: {lon}")
                self.ui.waypoint_list.setText(str(self.waypoints))
                waypoint_strings_s = [f"({lat},{lon})" for lat, lon in self.waypoints]
                waypoints_text_t = '\n'.join(waypoint_strings_s)
                self.ui.waypoint_list.setText(waypoints_text_t)
                self.shared_data.loadcell_ilet = True
            else:
                print("GPS verisi alınamadı.")
        else:
            self.response_box_failed("No mavlink connection.")

    def openCam(self):
        if self.ProcessCam.connection:
            self.ProcessCam.open()
            self.debugbar("Opening Camera")
            self.ui.start_btn.setEnabled(False)
            self.ui.stop_btn.setEnabled(True)
            self.ui.close_btn.setEnabled(True)

    def stopCam(self):
        if self.ProcessCam.connection:
            self.ProcessCam.stop()
            self.ui.stop_btn.setEnabled(False)
            self.ui.start_btn.setEnabled(True)
            self.debugbar("Stopping Camera")

    def closeCam(self):
        if self.ProcessCam.connection:
            self.ProcessCam.close()
            self.ui.viewData.clear()
            time.sleep(1)
            self.ui.start_btn.setEnabled(True)
            self.ui.stop_btn.setEnabled(False)
            self.ui.close_btn.setEnabled(False)

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                               "QUIT",
                                               "Are you sure want to stop process?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            self.server.stopServer()
            self.pipe_listener.stop_listening()
            time.sleep(4)

            if self.mavlink_server is not None:
                self.current_status_thread.stop_thread.emit()

                self.mavlink_server.close()
                self.mavlink_server = None
            if self.pipe_listener_thread is not None:
                self.pipe_listener_thread.quit()
                self.pipe_listener_thread.wait()
            event.accept()

        else:
            event.ignore()

    def add_gps_manual_cord(self):
        if self.ui.gps_manual_add.text():
            raw_gps = self.ui.gps_manual_add.text().split(',')
            self.waypoints.append((int(raw_gps[0]), int(raw_gps[1])))
            waypoint_strings = [f"({lat},{lon})" for lat, lon in self.waypoints]
            waypoints_text = '\n'.join(waypoint_strings)
            self.ui.waypoint_list.setText(waypoints_text)

    def start_mavlink_thread(self):
        # Start the MAVLink thread
        connection_text = self.ui.mavlink_lineedit.text().strip()
        self.mavlink_thread = MavlinkThread(connection_text)
        self.mavlink_thread.heartbeat_received.connect(self.on_heartbeat_received)
        self.mavlink_thread.start()

    def on_heartbeat_received(self):
        self.mavlink_server = self.mavlink_thread.mavlink_server
        self.ui.label_22.setText(f"Baglandi ")
        self.response_box("Mavlink connection succesfully")
        self.ProcessCam.set_mavlink_server(self.mavlink_server)
        self.current_status_thread = CurrentStatus()

        self.current_status_thread.set_mavlink_server(self.mavlink_server)
        self.current_status_thread.running = True
        self.current_status_thread.start()
        self.current_status_thread.mode_changed.connect(self.mode_label)
        self.current_status_thread.set_mavlink_server(self.mavlink_server)

        self.current_status_thread.waypoint_changed.connect(self.waypoint_seq_label)
        self.current_status_thread.waypoint_changed.connect(self.waypoint_capa_up_mission)
        self.current_status_thread.waypoint_changed.connect(self.waypoint_capa_down_mission)

    def getRaw(self, data):
        self.showdata(data)

    def showdata(self, img):
        self.Ny, self.Nx, _ = img.shape
        qimg = QtGui.QImage(img.data, self.Nx, self.Ny, QtGui.QImage.Format.Format_RGB888)
        self.ui.viewData.setScaledContents(True)
        self.ui.viewData.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def dht_label(self, var):
        self.ui.dht11_veriable.setText(var)

    def mode_label(self, mode):
        self.ui.label_30.setText(mode)

    def loadcell_label(self, var):
        self.ui.loadcell_veriable.setText(var)

    def response_box(self, response) -> None:
        self.ui.textEdit.setTextColor(QColor("black"))
        self.ui.textEdit.append(f"[+] {response} ")

    def response_box_failed(self, response) -> None:
        self.ui.textEdit.setTextColor(QColor("black"))
        self.ui.textEdit.append(f"[-] {response} ")

    def debugbar(self, msg):
        self.ui.statusbar.showMessage(str(msg), 5000)

    def change_window(self):
        button = self.sender()
        clicked_btn_info = self.menubuttons[button]
        self.ui.anasayfa_baslik_text.setText(clicked_btn_info["btn"].text().strip())
        # print(self.ui.anasayfa_baslik_text.setText(clicked_btn_info["btn"].text().strip()))
        if clicked_btn_info["icon_path"] is not None:
            pixmap = QPixmap(clicked_btn_info["icon_path"])
            self.ui.home_icon.setPixmap(pixmap)
        for value in self.menubuttons.values():
            if value["btn"] == clicked_btn_info["btn"]:
                clicked_btn_info["btn"].setDisabled(True)
                clicked_btn_info["btn"].setStyleSheet("background-color:rgb(222, 222, 222);")
                clicked_btn_info["btn"].setStyleSheet("color: rgb(0,0,0);")

                self.ui.sayfalar.setCurrentIndex(value['index'])
            else:
                value['btn'].setDisabled(False)
                value['btn'].setStyleSheet("background-color: white;")


class resume_stop_mission(QThread):
    def __init__(self, var, mavlink_server, parent=None):
        super(resume_stop_mission, self).__init__(parent)
        self.mavlink_server = mavlink_server
        self.var = var

    def run(self):
        try:
            print(float(self.var))
            self.mavlink_server.mav.mission_set_current_send(
                self.mavlink_server.target_system,
                self.mavlink_server.target_component,
                int(self.var)
            )
        finally:
            self.quit()
            self.wait()


class ThrottleThread(QThread):
    def __init__(self, mavlink_server, main_window, parent=None):
        super(ThrottleThread, self).__init__(parent)
        self.mavlink_server = mavlink_server
        self.main_window = main_window  # MainWindow örneğini burada saklıyoruz

    def run(self):
        print('capa_throotle')
        # current_time = time.time()
        # current_time2 = time.time()
        # while current_time2 - current_time <= 2:
        #    set_throttle_(self.mavlink_server, 2, 1800)
        #    current_time2 = time.time()
        # print("capa_throotle bitti")
        self.main_window.engel_capa_indir()


class EngelTespitThread(QThread, QTimer):
    finished = Signal(bool)  # İşlem bittiğinde sinyal gönderir

    def __init__(self, var, mavlink_server, shared_data, parent=None):
        super(EngelTespitThread, self).__init__(parent)
        self.var = var
        self.mavlink_server = mavlink_server
        self.shared_data = shared_data

    def run(self):
        if float(self.var) == float(7000) and not None:
            self.shared_data.loadcell_ilet = False
            auto_mode_start(self.mavlink_server, "MANUAL")
            self.finished.emit(True)
        # İşlem bittiğinde finished sinyalini gönder
        else:
            self.finished.emit(False)


class Camera(QtCore.QThread):
    raw_data = QtCore.Signal(np.ndarray)
    bitki_gps = QtCore.Signal(float, float)

    def __init__(self, shared_data, parent=None):
        super().__init__(parent)
        self.stream = None
        self.url = 'http://192.168.1.198:5000/video_feed'
        self.connection = True
        self.model = YOLO("C:/Users/kuddu/Desktop/artik_son.pt").to('cuda')
        self.running = False
        self.mavlink_server = None
        self.shared_data = shared_data
        self.last_detection_time = 0
        self.lock = threading.Lock()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        self.gps_listener_thread = None
        self.retry_timer = QtCore.QTimer()
        self.retry_timer.setInterval(5000)
        self.retry_timer.timeout.connect(self.retry_connection)

    def run(self):
        while self.connection:
            if not self.running:
                break

            self.retry_timer.start()
            while True:
                if not self.running:
                    break
                try:
                    with requests.get(self.url, stream=True, timeout=(5, 10)) as stream:
                        print(stream.status_code)
                        if stream.status_code == 200:
                            bytes_data = b''

                            for chunk in stream.iter_content(chunk_size=65536):
                                if not self.running:
                                    break
                                bytes_data += chunk

                                a = bytes_data.find(b'\xff\xd8')
                                b = bytes_data.find(b'\xff\xd9')

                                if a != -1 and b != -1 and b > a:
                                    jpg = bytes_data[a:b + 2]
                                    bytes_data = bytes_data[b + 2:]
                                    img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                                    if img is not None:
                                        self.raw_data.emit(self.process_frame(img))
                                else:

                                    if len(bytes_data) > 2 * 65536:
                                        bytes_data = b''

                                if self.check_for_delay(bytes_data):
                                    self.retry_connection()
                                    break

                        else:
                            print(f"Stream error: Status code {stream.status_code}")
                except requests.RequestException as e:
                    print(f"Connection error: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")

                QtCore.QThread.msleep(10)

    def retry_connection(self):
        if not self.running:
            return
        self.start()

    def check_for_delay(self, bytes_data):
        return len(bytes_data) > 2 * 65536

    def set_mavlink_server(self, mavlink_server):
        self.mavlink_server = mavlink_server

    def process_frame(self, frame):
        height, width, _ = frame.shape
        line_y1 = height // 2 - 50
        line_y2 = height // 2 + 50
        line_x1 = (width // 2) - 130
        line_x2 = (width // 2) + 130

        offset = 50

        results = self.model.predict(source=frame, conf=0.9, verbose=False, device=0)

        overlay = frame.copy()
        pts = np.array(
            [[line_x1, line_y1], [line_x2, line_y1], [line_x2, line_y2], [line_x1, line_y2]])
        cv2.fillPoly(overlay, [pts], (0, 255, 0))
        alpha = 0.3
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
        current_time = time.time()

        for result in results:
            for bbox in result.boxes:
                x_min, y_min, x_max, y_max = bbox.xyxy[0].cpu().numpy().astype(int)

                class_id = int(bbox.cls[0].cpu().numpy())
                class_name = result.names[class_id]

                x_center = int((x_min + x_max) // 2)
                y_center = int((y_min + y_max) // 2)

                cv2.circle(frame, (int(x_center), int(y_center)), 5, (255, 0, 0), -1)
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                if line_y1 <= y_center <= line_y2 and current_time - self.last_detection_time > 10:
                    if x_center < (width // 2) - offset:
                        region = "sol"
                    elif x_center > (width // 2) + offset:
                        region = "sag"
                    else:
                        region = None

                    if region:
                        with self.lock:
                            self.executor.submit(self.detect_and_emit_gps, region)
                        self.last_detection_time = current_time

        # Dikey sınır çizgilerini çizme
        cv2.line(frame, (line_x1, 0), (line_x1, height), (0, 0, 255), 3)  # Sol dikey çizgi (kırmızı)
        cv2.line(frame, (line_x2, 0), (line_x2, height), (0, 0, 255), 3)  # Sağ dikey çizgi (kırmızı)

        return frame

    def detect_and_emit_gps(self, arg):
        if self.mavlink_server is not None:
            self.shared_data = False
            auto_mode_start(master=self.mavlink_server, mode_name="HOLD")

            heading = self.get_heading(self.mavlink_server)
            lat, lon = self.get_gps_loc(self.mavlink_server)

            print(f"Current: lat: {lat}, lon: {lon}, heading: {heading}")
            if heading is not None:
                if arg == "sol":
                    if heading >= 270 or heading <= 90:
                        lat, lon = self.calculate_new_gps(heading, lat, lon, "LEFT")
                    else:
                        lat, lon = self.calculate_new_gps(heading, lat, lon, "RIGHT")
                elif arg == "sag":
                    if heading >= 270 or heading <= 90:
                        lat, lon = self.calculate_new_gps(heading, lat, lon, "RIGHT")
                    else:
                        lat, lon = self.calculate_new_gps(heading, lat, lon, "LEFT")

                self.bitki_gps.emit(lat, lon)
                auto_mode_start(master=self.mavlink_server, mode_name="AUTO")
                self.shared_data = True
                print(f"Detected object at region {arg}. Emitted GPS: lat={lat}, lon={lon}")

    def calculate_new_gps(self, heading, lat, lon, direction):
        distance = 0.0000044915
        if direction == "RIGHT":
            angle = (heading + 90) % 360
        elif direction == "LEFT":
            angle = (heading - 90) % 360

        delta_lat = distance * math.cos(math.radians(angle))
        delta_lon = distance * math.sin(math.radians(angle))

        new_lat = lat + delta_lat
        new_lon = lon + delta_lon
        return new_lat, new_lon

    def get_heading(self, master):
        if self.mavlink_server is None:
            return None
        while True:
            msg = None
            while True:
                temp = self.mavlink_server.recv_match(type='VFR_HUD', blocking=False)
                if temp is None:
                    break
                msg = temp

            if msg is None:
                msg = master.recv_match(type='VFR_HUD', blocking=True)

            if msg:
                heading = msg.heading
                return heading

    def get_gps_loc(self, mavlink_server):
        while True:
            msg = mavlink_server.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
            if msg:
                lat = msg.lat / 1e7
                lon = msg.lon / 1e7
                return lat, lon

    def auto_mode_start(self, master, mode_name):
        mode_id = master.mode_mapping()[mode_name]
        master.set_mode(mode_id)

    def start_gps_listener(self):
        if self.gps_listener_thread is None or not self.gps_listener_thread.is_alive():
            self.gps_listener_thread = threading.Thread(target=self.run_gps_listener)
            self.gps_listener_thread.start()

    def run_gps_listener(self):
        while self.running:
            QtCore.QThread.sleep(1)

    def stop(self):
        self.running = False
        self.retry_timer.stop()
        if self.gps_listener_thread is not None:
            self.gps_listener_thread.join()

    def open(self):
        if self.connection:
            self.running = True
            if not self.isRunning():
                self.start()

    def close(self):
        self.running = False
        if self.gps_listener_thread:
            self.gps_listener_thread.stop_listening()
            self.gps_listener_thread.quit()
            self.gps_listener_thread.wait()


class Server(QObject):
    def __init__(self, port, address):
        super().__init__()
        self.address = address
        self.port = port
        self.last = Server_solari(port=self.port, pipe_name=self.address)

    def startServer(self):
        self.last.start()

    def stopServer(self):
        self.last.stop()


class ServerThread(QThread):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        self.server.startServer()


class CurrentStatus(QThread):  # değisti test gunu degismemis hali chatgpt de var
    waypoint_changed = Signal(int)
    mode_changed = Signal(str)
    stop_thread = Signal()

    def __init__(self):
        super().__init__()
        self.mavlink_server = None
        self.running = True

    def set_mavlink_server(self, mavlink_server):
        self.mavlink_server = mavlink_server

    def request_message_interval(self, master, message_input: str, frequency_hz: float):
        message_name = "MAVLINK_MSG_ID_" + message_input
        message_id = getattr(mavutil.mavlink, message_name)

        master.mav.command_long_send(
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
            message_id,
            1e6 / frequency_hz,
            0,
            0, 0, 0, 0
        )
        print(f"Requested {message_input} message successfully.")

    def run(self):
        if self.mavlink_server is None:
            print("MAVLink server bağlantısı kurulamadı.")
            return

        master = self.mavlink_server

        # Waypoint ve Mode için gerekli mesaj frekanslarını ayarla
        self.request_message_interval(master, "MISSION_CURRENT", 10)

        last_seq = None
        last_mode = None
        self.stop_thread.connect(self.stop)

        while self.running:
            try:
                # MISSION_CURRENT ve HEARTBEAT mesajlarını sırayla al
                msg = master.recv_match(type=['MISSION_CURRENT', 'HEARTBEAT'], blocking=True, timeout=0.1)

                if not msg:
                    continue

                if msg.get_type() == 'MISSION_CURRENT':
                    seq = msg.seq
                    if seq != last_seq:
                        print(seq - 1)
                        self.waypoint_changed.emit(seq - 1)
                        last_seq = seq

                elif msg.get_type() == 'HEARTBEAT' and self.running:
                    mode = mavutil.mode_string_v10(msg)
                    if mode != "Mode(0x00000000)" and mode != last_mode:
                        self.mode_changed.emit(mode)
                        last_mode = mode

                time.sleep(0.05)

            except Exception as e:
                print(f"Veri alımı sırasında hata: {e}")
                time.sleep(1)  # Hata durumunda kısa bir bekleme

    def stop(self):
        self.running = False
        self.mavlink_server = None


class MavlinkThread(QThread):
    # Signal to emit when the heartbeat is received
    heartbeat_received = Signal()

    def __init__(self, connection_text, baudrate=57600):
        super().__init__()
        self.connection_text = connection_text
        self.baudrate = baudrate
        self.mavlink_server = None

    def run(self):
        # Establish the MAVLink connection
        if self.connection_text:
            try:
                if self.mavlink_server is None:
                    self.mavlink_server = mavutil.mavlink_connection(self.connection_text, baud=self.baudrate)
                    # Wait for a heartbeat
                    self.mavlink_server.wait_heartbeat()
                    # Emit the signal to notify that the heartbeat is received
                    self.heartbeat_received.emit()
            except Exception as e:
                print(f"mavlink server error {e}")


class PipeListener(QObject):
    loadcell_data = Signal(str)  # Loadcell verileri için sinyal
    sensor_data = Signal(str)  # Temp ve Humid verileri için sinyal
    pipe_name = r'\\.\pipe\shared_pipe'  # Tek bir pipe adresi

    def __init__(self, shared_data):
        super().__init__()
        self.pipe_handle = None
        self.is_listening = False
        self.pipe_loadcell_data = shared_data  # Shared data'yı al

        # QTimer ile döngü oluşturalım
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_pipe)

    @Slot()
    def listen_pipe(self):
        if self.pipe_name is None:
            print("Pipe adı belirtilmedi")
            return
        self.is_listening = True
        try:
            self.pipe_handle = win32file.CreateFile(
                self.pipe_name,
                win32file.GENERIC_READ,
                0,
                None,
                win32file.OPEN_EXISTING,
                0,
                None
            )
            print(f"Named pipe '{self.pipe_name}' bulundu. Pipe'dan okuma yapılıyor...")
            self.timer.start(50)  # Her 50 ms'de bir read_pipe fonksiyonunu tetikler

        except win32file.error as e:
            print(f"Named pipe '{self.pipe_name}' hatası: {e}. 1 saniye sonra tekrar deneniyor...")
            self.timer.start(1000)  # Hata durumunda 1 saniye bekler

    @Slot()
    def restart_listening(self):
        self.is_listening = True
        self.timer.start()
        self.listen_pipe()
    @Slot()
    def read_pipe(self):
        if self.pipe_handle is not None and self.pipe_loadcell_data.loadcell_ilet:
            try:
                data = win32file.ReadFile(self.pipe_handle, 4096)[1]
                decoded_data = data.decode().strip()
                self.parse_and_emit_data(decoded_data)

            except win32file.error as e:
                print(f"Read error: {e}")
                self.stop_listening()

    @Slot()
    def stop_listening(self):
        self.is_listening = False
        self.timer.stop()  # Timer'ı durdur
        if self.pipe_handle is not None:
            win32file.CloseHandle(self.pipe_handle)
            print(f"{self.pipe_name} başarıyla kapatıldı")
            self.pipe_handle = None

    def parse_and_emit_data(self, data):
        """Veriyi ayrıştırır ve uygun sinyali yayar."""
        try:
            parts = data.split(',')
            if len(parts) == 2:
                loadcell = parts[0].strip()
                temp = parts[1].strip()

                # Veriyi loadcell_ilet koşuluna göre sinyallere yay
                self.loadcell_data.emit(loadcell)
                self.sensor_data.emit(f"{temp}")  # degiscek sadece temp gitcek
            else:
                print("[ERROR] Veri formatı yanlış")
        except Exception as e:
            print(f"[ERROR] Veriyi ayrıştırırken bir hata oluştu: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.pipe_listener_thread = QThread()
    window.pipe_listener.moveToThread(window.pipe_listener_thread)
    window.pipe_listener_thread.started.connect(window.pipe_listener.listen_pipe)
    window.pipe_listener_thread.start()
    window.show()
    sys.exit(app.exec())
