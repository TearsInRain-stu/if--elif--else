import cv2

cap = cv2.VideoCapture(r"C:\Users\Aris\Desktop\openCV-Video\Recording 2026-05-14 000432.mp4")

while True:
    success,img = cap.read()
    cv2.imshow("VIDEO OUTPUT",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
