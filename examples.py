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
    input_folder = "/Users/allenpandas/Desktop/test"  # 原图像目录
    output_folder = "/Users/allenpandas/Desktop/test-ir"  # 输出图像目录
    # 支持的corruption效果
    custom_corruption_list = [
        'gaussian_noise', 'shot_noise', 'impulse_noise', 'defocus_blur',
        'motion_blur', 'zoom_blur', 'snow', 'fog', 'contrast', 'elastic_transform',
        'pixelate', 'jpeg_compression', 'speckle_noise', 'spatter'
    ]
    apply_corruption_to_folder(input_folder, output_folder, custom_corruption_list)
