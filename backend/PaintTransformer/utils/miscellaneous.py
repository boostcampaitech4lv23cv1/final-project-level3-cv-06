import os

import numpy as np
import torch
from PIL import Image


def set_image(img, img_type="RGB", l=None):
    img = img.convert(img_type)
    if l is not None:
        original_w, original_h = img.size
        if original_w > original_h:
            img = img.resize(
                (l, int(l / original_w * original_h)), resample=Image.NEAREST
            )
        else:
            img = img.resize(
                (int(l / original_h * original_w), l), resample=Image.NEAREST
            )
    img = np.array(img)
    if img.ndim == 2:
        img = np.expand_dims(img, axis=-1)
    img = img.transpose((2, 0, 1))
    img = torch.from_numpy(img).unsqueeze(0).float() / 255.0
    return img


def read_img_file(img_path, img_type="RGB", h=None, w=None):
    img = Image.open(img_path).convert(img_type)
    if h is not None and w is not None:
        img = img.resize((w, h), resample=Image.NEAREST)
    img = np.array(img)
    if img.ndim == 2:
        img = np.expand_dims(img, axis=-1)
    img = img.transpose((2, 0, 1))
    img = torch.from_numpy(img).unsqueeze(0).float() / 255.0
    return img


def tensor_to_pil_image(image_tensor):
    pil_image = Image.fromarray(
        (image_tensor.data.cpu().numpy().transpose((1, 2, 0)) * 255).astype(np.uint8)
    )
    return pil_image
