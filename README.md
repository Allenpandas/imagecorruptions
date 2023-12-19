# imagecorruptions

![image corruptions](https://raw.githubusercontent.com/bethgelab/imagecorruptions/master/assets/corruptions_sev_3.png?token=ACY4L7YQWNOLTMRRO53U6FS5G3UF6)

**[中文](./README.zh-CN.md)** | **[English](./README.md)**

This repository was forked from [CrazyVertigo/imagecorruptions](https://github.com/CrazyVertigo/imagecorruptions) and is maintained by [Allenpandas](https://github.com/Allenpandas) who has made optimizations and adjustments based on the original repository's code. If you have any questions, feel free to submit a [pull request](https://github.com/Allenpandas/imagecorruptions/pulls) 🤝, or [contact me](https://github.com/users/follow?target=Allenpandas) 📮. This package provides a set of corruptions that can be applied to images in order to benchmark the robustness of neural networks. These corruptions are not meant to be used as training data augmentation but rather to test the networks against unseen perturbations. For more information have a look at the paper on the original corruption package by Hendrycks and Dietterich: [Benchmarking Neural Network Robustness to Common Corruptions and Surface Variations](https://arxiv.org/abs/1807.01697).

**Notice:** This repository folked from [CrazyVertigo/imagecorruptions](https://github.com/CrazyVertigo/imagecorruptions) , and [CrazyVertigo/imagecorruptions](https://github.com/CrazyVertigo/imagecorruptions)  folked from [bethgelab/imagecorruptions](https://github.com/bethgelab/imagecorruptions).

## Installation and Usage
This package is pip installable via `pip3 install imagecorruptions`.

 An example of how to use the corruption function is given below, and you can also find corresponding code in the `examples.py` file in the root directory.

```python
from PIL import Image
import numpy as np
from imagecorruptions import corrupt
import os
import random


def apply_corruption(input_image_path, output_folder, corruption_list=None):
    # 创建输出目录
    os.makedirs(output_folder, exist_ok=True)
    # 读取图像并将PIL图像转换为NumPy数组
    image = Image.open(input_image_path)
    image_array = np.array(image)
    # 随机选择corruption效果
    corruption_name = random.choice(corruption_list)
    # 执行corruption
    corrupted_image_array = corrupt(image_array, corruption_name=corruption_name, severity=1)
    # 转换处理后的图像数组为 PIL 图像对象
    corrupted_image = Image.fromarray(corrupted_image_array)
    # 拼接输出图像的文件名和路径
    output_image_path = os.path.join(output_folder, os.path.basename(input_image_path))
    # 保存输出图像
    corrupted_image.save(output_image_path)


def apply_corruption_to_folder(input_folder, output_folder, corruption_list=None):
    for filename in os.listdir(input_folder):
        # 获取目录下所有的.jpg和png图像
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_folder, filename)
            # 逐一进行corruption
            apply_corruption(input_image_path, output_folder, corruption_list)


if __name__ == '__main__':
    input_folder = ""  # 原图像目录
    output_folder = ""  # 输出图像目录
    # 支持的corruption效果
    custom_corruption_list = [
        'gaussian_noise', 'shot_noise', 'impulse_noise', 'defocus_blur',
        'motion_blur', 'zoom_blur', 'snow', 'fog', 'contrast', 'elastic_transform',
        'pixelate', 'jpeg_compression', 'speckle_noise', 'spatter'
    ]
    apply_corruption_to_folder(input_folder, output_folder, custom_corruption_list)

```
**Notice:** You can set `input_folder` as the directory for the original images and `output_folder` as the directory for the resulting images.

Now, the currently supported **corruption** methods include the following: gaussian_noise（高斯噪声）、shot_noise（抖动噪声）、impulse_noise（脉冲噪声）、defocus_blur（虚焦模糊）、motion_blur（运动模糊）、zoom_blur（缩放模糊）、snow（雪花）、fog（雾）、contrast（对比度）、elastic_transform（弹性变换）、pixelate（像素化）、jpeg_compression（JPEG压缩）、speckle_noise（斑点噪声）、spatter（飞溅）

## Citation

If you use the imagecorruptions package, please consider citing:
```
@article{michaelis2019dragon,
  title={Benchmarking Robustness in Object Detection: Autonomous Driving when Winter is Coming},
  author={Michaelis, Claudio and Mitzkus, Benjamin and Geirhos, Robert and Rusak, Evgenia and Bringmann, Oliver and Ecker, Alexander S. and Bethge, Matthias and Brendel, Wieland},
  journal={arXiv preprint arXiv:1907.07484},
  year={2019}
}
```
