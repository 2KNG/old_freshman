import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init
# torchvisioin 은 유명한 영상처리용 데이터셋, 모델, 이미지 변환기가 들어있는 패키지
import torchvision.datasets as dset         # 데이터를 읽어오는 역할
import torchvision.transforms as transforms # 불러온 이미지를 필요에 따라 변환해주는 역할
from torch.utils.data import DataLoader     # 데이터를 원하는 batch size 대로 묶어서 전달, 규칙에 따라 정렬 또는 섞기
from torch.autograd import Variable, Function
# torchvision 은 유명한 영상처리용 데이터셋, 모델, 이미지 변환기가 들어있는 패키지로서,
# 여기서 dataset

# 랜덤값 고정용
# # for reproducibility
# random.seed(777)
# torch.manual_seed(777)
# if device == 'cuda':
#     torch.cuda.manual_seed_all(777)

batch_size = 256            # 배치사이즈는 0~255 로 2개가 한세트
learning_rate = 0.0002      # 학습률은 0.0002
num_epoch = 10              # 학습횟수는 10회

# dset(데이터경로, True(학습데이터) or False(테스트 데이터), ToTensor(이미지 데이터를 파이토치 텐서로 변환),
# None라벨에 대한 변환 하지 않음, True 없으면 다운)
mnist_train = dset.MNIST("./", train=True, transform=transforms.ToTensor(),
                         target_transform=None, download=True)
mnist_test = dset.MNIST("./", train=False, transform=transforms.ToTensor(),
                        target_transform=None, download=True)

# 위 데이터가 정리되면
# torch.utils.data.DataLoader(데이터, 묶을 batch_size,
# shuffle = True 섞음, 묶을 때 프로세서 2개 사용, 남는건 버린다)
train_loader = torch.utils.data.DataLoader(mnist_train, batch_size=batch_size,
                                           shuffle=True, num_workers=2, drop_last=True)
test_loader = torch.utils.data.DataLoader(mnist_test, batch_size=batch_size,
                                          shuffle=False, num_workers=2, drop_last=True)


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()         # CNN의 부모 클래스인 nn.Module 을 초기화
        self.layer = nn.Sequential(         # 이미지의 특징을 찾는 단계
            # torch.nn.Conv2d(in_channels, out_channels, kernel_size,
            # stride=1, padding=0, dilation=1, groups=1, bias=True,
            # padding_mode='zeros', device=None, dtype=None)
            # in_channels = 채널의 수 (컬러는 RGB 3층, MNIST는 1층)
            nn.Conv2d(1, 16, 5),    # 출력(피처맵의 두께, 필터의 개수)는 16개로 지정, 필터의 크기는 5로 설정 > 버림 함수에 피처맵 크기는 24
            nn.ReLU(),              # 활성화 함수 렐루에 대입
            nn.Conv2d(16, 32, 5),   # 출력(피처맵의 두께, 필터의 개수)는 32개로 지정, 필터의 크기는 5로 설정 > 버림 함수에 피처맵 크기는 20
            nn.ReLU(),              # 활성화 함수 렐루에 대입
            nn.MaxPool2d(2, 2),     # 맥스풀링(풀링영역, 스트라이드 보폭) > 32, 10, 10
            nn.Conv2d(32, 64, 5),   # 출력(피처맵의 두께, 필터의 개수)는 64개로 지정, 필터의 크기는 5로 설정 > 버림 함수에 피처맵 크기는 6
            nn.ReLU(),              # 활성화 함수 렐루에 대입
            nn.MaxPool2d(2, 2)      # 맥스풀링(풀링영역, 스트라이드 보폭) > 64, 3, 3
        )
        self.fc_layer = nn.Sequential(      # 분류 단계
            nn.Linear(64*3*3, 100),         # 64, 3, 3 의 형태를 완전 연결 계층으로 만들고 100개로 나열
            nn.ReLU(),
            nn.Linear(100, 10)              # 10개의 카테고리로 뉴런의 수를 줄임
        )

    def forward(self, x):
        out = self.layer(x)
        out = out.view(batch_size, -1)      # 64, 3, 3 형태의 텐서를 view 함수를 통해 바꿔줌( -1 은 알아서 계산하라는 의미
        out = self.fc_layer(out)
        return out



USE_CUDA = torch.cuda.is_available() # GPU를 사용가능하면 True, 아니라면 False를 리턴
print(USE_CUDA)
device = torch.device("cuda" if USE_CUDA else "cpu") # GPU 사용 가능하면 사용하고 아니면 CPU 사용
print("다음 기기로 학습합니다:", device)

# model = CNN().to(device)
model = CNN().cuda()
loss_func = nn.CrossEntropyLoss()   # 손실함수는 크로스엔트로피
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

loss_arr = []
for i in range(num_epoch) :
    for j, [image, label] in enumerate(train_loader):
        x = image.to(device)
        y_= label.to(device)

        optimizer.zero_grad()
        output = model.forward(x)
        loss = loss_func(output, y_)
        loss.backward()
        optimizer.step()

        if j % 1000 == 0:
            print(loss)
            loss_arr.append(loss.cpu().detach().numpy())

# 학습된 모델을 테스트 데이터에 대해 검증해보는 부분

correct = 0
total = 0

with torch.no_grad() :
    for image, label in test_loader:
        x = image.to(device)
        y_= label.to(device)

        output = model.forward(x)
        _,output_index = torch.max(output, 1)

        total += label.size(0)
        correct += (output_index == y_).sum().float()

    print("테스트 데이터 정확도: {}".format(100*correct/total))
