import cv2

capture = cv2.VideoCapture("C:/sibal/goose.mp4")
print(capture.isOpened())
# 비디오 출력 클래스(cv2.VideoCapture) 동영상 파일에서 정보를 받아올 수 있다.
# 카메라 출력에서 사용한 클래스와 동일한 클래스를 사용하며, 진행 방식도 동일하나, 여기선 장치번호가 아닌 동영상 파일의 경로를 지정해준다.
while cv2.waitKey(33) < 0 :
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT) :
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # capture.get 은 비디오 속성을 반환해주는 메서드이다.
        # 현재 프레임 수 cv2.CAP_PROP_POS_FRAMES 와 총 프레임 수 cv2.CAP_PROP_FRAME_COUNT 를 비교한다.
        # 현재 프레임과 총 프레임이 같다면, 동영상이 끝난 것이다.
        

        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)
        cv2.waitKey(0)  # 키입력 대기 함수


capture.release()
cv2.destroyAllWindows()


'''
VideoCapture 메서드
        메서드	                       의미
capture.isOpened()	        동영상 파일 열기 성공 여부 확인
capture.open(filename)	        동영상 파일 열기
capture.set(propid, value)	동영상 속성 설정
capture.get(propid)	        동영상 속성 반환
capture.release()	        동영상 파일을 닫고 메모리 해제



VideoCapture 속성
            속성	                의미	                비고
cv2.CAP_PROP_FRAME_WIDTH	프레임의 너비	            -
cv2.CAP_PROP_FRAME_HEIGHT	프레임의 높이	            -
cv2.CAP_PROP_FRAME_COUNT	총 프레임 수	            -
cv2.CAP_PROP_FPS	        프레임 속도	            -
cv2.CAP_PROP_FOURCC     	코덱 코드	            -
cv2.CAP_PROP_BRIGHTNESS         이미지 밝기	        카메라만 해당
cv2.CAP_PROP_CONTRAST	        이미지 대비	        카메라만 해당
cv2.CAP_PROP_SATURATION 	이미지 채도	        카메라만 해당
cv2.CAP_PROP_HUE	        이미지 색상	        카메라만 해당
cv2.CAP_PROP_GAIN	        이미지 게인	        카메라만 해당
cv2.CAP_PROP_EXPOSURE	        이미지 노출	        카메라만 해당
cv2.CAP_PROP_POS_MSEC	        프레임 재생 시간	    ms 반환
cv2.CAP_PROP_POS_FRAMES	        현재 프레임	        프레임의 총 개수 미만
CAP_PROP_POS_AVI_RATIO	        비디오 파일 상대 위치	0 = 시작, 1 = 끝
'''
