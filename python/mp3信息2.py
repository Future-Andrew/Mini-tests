import eyed3
import ctypes
import sys

# 确保文件路径正确
audio_file_path = "C:/Users/王国聪/Desktop/OOK.mp3"

# 加载MP3文件
audio_file = eyed3.load(audio_file_path)

# 检查是否存在ID3标签，如果不存在则创建
if audio_file.tag is None:
    audio_file.initTag()

# 修改标题
audio_file.tag.title = "ok不OK"

# 修改艺术家
audio_file.tag.artist = "zombie"

# 修改专辑
audio_file.tag.album = "the new zombie"

# 保存更改
audio_file.tag.save()

# 检测是否已经以管理员权限运行
if sys.platform == 'win32':
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        isAdmin = False

    if isAdmin:
        print("已经以管理员权限运行")
    else:
        # 重新启动程序并请求管理员权限
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join([f'"{arg}"' for arg in sys.argv]), None, 0)
