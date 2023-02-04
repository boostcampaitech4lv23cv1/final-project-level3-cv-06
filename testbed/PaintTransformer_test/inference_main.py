import sys

from PaintTransformer.inference import *
from PIL import Image

import os

import numpy as np

resize_l = 1024
K = 4
stroke_num = 6
patch_size = 32

model, meta_brushes, device = init(stroke_num, model_path="model_06.pth")

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


def make_duration_list(
    num_frame: int = 200, total_time: int = 10, mode: str = "LINEAR"
) -> list:
    """make frame duration list for animation

    Args:
        num_frame (int, optional): number of frames. Defaults to 200.
        total_time (int, optional): total time of animation. Defaults to 10.
        mode (str, optional): mode of duration list. Defaults to "LINEAR".

    Returns:
        list: duration list
    """

    exp_dict = {
        "SQRT": 0.5,
        "LINEAR": 1,
        "SQUARE": 2,
    }
    min_time_step = 12

    if mode == "CONSTANT":
        return [round(total_time * 1000 / num_frame)] * num_frame
    else:
        exp_num = exp_dict[mode]
        duration_list = np.arange(min_time_step, min_time_step + num_frame)
        duration_list = np.power(duration_list, exp_num)
        duration_list = np.asarray(
            duration_list / sum(duration_list) * total_time * 1000, dtype=int
        )
        duration_list[duration_list < min_time_step] = min_time_step
        return list(duration_list)


fn = "output_iu_06_dummy"

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
