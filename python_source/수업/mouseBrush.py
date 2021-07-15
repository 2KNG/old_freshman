import numpy as np
import cv2
from random import shuffle
import math

mode, drawing = True, False  # mode: 원인지 직사각형인지 결정하는 플레그, drawing: 누르고 있으면 그려지고 떼면 안그려짐
ix,iy = -1,-1  # 마우스 왼쪽 버튼을 누른 지점으로 활용되는 변수
b = [i for i in range(256)]  # bgr값을 위해 0~255까지의 리스트를 만듦 이곳의 0번 인덱스의 값을 사용할 예정
g = [i for i in range(256)]  # bgr값을 위해 0~255까지의 리스트를 만듦 이곳의 0번 인덱스의 값을 사용할 예정
r = [i for i in range(256)]  # bgr값을 위해 0~255까지의 리스트를 만듦 이곳의 0번 인덱스의 값을 사용할 예정

def onMouse(event, x, y,flags, param):  # 마우스 이벤트, 마우스 이벤트가 일어나는 좌표, img가 전달됨
    global ix, iy, drawing, mode, b, g, r  # 전역에 있는 변수들을 가져옴

    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 클릭시 실행
        drawing = True
        ix,iy = x,y
        shuffle(b), shuffle(g), shuffle(r)

    elif event == cv2.EVENT_MOUSEMOVE: # 마우스가 움직일 때 발생
        if drawing:
            if mode:
                cv2.rectangle(param, (ix,iy),(x,y),(b[0],g[0],r[0]),-1)
            else:
                r=(ix-x)**2 + (iy-y)**2
                r = int(math.sqrt(r))
                cv2.circle(param, (ix, iy), r, (b[0],g[0],r[0]),-1)


    elif event == cv2.EVENT_LBUTTONUP:  # 왼쪽 마우스가 떨어지는 경우
        drawing = False
        if mode:
            cv2.rectangle(param, (ix, iy), (x, y), (b[0], g[0], r[0]), -1)
            # 이미지 파일, 시작점의 좌표, 끝나는 점의 좌표, 색상, 선 두깨
        else:
            r = (ix - x) ** 2 + (iy - y) ** 2
            r = int(math.sqrt(r))
            cv2.circle(param, (ix, iy),r, (b[0], g[0], r[0]), -1)

def mouseBrush():
    global mode
    img = np.zeros((512,512,3),np.uint8)
    cv2.namedWindow("paint")
    cv2.setMouseCallback("paint", onMouse, param=img)
    # 마우스 이벤트 처리를 수행할 창 이름, 마우스 이벤트 처리를 위한 콜백 함수 이름, 콜백 함수에 전달할 데이터

    while True:
        cv2.imshow("paint",img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27 :
            break
        elif k == ord('m'):
            mode = not mode

    cv2.destroyAllWindows()

mouseBrush()