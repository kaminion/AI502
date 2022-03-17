import torch

t = torch.FloatTensor([[[0, 1, 2],
[3, 4, 5]],
[[6, 7, 8],
[9, 10, 11]
]])

print(t.shape)

# reshape


# squeeze - 짜내다
# we can delete one-dimension
# does not contain any meaning

ft = torch.FloatTensor([[0], [1], [2]])
print(ft)
print(ft.shape)