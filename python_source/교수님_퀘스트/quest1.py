import os
import soundfile as sf
import numpy as np


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

def count_runtime(DIR_PATH):
    count = 0
    for file in os.listdir(DIR_PATH):
        wav_file = os.path.join(DIR_PATH, file)
        src_wav, sr_wav = audioread(wav_file)
        src_length = len(src_wav)                           # 오디오 파일의 길이
        runtime = round(src_length / sr_wav)
        count += runtime
    print("runtime : {}s".format(count))
    return 0

print(count_runtime("C:/Users/User/OneDrive - ""한국폴리텍대학/Shared Documents/AIFLEX/AIFLEX/SOUNDCODE/soundcode_segment"))

print(audioread("C:/Users/User/OneDrive - ""한국폴리텍대학/Shared Documents/AIFLEX/AIFLEX/SOUNDCODE/soundcode_segment/sc_202_CA.wav"))
data, sr = audioread("C:/Users/User/OneDrive - ""한국폴리텍대학/Shared Documents/AIFLEX/AIFLEX/SOUNDCODE/soundcode_segment/sc_202_CA.wav")

num = np.array(data)
print(num)
print(np.shape(num))
