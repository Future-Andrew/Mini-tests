import eyed3

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

# 打印出标签信息以确认更改
print("ID3标签信息：")
print("标题:", audio_file.tag.title[0] if audio_file.tag.title else "无")
print("艺术家:", audio_file.tag.artist[0] if audio_file.tag.artist else "无")
print("专辑:", audio_file.tag.album[0] if audio_file.tag.album else "无")
