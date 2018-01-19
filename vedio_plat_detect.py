from hyperlpr_py3 import pipline as  pp
import cv2

# cam = cv2.VideoCapture(1)
cam = cv2.VideoCapture("./vedio/IMG_0673.MOV")
frmcnt = 1

timeF = 1  # 视频帧计数间隔频率

while True:
    _, img = cam.read()
    rows, cols, channel = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 270, 1.5)
    img = cv2.warpAffine(img, M, (cols, rows))
    if (frmcnt % timeF == 0):  # 每隔timeF帧进行存储操作
        img, res = pp.SimpleRecognizePlateByE2E(img)
    cv2.imshow('plat_detect', img)
    frmcnt = frmcnt + 1

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
