from hyperlpr_py3 import pipline as  pp
import cv2

# cam = cv2.VideoCapture(1)
cam = cv2.VideoCapture("./vedio/IMG_0663.MOV")
frmcnt = 1
timeF = 1  # 视频帧计数间隔频率

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('out.mp4',fourcc, 30.0, (1920,1080))

while True:
    _, img = cam.read()
    rows, cols, channel = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 270, 1.5)
    img = cv2.warpAffine(img, M, (cols, rows))
    if (frmcnt % timeF == 0):  # 每隔timeF帧进行存储操作
        img, res = pp.SimpleRecognizePlateByE2E(img)
    out.write(img)
    cv2.imshow('plat_detect', img)
    frmcnt = frmcnt + 1

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
