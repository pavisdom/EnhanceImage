### run from here
import os
import sys

from cutout import CutoutProClient
FOLDER_NAME = "Enhanced"

arg_list = sys.argv
print(arg_list)
files = []
if len(arg_list) > 1:
    files = [
        f for f in arg_list if os.path.isfile(f)
        and not f.lower().endswith(".py")
    ]

else:
    # todo:
    exit()
try:


    cutout = CutoutProClient()

    for f in files:
        _dir, _file = os.path.split(f)
        save_path = os.path.join(_dir,FOLDER_NAME)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        _file = f"{_file.split('.')[0]}.jpg"

        save_path = os.path.join(save_path, _file)
        print(save_path)
        cutout.image_enhance(f,save_path)
        print("-----------------------")
except Exception as e:
    print(e)
    input("press enter to exit")