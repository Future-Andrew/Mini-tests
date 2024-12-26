from PIL import Image
import os
 
# 设置要修改的图片文件夹路径
folder_path ="C:/Users/王国聪/Desktop/2024-1"
 
# 设置目标图片大小
target_size = (180, 240)
 
# 遍历文件夹中的所有图片文件
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 打开图片文件
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)
 
        # 修改图片大小并保存
        resized_image = image.resize(target_size)
        resized_image.save(image_path)
print("批量操作完成！")

def convert_images_to_8bit_color(folder_path):
    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是图片
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 构建完整的文件路径
            file_path = os.path.join(folder_path, filename)
            
            # 打开图片
            with Image.open(file_path) as img:
                # 如果图像已经是RGB模式，则不需要转换
                if img.mode == 'RGB':
                    # 保存图像，覆盖原文件
                    img.save(file_path, quality=85)  # 指定JPEG格式和质量
                    print(f"Saved {filename} as JPEG with quality 85.")
                else:
                    # 转换为RGB模式
                    color_img = img.convert('RGB')
                    # 保存RGB图像，覆盖原文件
                    color_img.save(file_path, quality=85)  # 指定JPEG格式和质量
                    print(f"Converted {filename} to RGB and saved as JPEG.")

# 使用示例
folder_path = 'C:\\Users\\王国聪\\Desktop\\2024-1'  # 包含图片的文件夹路径
convert_images_to_8bit_color(folder_path)
