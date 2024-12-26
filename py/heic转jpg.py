import os
import pyheif
from PIL import Image

file_path = "./input/"      # 输入的heic格式图片的文件夹
target_path = "./output/"    # 输出的jpg格式的图片的文件夹
form = "jpeg"       # 设置输出图片格式，需要转换成png时，引号内换成png即可
resize_width = 1200  # 设置目标宽度
resize_height = 900  # 设置目标高度

# 确保输出文件夹存在
if not os.path.exists(target_path):
    os.makedirs(target_path)

files = os.listdir(file_path)    # 返回目录下的所有文件和目录名
file_num = len(files)      # 返回文件的数目
filename = 1    # 设置初始文件名

for file in files:     # 遍历文件列表
    if file.lower().endswith(".heic"):  # 确保处理的是HEIC文件
        img = pyheif.read(file_path + file)  # 读取HEIC图片文件
        img = Image.frombytes(mode=img.mode, size=img.size, data=img.data)  # 读取图片参数
        # 调整图片大小
        img = img.resize((resize_width, resize_height), Image.ANTIALIAS)
        # 保存图片为JPEG
        img.save(target_path + f"{filename}.{form}", format=form)
        filename += 1

print(f"共转换了{file_num}张照片。")