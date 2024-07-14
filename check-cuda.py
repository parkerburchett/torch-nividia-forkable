import torch

if torch.cuda.is_available():
    print(f'{torch.cuda.get_device_name(torch.device("cuda"))=}')
else:
    raise ImportError("Can't properly load cuda")
