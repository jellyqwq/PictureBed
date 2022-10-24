import torch
import torch.nn as nn
import torch.nn.functional as F

# CIFAR-10: 32x32

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        # Conv2d(in_channels, out_channels, kernel_size)
        # in_channels: 输入图片的通道数, 如RGB为三通道, 所以是3, Gray是灰度图, 单通道, 为1
        # out_channels: 卷积核个数=输出特征数量
        # kernel_size: 卷积核大小, 这里5表示5x5的正方形卷积核
        self.pool = nn.MaxPool2d(2, 2)
        # 最大池化 MaxPool2d(kernels, strides)
        # kernels: 核大小, 这里2表示2x2, 取出2x2方位内的最大值
        # strides: 核的步长
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 这一步将会提取出16种特征图
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        # 线性变换, 特征维数*图片高*图片宽(16 * 5 * 5)->120
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        # 数据集一共十个类别, 最后收束到10上

    def forward(self, x):
        # x 是由 (batch_sizes, channels, height, width)四个量组成
        # 其中 batch_sizes不做卷积运算
        x = self.pool(F.relu(self.conv1(x)))
        # 先调用第一层卷积完成self.conv1(x)
        # 再使用激活函数对卷积后的结果进行区间化(sigmoid, relu, ...)
        # 最后池化, 用最大池化的方法进一步提取特征
        x = self.pool(F.relu(self.conv2(x)))
        # 重复上述步骤
        # 此时的卷积量为 (batch_sizes, 16, 5, 5)
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        # 维度线性展开, 全连接层
        # 该操作同理
        # >>> m = torch.nn.Flatten()
        # >>> x = m(x)
        # 这两者都是对指定区间的维度联合展开, 在这里就是对[1:-1]部分进行展开, 不包括index-0(batch_sizes)
        # 所以这步完成后x.shape为(batch_sizes, 16*5*5)
        x = F.relu(self.fc1(x))
        # 对线性变换(减少参数)并激活(缩小参数至0~1)
        x = F.relu(self.fc2(x))
        # 同理
        x = self.fc3(x)
        # 将参数线性变换至数据集种类数上(概率)
        return x


net = Net()