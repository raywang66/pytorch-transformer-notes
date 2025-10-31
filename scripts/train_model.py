# train_model.py
import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

if __name__ == "__main__":
    model = SimpleModel()
    x = torch.randn(5, 10)
    output = model(x)
    print("Model output:", output)
