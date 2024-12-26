import pandas as pd
import os

def rename_photos_based_on_excel(excel_path, photo_folder_path):
    # 读取Excel文件
    df = pd.read_excel(excel_path)
    
    # 检查是否至少有两列
    if len(df.columns) < 2:
        print("Excel文件中没有足够的列。")
        return

    # 创建一个编号列表，即Excel中的B列数据
    numbers = df.iloc[:, 1].tolist()

    # 获取照片文件夹中的所有文件，并按文件名排序
    photo_files = sorted(os.listdir(photo_folder_path),
                         key=lambda x: os.path.splitext(x)[0])

    # 遍历照片文件夹中的文件
    for i, filename in enumerate(photo_files):
        # 只处理图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 获取对应的号码
            if i < len(numbers):
                number = numbers[i]
            else:
                print(f"No matching number in Excel for {filename}. Skipping.")
                continue

            # 提取图片文件的时间戳部分，假设时间戳格式为IMG_YYYYMMDD_HHMMSS
            # 并假设文件名格式为IMG_YYYYMMDD_HHMMSSXXXX
            timestamp = os.path.splitext(filename)[0].split('_')[-1]
            # 构建新的文件名，保持原文件名的时间戳部分，替换为Excel中的号码
            new_filename = f"{number}{os.path.splitext(filename)[1]}"
            
            # 构建完整的文件路径
            old_file_path = os.path.join(photo_folder_path, filename)
            new_file_path = os.path.join(photo_folder_path, new_filename)
            
            # 重命名文件
            if not os.path.exists(new_file_path):  # 检查新文件名是否已存在
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"File '{new_filename}' already exists. Skipping '{filename}'.")

# 使用示例
excel_path = 'C:/Users/王国聪/Desktop/1.xlsx'  # Excel文件路径
photo_folder_path = 'C:/Users/王国聪/Desktop/4'  # 照片所在的文件夹路径
rename_photos_based_on_excel(excel_path, photo_folder_path)
