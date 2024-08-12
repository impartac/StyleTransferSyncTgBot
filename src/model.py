import torch
from torchvision import models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = models.vgg16(weights='DEFAULT').features.to(device).eval()
