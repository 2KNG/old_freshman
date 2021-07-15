"""
Description: 특정폴더의 wav 데이터를 일정길이로 분절하여 저장
Date:  2021.7.12
Developer: R.H-D Kim
"""

import argparse             # 파이썬 인자값 추가하기, 파일형식 변경하는거같음
import os                   # 운영체제와 상호작용을 돕는 다양한 기능 제공
import soundfile as sf
# 아나콘다 환경 인스톨 방법 conda install -c conda-forge pysoundfile

# 오디오 읽기 함수(경로, norm=False?, 시작과 끝은 디폴트로 0, None 지정
def audioread(path, norm=False, start=0, stop=None):
    '''Function to read audio'''

    # os.path.abspath(path) 특정 경로에 대해 절대 경로 얻기
    path = os.path.abspath(path)
    # os.path.exists(path) 파일 혹은 디렉토리 경로가 존재하는지 체크하기
    if not os.path.exists(path):
        # 없으면 (path) 없다고 ValueError 예외처리
        raise ValueError("[{}] does not exist!".format(path))

    try:
        audio, sample_rate = sf.read(path, start=start, stop=stop)      # 넘파이 형식으로 오디오를 읽음
# https://github.com/bastibe/python-soundfile/blob/master/soundfile.py
    # 파일 지원안하면 RuntimeError 예외처리
    except RuntimeError:  # fix for sph pcm-embedded shortened v2
        print('WARNING: Audio type not supported')

    return audio, sample_rate

# 오디오 쓰기 함수
def audiowrite(destpath, audio, sample_rate=44100):
    '''Function to write audio'''

    # 파일경로를 절대경로로 변경
    destpath = os.path.abspath(destpath)
    # 파일의 폴더 경로를 반환
    destdir = os.path.dirname(destpath)

# os.mkdir() 폴더 하나만 생성, os.makedirs() './a/b/c' > a 폴더안에 b폴더안에
    if not os.path.exists(destdir):     # 경로가 존재하지 않으면
        os.makedirs(destdir)            # 경로를 생성한다

    sf.write(destpath, audio, sample_rate)      # 읽어드린 넘파이로 다시 사운드파일 형대로 저장

    return 0    # 0을 반환하면서 끝남


def util_seg_wav( PATH_SRC, SEG_WAV ):      # 소스위치, 분절될 파일(시간인가?)

# __init__에 해당
    total_count = 0# 총 분절 개수
    total_time = 0# 전체 분절된 시간
    # 지정된 디렉토리에 있는 모든 파일 리스트를 작성
    for IDs in os.listdir(PATH_SRC):        # 소스 위치에 있는 파일을 IDs로 받고 반복 (~~L 또는 R)
        index = 0# 파일 분절 위치
        f_count = 0# 총 분절 개수

        # 작성된 파일 리스트의 전체 경로를 재구성
        WavPath = os.path.join(PATH_SRC,IDs)        # PATH_SRC/IDs 형태의 경로 통합
        # wav 파일 읽기
        src_wav, sr_wav = audioread(WavPath)        # 아까 만들어준 오디오 읽기 함수로 ~IDs 파일을 읽고 src_wav에 오디오 파일을, sr_wav에 샘플링 레이트 저장
        # 지정된 길이(SEG_WAV)만큼 잘랐을 때 분할파일 개수 계산
        src_length = len(src_wav)                           # 오디오 파일의 길이
        seg_length = round(SEG_WAV*sr_wav)                  # 분절길이 = 반올림(분절시간*읽은 샘플링레이트)
        num_segment = round(src_length/(SEG_WAV*sr_wav))    # 갯수는 총길이(분절시간 / 샘플링레이트)
        # 파일이름과 확장자를 분리
        fname = os.path.splitext(IDs)           # split(filename) : 폴더와 파일 분리(리스트) splitext(filename) : 확장자만 따로 분류
        # 분할파일 개수 만큼 잘라서 wav 파일 저장
        for idx in range(num_segment):          # 분절 갯수만큼 반복
            index += 1
            total_time += seg_length
            dirname = "seg_" + fname[0]         # 확장자와 분리된 파일이름을 dirname 에 저장
            DIR_OUT = os.path.join(PATH_SRC, dirname)   # 경로와 파일이름 합쳐주고
            print(DIR_OUT)
            filename = fname[0] + "_{:03d}.wav".format(f_count) # 세부파일이름은 0~255(시간별 분절이니까 bit)
            PATH_OUT = os.path.join(DIR_OUT, filename)          # 다시 합쳐주고
            audiowrite(PATH_OUT, src_wav[idx*seg_length:(idx+1)*seg_length]) # 아까 맹들어준 오디오 파일만들기 함수로 오디오 파일 생성
            # 분절 시간 간격으로 인덱싱
            f_count += 1

        total_count += f_count

    return total_count, round(total_time/sr_wav)
# 파일 갯수랑 총걸린시간/샘플링레이트 반올림해서 반환 시간과 샘플링 레이트 관계를 알아야댐


# https://greeksharifa.github.io/references/2019/02/12/argparse-usage/
parser = argparse.ArgumentParser(description='Segmentation of wav files')
parser.add_argument('--path_src', '-ps', default='sample',
                    help='Prefix Directory Name to input source')
parser.add_argument('--seg_wav', '-sw', default=2.0, type=float,
                    help='Prefix the duration of wav segmentation')
args = parser.parse_args()

numfile, totaltime = util_seg_wav( args.path_src, args.seg_wav )
print("[Notice] Number of splited wav files:", numfile,"& Total time:",totaltime,"sec")


'''
DB구축 작업 외 다음 내용도 고민해 보시기 바랍니다.

1. 각 주파수 위치 별로 감도가 줄어드는 비율 분석 (상위 주파수의 감도가 많이 떨어지면 사운드 코드 위치를 다시 조정할 필요가 있습니다)

2. 스테레오를 L과 R로 분리하여 전체 길이를 맞추고 2초 간격으로 자동 분절하는 파이썬 코드 작성 (분절된 파일 네이밍 규칙 정의)

3. 분절된 wav 파일을 각 코드별로 csv 파일로 저장하는 파이썬 코드 작성 (상위 코드, 하위 코드, 순서 별로 파일 네이밍 규칙 정의)

4. 전체 wav 파일을 입력하면 자동으로 사운드 코드를 검출하고 인식결과 출력 (결과는 txt 또는 csv 형태로 list 출력)
'''