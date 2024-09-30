import socket
import win32pipe
import win32file
import threading

class Server_solari:
    def __init__(self, port, pipe_name):
        self.port = port
        self.pipe_name = pipe_name
        self.server_socket = None
        self.pipe = None
        self.client_thread = None
        self.conn = None
        self.addr = None
        self.stop_event = threading.Event()  # Event to signal the thread to stop

    def start(self):
        # Named Pipe oluştur
        try:
            self.pipe = win32pipe.CreateNamedPipe(
                self.pipe_name,
                win32pipe.PIPE_ACCESS_DUPLEX,
                win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
                1, 65536, 65536,
                0,
                None
            )
            print("[INFO] Waiting for pipe connection...")
            win32pipe.ConnectNamedPipe(self.pipe, None)

            # TCP sunucusunu başlat
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(('192.168.1.187', self.port))
            self.server_socket.listen(1)
            print(f"[INFO] Server listening on localhost:{self.port}")

            # İstemci işleme iş parçacığını başlat
            self.client_thread = threading.Thread(target=self.handle_client)
            self.client_thread.start()

        except Exception as e:
            print(f"[ERROR] Failed to start the server: {e}")
            self.stop()

    def handle_client(self):
        while not self.stop_event.is_set():
            try:
                # TCP bağlantısını kabul et
                self.conn, self.addr = self.server_socket.accept()
                print(f"[INFO] New connection from {self.addr}")

                while not self.stop_event.is_set():
                    # TCP üzerinden veri al
                    data = self.conn.recv(1024)
                    if not data:
                        print("[INFO] Client disconnected.")
                        break

                    # Veriyi ayrıştır
                    try:
                        if data is not None:
                            data_str = data.decode('utf-8').strip()
                            loadcell, temp = self.parse_data(data_str)
                            formatted_message = f"{loadcell},{temp}"

                            # Veriyi Named Pipe'a yaz
                            win32file.WriteFile(self.pipe, formatted_message.encode('utf-8'))
                    except Exception as e:
                        print(f"[ERROR] Data parsing or writing failed: {e}")

            except Exception as e:
                print(f"[ERROR] {e}")
                break

            finally:
                if self.conn:
                    self.conn.close()
                    print("[INFO] Connection closed.")

        # Cleanup when the loop exits
        print("[INFO] Closing pipe and server socket.")
        if self.pipe:
            try:
                win32pipe.DisconnectNamedPipe(self.pipe)
                win32file.CloseHandle(self.pipe)
            except Exception as e:
                print(f"[ERROR] {e}")
        if self.server_socket:
            self.server_socket.close()

    def parse_data(self, data):
        """Veriyi ayrıştırır ve Loadcell, Temp değerlerini döner."""
        try:
            parts = data.split(',')

            if len(parts) != 2:
                raise ValueError("Data format is incorrect")

            loadcell = float(parts[0].strip())
            temp = float(parts[1].strip())
            return loadcell, temp
        except ValueError as e:
            print(f"[ERROR] Data parsing error: {e}")
            #print(data)
            return 0.0, 0.0  # Humid değeri çıkarıldı

    def send_message(self, msg):
        if self.conn:
            try:
                print(f"[INFO] Sending message: {msg}")
                self.conn.sendall(msg.encode())
            except Exception as e:
                print(f"[ERROR] Failed to send message: {e}")

    def stop(self):
        if self.server_socket:
            self.server_socket.close()
            print("[INFO] Server socket closed.")

        if self.pipe:
            try:
                win32pipe.DisconnectNamedPipe(self.pipe)
                win32file.CloseHandle(self.pipe)
                print("[INFO] Named pipe closed.")
            except Exception as e:
                print(f"[ERROR] {e}")

        if self.client_thread:
            self.stop_event.set()
            self.client_thread.join()
            print("[INFO] Client thread has finished.")

        # Reset variables
        self.server_socket = None
        self.pipe = None
        self.client_thread = None
