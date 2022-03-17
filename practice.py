import numpy as np
import torch

t = np.array([0., 1.0, 2.0])
print(t)
# 차원
print(t.ndim)
# element 개수
print(t.shape)

print(t[0])
print(t[1])
print(t[-1])

# array data structure
t = np.array([[1. , 2., 3.], [4., 5., 6.]])
print(t.ndim, t.shape)

# torch는 tensor - GPU & CPU
t = torch.FloatTensor([[1., 2., 3., 4., 5., 6.], [1., 2., 3., 4., 5., 6.]])
print(t)
print(t.dim()) #rank
print(t.shape) # shape
# 나머지는 동일, 슬라이싱이라던지..

print(t.size()) # shape

# 전체에서 1열을 선택 (index 관점)
print(t[:, 1])

