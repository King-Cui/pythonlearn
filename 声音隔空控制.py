import math
from datetime import time

import cv2
import mediapipe as mp
import numpy as np
import pyautogui

#################################
# 相机参数
from comtypes import CLSCTX_ALL
from numpy.core.numerictypes import cast
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from selenium.webdriver.common.actions.interaction import POINTER

wCam, hCam = 640, 480

videoCap = cv2.VideoCapture(0)
videoCap.set(3, wCam)  # 设置摄像头高度
videoCap.set(4, hCam)  # 设置这项头高度

#################################
# 显示FPS
cTime = 0
pTime = 0

##################################
# mediapipe模块初始化
mode = False
maxHands = 2
detectionCon = 0.5
trackCon = 0.5
mpHands = mp.solutions.hands
hands = mpHands.Hands(mode, maxHands, detectionCon, trackCon)
mpDraw = mp.solutions.drawing_utils

################################
# 音量模块初始化
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute() # 静音
# volume.GetMasterVolumeLevel() # 主音量等级
# volume.GetVolumeRange() # 主音量范围
# volume.SetMasterVolumeLevel(-20.0, None) # 设置主音量
# print(volume.GetVolumeRange()) #  (-63.5, 0.0, 0.5)

#################################
# 获取当前音量范围(range)和最大最小音量
volumeRange = volume.GetVolumeRange()  # 获取当前主音量范围
minVol = volumeRange[0]
maxVol = volumeRange[1]
# 后面映射部分需要用到
vol = 0
volBar = 400
volPer = 0
#################################

cap = cv2.VideoCapture(0)  #若使用外接摄像头 则更改为1或其他编号
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


def handDetector():
    pass


detector = handDetector()
success, img = cap.read()
img = detector.findHands(img)
lmList = detector.findPosition(img, draw=False)
pointList = [4, 8, 12, 16, 20]
if len(lmList) != 0:
    countList = []
    if lmList[4][1] > lmList[3][1]:
        countList.append(1)
    else:
        countList.append(0)
    for i in range(1, 5):
        if lmList[pointList[i]][2] < lmList[pointList[i] - 2][2]:
            countList.append(1)
        else:
            countList.append(0)
    count = countList.count(1)
    HandImage = cv2.imread(f'FingerImg/{count}.jpg')
    HandImage = cv2.resize(HandImage, (150, 200))
    h, w, c = HandImage.shape
    img[0:h, 0:w] = HandImage
    cv2.putText(img, f'{int(count)}', (15, 400), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 255), 10)

# 用来追踪发现并且追踪手部
def findHands(self, img, draw=True):  # 对传入的图像, 是否draw
        self.results = self.hands.process(img) # 对每帧图像进行加工
        if self.results.multi_hand_landmarks:  # 检测到手, 并且返回标号
            for oneHand in self.results.multi_hand_landmarks: # 遍历所有手(maxHand)
                if draw: # 是否标记出
                    self.mpDraw.draw_landmarks(img, oneHand, self.mpHands.HAND_CONNECTIONS)
        return img  # 返回加工好的图像

def getMarkList(result_):
    mark_list = []  # 初始化空列表
    if result_.multi_hand_landmarks: # 如果有标号（检测到手）
        oneHand = result_.multi_hand_landmarks[0]  # 只检测一个手
        for num, local in enumerate(oneHand.landmark):  # 遍历枚举
            h, w, c = img.shape # 获取画幅
            local_x, local_y = int(local.x * w), int(local.y * h) # 比例放大, 得到位置
            mark_list.append([num, local_x, local_y]) # 添加到mark_List
    return mark_list


def volumeControl(img, markList=None):
        if len(markList) != 0:  # 如果检测出点了
            thumb_x, thumb_y = markList[4][1], markList[4][2]
            index_x, index_y = markList[8][1], markList[8][2]
            little_x, little_y = markList[20][1], markList[20][2]
            cx, cy = (thumb_x + index_x) // 2, (thumb_y + index_y) // 2  # 找到拇指和食指的中心

        # 高亮我们想要检测的标号
        cv2.circle(img, (thumb_x, thumb_y), 10, (122, 255, 0), cv2.FILLED)
        cv2.circle(img, (index_x, index_y), 10, (122, 255, 0), cv2.FILLED)
        cv2.circle(img, (little_x, little_y), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 6, (122, 255, 0), cv2.FILLED)

        # 然后我们来在我们想标记的中间画根线
        cv2.line(img, (thumb_x, thumb_y), (little_x, little_y), (0, 255, 255), 2)
        cv2.line(img, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 255), 3)  # 参数分别是: 要显示到的图像, 坐标1, 坐标2, BGR, 厚度

        # 那么我们如何获取长度呢, 很简单嘛, 空间中的欧几里得范数:sqrt(x*x+y*y), math.hypot()就可以直接计算出
        thumb_index_distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
        little_thumb_distance = math.hypot(little_x - thumb_x, little_y - thumb_y)
        # print(thumb_index_distance)  # 打印长度, 看两根手指最大和最小的范围

        # 接下来我们就要改变系统音量了: pycaw在github中可以找到
        # 手指的长度范围: Hand range: 20~200
        # 声音的范围: Volume Range: -65~0 ( 0为最大音量)
        # 我们需要一个映射, 这里就用到了numpy.interp()
        vol = np.interp(thumb_index_distance, [20, 160], [minVol, maxVol])  # 音量的转换
        volBar = np.interp(thumb_index_distance, [20, 160], [400, 150])  # 音量条的转换
        volPer = np.interp(thumb_index_distance, [20, 160], [0, 100])  # 转换百分比

        # print(int(thumb_index_distance), vol)

        # 此时我们就可以控制我们的音量了
        volume.SetMasterVolumeLevel(vol, None)  # 设置主音量

        # 我们最后一件事情能够做的就是显示音量:
        # cv2.putText(img,f"volume: {vol}",(0,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255))

        cv2.rectangle(img, (30, 150), (60, 400), (255, 255, 20), 3)  # 画一个矩形
        cv2.rectangle(img, (30, int(volBar)), (60, 400), (255, 255, 20), cv2.FILLED)  # 填充矩形

        cv2.putText(img, f"{str(int(volPer))}%", (20, 430), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                    (255, 255, 20), 2)  # BGR颜色, 线的宽度

        # 根据你的检测精度和距离, 合适的设定你的阈值
        if thumb_index_distance <= 25:  # 当长度<=25, 我认为食指和拇指一块了
            cv2.circle(img, (cx, cy), 10, (0, 50, 255), cv2.FILLED)  # 当检测到合在一起了, 就改变颜色
            pyautogui.hotkey('ctrl', 'alt', 'right')  # 网易云热键热键：切歌
            # time.sleep(1) # 等待, 不要重复切换热键
            cv2.waitKey(200)
        # 暂停
        if little_thumb_distance <= 25:  # 过小时， 就在暂停图像，等待恢复
            # cv2.waitKey(0)
            time.sleep(2)


def dispFPS(img):
    global cTime, pTime
    # 显示FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {str(int(fps))}", (0, 30), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                (10, 255, 0), 2)  # BGR颜色, 线的宽度




















