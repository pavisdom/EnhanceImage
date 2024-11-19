# This is a sample Python script.
import os
import re
from time import sleep

from cutout import CutoutProClient
from email_service import TempMail

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

img_formats = ['jpg', 'jpeg', 'png']
cutout = CutoutProClient()
folder= '/home/pavithra/Downloads/t'
img_list = [os.path.join(folder,f) for f in os.listdir(folder) if f.split(".")[-1].lower() in img_formats]
print("\n".join(img_list))
for img in img_list:
    print(os.path.split(img))
x = input(f"{len(img_list)} many images. wanna continue? (y/n)")
if x.lower() != 'y':
    exit()

# clear()
print_list = [{"id":i,"file":f,"name":os.path.split(f)[1], "attempts": 0, "status": "pending"} for i,f in enumerate(img_list)]
# print_str = "\n".join(["{id}. {name} - {attempts} - {status}".format(**p) for p in print_list])
# print(print_str)

def print_img_list(index=None,attempt=0,status=None):
    if index is not None:
        print_data = print_list[index]
        print_data["attempts"] += attempt
        print_data["status"] = status or print_data["status"]
        print_list[index] = print_data

    print_str = "\n".join(["{id}. {name} - {attempts} - {status}".format(**p) for p in print_list])
    clear()
    print(print_str)

# print()
# print(f"{len(print_list)}")

while True:
    file_list = [f_ for f_ in print_list if f_["status"] != "success"]
    for f_data in file_list:
        print_img_list(index=f_data["id"],attempt=1,status="processing")
        enh = cutout.image_enhance_clean(f_data["file"])
        _status = "success" if enh else "failed"
        print_img_list(index=f_data["id"],status=_status)
    # else:
    #     print("All images are done!")
    #     break
    if len(file_list) == 0:
        print("All images are done!")
        break
