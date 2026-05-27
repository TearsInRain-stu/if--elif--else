import cv2

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,960)

while True:
    success,img = cap.read()
    cv2.imshow("wabcon OUTOUT",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
