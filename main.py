import torch

print(torch.__version__)             # see which PyTorch version you have
print(torch.cuda.is_available())     # must be True if GPU works
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
