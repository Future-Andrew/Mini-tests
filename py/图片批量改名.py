import pandas as pd
import os

def rename_photos_based_on_excel(excel_path, photo_folder_path):
    # 读取Excel文件
    df = pd.read_excel(excel_path)
    print(df)
    
    # 检查DataFrame是否至少有两列
    if df.shape[1] < 2:
        print("Excel文件中没有足够的列。")
        return
    
    # 创建一个字典，将中文名映射到号码
    name_to_number = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
    
    # 遍历照片文件夹
    for filename in os.listdir(photo_folder_path):
        # 只处理图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 获取不带扩展名的文件名
            name = os.path.splitext(filename)[0]
            
            # 检查名字是否在字典中
            if name in name_to_number:
                # 获取对应的号码
                number = name_to_number[name]
                
                # 构建新的文件名
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
