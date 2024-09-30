import cv2
import numpy as np

# Kamerayı başlat
cap = cv2.VideoCapture(0)

# Çizginin sabit x koordinatı
line_x = 320

while True:
    # Kameradan bir frame oku
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntü boyutlarını al
    height, width, _ = frame.shape

    # Çizginin başlangıç ve bitiş noktalarını belirle
    start_point = (line_x, height)
    end_point = (line_x, height // 2)

    # Çizgiyi çiz (yeşil renkte)
    cv2.line(frame, start_point, end_point, (0, 255, 0), 2)

    # Nesnenin x merkezini belirlemek için bir test noktası ekleyelim (örneğin, x=300)
    object_x_center = 300  # Bu değer normalde YOLOv8 gibi bir tespit algoritmasından gelir

    # Nesnenin çizginin sağında mı solunda mı olduğunu kontrol et
    if object_x_center < line_x:
        konum = "sol"
    elif object_x_center > line_x:
        konum = "sağ"
    else:
        konum = "çizgi üzerinde"

    # Ekranda durumu göster
    cv2.putText(frame, f'Nesne {konum} konumda', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow('Yol Uzerinde Cizgi', frame)

    # 'q' tuşuna basılana kadar döngüde kal
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
