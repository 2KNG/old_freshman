import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
# torchvisioin 은 유명한 영상처리용 데이터셋, 모델, 이미지 변환기가 들어있는 패키지
import torchvision.datasets as dset         # 데이터를 읽어오는 역할
import torchvision.transforms as transforms # 불러온 이미지를 필요에 따라 변환해주는 역할
from torch.utils.data import DataLoader     # 데이터를 원하는 batch size 대로 묶어서 전달, 규칙에 따라 정렬 또는 섞기


def conv_2_block(in_dim, out_dim):
    model = nn.Sequential(
        nn.Conv2d(in_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2, 2)
    )
    return model


def conv_3_block(in_dim, out_dim):
    model = nn.Sequential(
        nn.Conv2d(in_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2, 2)
    )
    return model


class VGG(nn.Module):
    def __init__(self, base_dim, num_classes = 2):
        super(VGG, self).__init__()
        self.feature = nn.Sequential(
            conv_2_block(3, base_dim),
            conv_2_block(base_dim, 2*base_dim),
            conv_3_block(2*base_dim, 4*base_dim),
            conv_3_block(4*base_dim, 8*base_dim),
            conv_3_block(8*base_dim, 8*base_dim),
        )
        self.fc_layer = nn.Sequential(
            nn.Linear(8*base_dim * 7 * 7, 100),
            nn.ReLU(True),
            nn.Linear(100,20),
            nn.ReLU(True),
            nn.Linear(20, num_classes),
        )