### run from here
import os
import sys

from cutout import CutoutProClient

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
cutout = CutoutProClient()

for f in files:
    cutout.image_enhance(f)
    print("-----------------------")