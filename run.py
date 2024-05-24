# ### run from here
# import os
# import sys
#
# from cutout import CutoutProClient
# FOLDER_NAME = "Enhanced"
#
# # arg_list = sys.argv
# # print(arg_list)
# # files = []
# # if len(arg_list) > 1:
# #     files = [
# #         f for f in arg_list if os.path.isfile(f)
# #         and not f.lower().endswith(".py")
# #     ]
# #
# # else:
# #     # todo:
# #     exit()
#
# files = ["53351511.jpg"]
# # try:
#
#
# cutout = CutoutProClient()
#
# for f in files:
#     # _dir, _file = os.path.split(f)
#     # save_path = os.path.join(_dir,FOLDER_NAME)
#     # if not os.path.exists(save_path):
#     #     os.makedirs(save_path)
#     # _file = f"{_file.split('.')[0]}.jpg"
#     #
#     # save_path = os.path.join(save_path, _file)
#     # print(save_path)
#     cutout.image_enhance(f)
#     print("-----------------------")
# # except Exception as e:
# #     print(e)
# #     input("press enter to exit")


import os
import sys

from cutout import CutoutProClient


FOLDER_NAME = "Enhanced"
print("enhancement runnig....")
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

cutout_client = CutoutProClient()
failed_files = []

printing_list = [{"id": i+1, "name":os.path.split(file)[1], "status": "-", "save_path": "-"} for i,file in enumerate(files)]

def print_progress():
    os.system('cls')
    print("Enhancement Progress")
    for data in printing_list:
        print("{id}.\t{name}\t{status}\t{save_path}".format(**data))

print_progress()

try:
    for i,f in enumerate(files):
        _dir, _file = os.path.split(f)
        save_path = os.path.join(_dir, FOLDER_NAME)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        _file = f"{_file.split('.')[0]}.jpg"

        save_path = os.path.join(save_path, _file)
        printing_list[i]["save_path"] = save_path
        printing_list[i]["status"] = "pending"
        print_progress()
        # print(save_path)
        cutout_client.image_enhance(f, save_path=save_path)
        f_size = os.path.getsize(save_path)
        if f_size == 122:
            # print("file enhance failed.")
            printing_list[i]["status"] = "pending"
            failed_files.append((f,save_path))
        else:
            printing_list[i]["status"] = "completed"
        print_progress()
except Exception as e:
    print(e)

if len(failed_files) > 0:
    print(f"{len(failed_files)} many imgs has failed")
    if input("If you wanna retry press y") == 'y':
        for f, save_path in failed_files:
            cutout_client.image_enhance(f, save_path=save_path)
            print("-----------------------")

input("press enter to exit")