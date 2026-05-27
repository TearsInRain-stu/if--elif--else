import cv2

# 创建变量img来储存图片
# cv2.imread函数用来读取图片
# 语法:cv2.imread(r"address")

img = cv2.imread(r"C:\Users\Aris\Desktop\piture\gzp2DYV2.jpeg")

# 显示图片的函数
# imshow函数创建窗口
# 语法:imshow（“窗口名”，图片变量）
cv2.imshow("output",img)

# 延迟窗口显示函数
# 语法:wait() 0为按任意键退出 数字为 毫秒后退出
cv2.waitKey(0) 
