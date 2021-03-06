import cv2
import mediapipe as mp
import time#用于得知当前时间
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)#捕获摄像头,0一般是笔记本的内置摄像头，1，2，3等等则是接在usb口上的摄像头
mpHands = mp.solutions.hands#简化函数名
hands = mpHands.Hands(False,4,1,0.7,0.7)#配置侦测过程中的相关参数
mpDraw = mp.solutions.drawing_utils#画点用的函数
handLmStyle = mpDraw.DrawingSpec(color = (0,0,255),thickness = 5)#点的样式，#线的样式BGR，前一个参数是颜色，后一个是粗细
handConStyle = mpDraw.DrawingSpec(color = (0,255,0),thickness = 10)#线的样式BGR，#线的样式BGR，前一个参数是颜色，后一个是粗细
pTime = 0
cTime = 0
while True:#读取视频的循环
    ret,img = cap.read()#读入每一帧图像
    if ret:#如果读取不为空值，则显示画面
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#将BGR图像转化为RGB图像，因为mediapie需要的是RGB
        result = hands.process(imgRGB)#导入图像进行识别
        #print(result.multi_hand_landmarks)
        imgHeight = img.shape[0]#得到图像的高
        imgWeight = img.shape[1]#得到图像的宽
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:#循环一遍所有的坐标
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS,handLmStyle,handConStyle)#画出点和线
                for i,lm in enumerate(handLms.landmark):
                    xPos = int(imgWeight*lm.x)#将坐标转化为整数
                    yPos = int(imgHeight*lm.y)
                    cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)#将手上对应的点的编号打印在图片上
                    print(i,xPos,yPos)#将坐标打印出来
    cTime = time.time()#得到当前时间
    fps = 1/(cTime-pTime)#用1除以播放一帧所用时间就可以得出每秒帧数
    pTime = cTime#得到这一帧结束时的时间
    cv2.putText(img,f"FPS:{int(fps)}",(30,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)#将得到的帧数信息打印在图片上
    cv2.imshow("img", img)#展示图片
    if cv2.waitKey(1) ==ord("q"):#如果按下q键，则终止循环
        break