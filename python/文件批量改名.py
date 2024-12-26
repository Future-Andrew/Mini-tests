import os
import re

def rename_files_with_chinese_names(folder_path):
    # 定义一个正则表达式，用于匹配文件名中的中文名
    chinese_name_pattern = re.compile(r'[\u4e00-\u9fa5]+')

    # 遍历指定文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # 使用正则表达式查找中文名
            match = chinese_name_pattern.search(filename)
            if match:
                # 如果找到中文名，获取中文名
                chinese_name = match.group()
                # 获取文件的扩展名
                file_extension = os.path.splitext(filename)[1]
                # 构建新的文件名（中文名 + 扩展名）
                new_filename = f"{chinese_name}{file_extension}"
                # 构建完整的文件路径
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)
                # 重命名文件
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")

# 使用示例
folder_path = 'C:/Users/王国聪/Desktop/4'  # 文件夹路径
rename_files_with_chinese_names(folder_path)
