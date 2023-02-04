import sys

from PaintTransformer.inference import *
from PIL import Image

import os

resize_l = 1024
K = 5
stroke_num = 8
patch_size = 32

model, meta_brushes, device = init(stroke_num, model_path="model.pth")

image = Image.open("PaintTransformer/dataset/original/animal/cat/cat_1.jpg")
output = inference(
    image=image,
    resize_l=resize_l,  # resize original input to this size. (max(w, h) = resize_l)
    K=K,  # set K
    device=device,
    model=model,
    meta_brushes=meta_brushes,
    stroke_num=stroke_num,
    patch_size=patch_size,
)

output[-1].save("cat_1_result.jpg")
