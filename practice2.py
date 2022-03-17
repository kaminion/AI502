# Broad Casting
# M1 + M2 매우 빠름
import torch
import numpy as np


m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
# 매우 심플하고 빠름
print(m1 + m2, '\n')

# 1 x 2 Vector + 2 x 1 Vector
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([[3], [4]])
print(m1.shape)
print(m1 + m2, '\n')


# Matrix Multiplecation vs Multiplecation 

# 행렬 곱, 잘 알고있는 그 연산
m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])
print(m1.matmul(m2))

# Mutltiplication, 단순하게 현재 shape만 곱함
m1 = torch.FloatTensor([[1, 2], [3, 4]])
m2 = torch.FloatTensor([[1], [2]])

print(m1.mul(m2))