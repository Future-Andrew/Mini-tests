import os

def rename_files_sequentially(folder_path):
    # 获取文件夹中的所有文件，并按文件名排序
    files = sorted(os.listdir(folder_path), key=lambda x: os.path.splitext(x)[0])

    # 遍历文件夹中的文件
    for index, filename in enumerate(files, start=1):
        # 只处理图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 提取文件的扩展名
            file_extension = os.path.splitext(filename)[1]
            # 构建新的文件名（编号 + 扩展名）
            new_filename = f"{index}{file_extension}"
            
            # 构建完整的文件路径
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # 重命名文件
            if not os.path.exists(new_file_path):  # 检查新文件名是否已存在
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"File '{new_filename}' already exists. Skipping '{filename}'.")

# 使用示例
folder_path = 'C:/Users/王国聪/Desktop/7cs'  # 文件夹路径
rename_files_sequentially(folder_path)
