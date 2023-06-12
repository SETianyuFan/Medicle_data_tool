import os
import shutil

directory = "/home/tianyu/Desktop/Task501_testFirst/labelsTr"

for filename in os.listdir(directory):

    if os.path.isfile(os.path.join(directory, filename)):
        # 替换文件名中的 "task1" 为 "taskfirst"
        new_name = filename.replace("test1", "testFirst")
        # 使用shutil.move进行重命名
        shutil.move(os.path.join(directory, filename), os.path.join(directory, new_name))