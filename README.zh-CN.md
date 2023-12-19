# imagecorruptions

![image corruptions](https://raw.githubusercontent.com/bethgelab/imagecorruptions/master/assets/corruptions_sev_3.png?token=ACY4L7YQWNOLTMRRO53U6FS5G3UF6)

**[中文](./README.zh-CN.md)** | **[English](./README.md)**

这个存储库是从 [CrazyVertigo/imagecorruptions](https://github.com/CrazyVertigo/imagecorruptions) 派生出来的，目前由本人 [Allenpandas](https://github.com/Allenpandas) 维护，本代码在原始存储库的代码的基础上进行了优化和调整。如果您有任何疑问，欢迎随时提交 [pull request](https://github.com/Allenpandas/imagecorruptions/pulls) 🤝，或 [联系我 ](https://github.com/users/follow?target=Allenpandas)📮。这个仓库代码提供了一组可以应用于图像的损坏，以便对神经网络的鲁棒性进行基准测试。这些破坏不是用来增强训练数据的，而是用来测试网络对看不见的扰动的抵抗能力。欲了解更多信息，请参阅 Hendrycks 和 Dietterich 关于 image corruption的论文：[Benchmarking Neural Network Robustness to Common Corruptions and Surface Variations](https://arxiv.org/abs/1807.01697)。

**注意：** 这个仓库来源于 [CrazyVertigo/imagecorruptions](https://github.com/CrazyVertigo/imagecorruptions) , 且仓库 [CrazyVertigo/imagecorruptions](https://github.com/CrazyVertigo/imagecorruptions)  来源于 [bethgelab/imagecorruptions](https://github.com/bethgelab/imagecorruptions).

## Installation and Usage
通过pip安装所需要的依赖包： `pip3 install imagecorruptions`.

下面给出了如何使用的示例，您也可以在根目录下的`examples.py`文件中找到相应的代码。

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
**注意：** 您需要将 `input_folder` 设置为原始图像的存放目录，将 `output_folder` 设置为输出图像的存放目录。

目前支持的corruption方法有以下几类：gaussian_noise（高斯噪声）、shot_noise（抖动噪声）、impulse_noise（脉冲噪声）、defocus_blur（虚焦模糊）、motion_blur（运动模糊）、zoom_blur（缩放模糊）、snow（雪花）、fog（雾）、contrast（对比度）、elastic_transform（弹性变换）、pixelate（像素化）、jpeg_compression（JPEG压缩）、speckle_noise（斑点噪声）、spatter（飞溅）

## Citation

如果您使用 imagecorruptions 包，请考虑引用:
```
@article{michaelis2019dragon,
  title={Benchmarking Robustness in Object Detection: Autonomous Driving when Winter is Coming},
  author={Michaelis, Claudio and Mitzkus, Benjamin and Geirhos, Robert and Rusak, Evgenia and Bringmann, Oliver and Ecker, Alexander S. and Bethge, Matthias and Brendel, Wieland},
  journal={arXiv preprint arXiv:1907.07484},
  year={2019}
}
```
