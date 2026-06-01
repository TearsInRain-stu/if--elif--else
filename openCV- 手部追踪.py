import cv2
import mediapipe as mp


# 调用MediaPipe的手部检测模块
mpHands = mp.solutions.hands

# 初始化手部识别模型
hands = mpHands.Hands()

# 调用MediaPipe的绘画工具，用于画出手部关节点和连线
mpDraw = mp.solutions.drawing_utils

# 打开电脑默认摄像头
cap = cv2.VideoCapture(0)

handLmsStyle = mpDraw.DrawingSpec(color=(0,154,47),thickness=7,circle_radius=5)
handConStyle = mpDraw.DrawingSpec(color=(0,45,255),thickness=10,circle_radius=5)


while True:
    ret, img = cap.read()
    if ret:
        # 将图像从BGR格式转为RGB格式
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 将图像传入模型，进行手部识别
        result = hands.process(imgRGB)
        # print(result.multi_hand_landmarks)

        # 如果检测到手部关节点
        if result.multi_hand_landmarks:

            # 遍历每一只检测到的手
            for handLms in result.multi_hand_landmarks:

                # 绘制手部的关键点和关节连线
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,handLmsStyle,handConStyle)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
