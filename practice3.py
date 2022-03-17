import torch


t = torch.FloatTensor([1, 2])
print(t.mean())

t = torch.LongTensor([1, 2])
try:
    print(t.mean())
except Exception as exc:
    print(exc)

# dimension은 배열과 똑같이 생각, 0차원이 가로로 쭉, 1차원이 세로로 쭉, 2차원이 Z축으로 쭉
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t.sum(dim=1))
print(t.max(dim=1))

# argmax index 반환,
print(t.max(dim=1)[1])