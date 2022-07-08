import cv2
import mediapipe

#################################
# 相机参数
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