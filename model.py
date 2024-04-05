import torch.nn as nn
from torchvision import models

class myVGG19(nn.Module):
    def __init__(self):
        super(myVGG19, self).__init__()
        self.vgg19 = models.vgg19(pretrained=False)
        self.vgg19.features[0] = nn.Conv2d(1, 64, kernel_size=3, padding=1)  # 첫 번째 레이어를 1채널 입력에 맞게 수정
        num_ftrs = self.vgg19.classifier[6].in_features
        self.vgg19.classifier[6] = nn.Linear(num_ftrs, 10)  # 마지막 레이어를 10개 클래스에 맞게 조정
    
    def forward(self, x):
        return self.vgg19(x)