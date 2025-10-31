# Tensor 基础

Tensor 是 PyTorch 的核心数据结构，类似于 NumPy 的 ndarray，但支持 GPU 加速和自动求导。

## 示例代码
```python
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(x * 2)
```
