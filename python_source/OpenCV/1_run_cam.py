import numpy as np
import cv2

print(cv2.__version__)
#cv2.VideoCapture(index) 비디오 출력 클래스, index는 카메라의 장치번호. 기본적으로 노트북 카메라의 장치번호는 0
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)      #capture.set(propid, value) 카메라의 속성 설정 메서드.
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     #propid는 변경하려는 카메라 설정 value는 카메라 설정의 속성 값
                                                #반복문(while)을 활용하여 카메라에서 프레임을 지속적으로 받아온다.
while cv2.waitKey(33) < 0:                      #cv2.waitkey(delay) 는 키입력이 있을 때까지 프로그램을 지연
                                                #delay 는 지연시간이다. delay 가 0일 경우 지속적으로 키입력을 검사하여 프레임이 넘어가지 않는다
    ret, frame = capture.read()                 #ret은 카메라 상태에 따라 True,False를 반환하며, frame엔 현재 시점의 프레임이 저장된다. cv2.capture.read() 는 프레임 읽기 메서드이다.
    cv2.imshow("VideoFrame", frame)             #cv2.imshow(winname, mat) 로 윈도우 창에 이미지를 출력한다
#비디오 프레임 이름을 갖는 윈도우 창에 프레임이 표시된다  #winname은 윈도우 창의 제목, mat 은 할당할 이미지를 의미한다.


capture.release()       # capture.relase() 로 카메라 장치에서 받아온 메모리를 해제한다.
cv2.destroyAllWindows() # cv.destroyALLWindows() 모든 윈도우 창을 닫는다
