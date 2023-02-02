import sys

from PaintTransformer.inference import *
from PIL import Image

import os

import numpy as np

resize_l = 1024
K = 5
stroke_num = 16
patch_size = 32

model, meta_brushes, device = init(stroke_num, model_path="model_16.pth")

image = Image.open("dataset/original/entertainer/iu/iu_01.jpg")
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

num_frame = len(output)


def make_duration_list(num_frame: int=200, total_time: int=10, mode: str="CONSTANT"):

    min_time_step = 12
    if mode=="CONSTANT":
        duration_list = [round(total_time*1000/num_frame)]*num_frame
        return duration_list
    if mode=="LINEAR":
        duration_list = np.arange(min_time_step, min_time_step + num_frame)
        duration_list = np.asarray(duration_list/sum(duration_list)*total_time*1000, dtype=int)
        duration_list[duration_list<min_time_step] = min_time_step
        return list(duration_list)



fn = "output_iu_dummy_16_linear"

# constant
# timestep_list = [10]*200

timestep_list = make_duration_list(num_frame=num_frame, mode="LINEAR")

output[0].save(
        fn+".webp",
        format="WEBP",
        save_all=True,
        append_images=output[1:],
        optimize=True,
        duration=timestep_list,
        loop=1,
    )
output[-1].save(fn+"_final.webp")
