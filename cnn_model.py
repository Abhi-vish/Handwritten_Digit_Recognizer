import torch
from torch import nn

class MNISTDigitRecognitionModel(nn.Module):
  def __init__(self,
               input_shape:int,
               hidden_units:int,
               output_shape:int):
    super().__init__()
    self.conv2d_block_1 = nn.Sequential(
       nn.Conv2d(in_channels=input_shape,
                 out_channels=hidden_units,
                 kernel_size=3,
                 stride=1,
                 padding=1),
       nn.ReLU(),
       nn.Conv2d(in_channels=hidden_units,
                 out_channels=hidden_units,
                 kernel_size=3,
                 stride=1,
                 padding=1),
       nn.ReLU(),
       nn.MaxPool2d(kernel_size=2,
                    stride=2) 
    )
    self.conv2d_block_2 = nn.Sequential(
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  stride=1,
                  padding=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=hidden_units,
                 out_channels=hidden_units,
                 kernel_size=3,
                 stride=1,
                 padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2)
    )
    self.classifier = nn.Sequential(
        nn.Flatten(),
        nn.Linear(in_features=hidden_units * 7*7,
                  out_features=output_shape)
    )
  
  def forward(self, x):
    x = self.conv2d_block_1(x)
    # print(x.shape)
    x = self.conv2d_block_2(x)
    # print(x.shape)
    x = self.classifier(x)
    return x