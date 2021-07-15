import os
import soundfile as sf
import argparse
import numpy as np
import random


def audioread(path, norm=False, start=0, stop=None):
    '''Function to read audio'''

    path = os.path.abspath(path)
    if not os.path.exists(path):
        raise ValueError("[{}] does not exist!".format(path))

    try:
        audio, sample_rate = sf.read(path, start=start, stop=stop)
# https://github.com/bastibe/python-soundfile/blob/master/soundfile.py
    except RuntimeError:  # fix for sph pcm-embedded shortened v2
        print('WARNING: Audio type not supported')

    return audio, sample_rate

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



def util_random_wav( PATH_SRC, RUN_TIME):

    # __init__에 해당
    total_count = 0
    total_time = 0
    fname_list = []
    wav_list = []
    # wav_list = np.ndarray([])
    shuffle_list = os.listdir(PATH_SRC)
    random.shuffle(shuffle_list)
    print(shuffle_list)


    for IDs in shuffle_list:
        if total_time < RUN_TIME :
            WavPath = os.path.join(PATH_SRC, IDs)
            tag = IDs[3:6]
            fname_list.append(tag)
            print(tag)
            src_wav, sr_wav = audioread(WavPath)
            wav_list = np.r_[wav_list, src_wav]
            src_length = len(src_wav)
            runtime = round(src_length / sr_wav)
            total_time += runtime
            total_count += 1
        else :
            break

    print(fname_list)
    file_name = os.path.join(PATH_SRC, "{}.wav".format(fname_list))
    audiowrite(file_name, wav_list)

    return total_count, total_time

util_random_wav("C:/Users/khkim/OneDrive - ""한국폴리텍대학/Shared Documents/AIFLEX/AIFLEX/SOUNDCODE/soundcode_segment", 30)

#
# # https://greeksharifa.github.io/references/2019/02/12/argparse-usage/
# parser = argparse.ArgumentParser(description='Segmentation of wav files')
# parser.add_argument('--path_src', '-ps', default='sample',
#                     help='Prefix Directory Name to input source')
# parser.add_argument('--seg_wav', '-sw', default=2.0, type=float,
#                     help='Prefix the duration of wav segmentation')
# args = parser.parse_args()
#
# numfile, totaltime = util_random_wav( args.path_src, args.seg_wav )
# print("[Notice] Number of splited wav files:", numfile,"& Total time:",totaltime,"sec")

