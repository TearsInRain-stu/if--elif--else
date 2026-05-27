import cv2

# 打开摄像头，id = 0 为默认摄像头
cap = cv2.VideoCapture(0)

# 设置摄像头窗口的宽和长
cap.set(3,1280) # 长
cap.set(4,960)  # 宽

# 展示窗口
while True:
    success,img = cap.read()       # read() return(bool,picture) 
    cv2.imshow("wabcon OUTOUT",img）
    # 按q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
