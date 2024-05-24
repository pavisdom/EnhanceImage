### run from here
import os
import sys

from cutout import CutoutProClient
from rotate import rotate_45, rotate_until_ratio, rotate_image, resize_image, crop_image

FOLDER_NAME = "Enhanced"

enhance_quality = {
    "0": False,
    "1": "jpg_50",
    "2": "jpg_75",
    "3": "jpg_100"
}

def crop_to_ratio(files):
    error_files = []
    bg_files_done = []
    enh_files_done = []
    cutout = CutoutProClient()
    print("select enhance quality:")
    print("0 : no enhance")
    print("1 : jpg_50")
    print("2 : jpg_75")
    print("3 : jpg_100")
    quality = enhance_quality.get(input("enter value"),False)
    print(f"enhance quality: {quality}")
    for f in files:
        try:
            _dir, _file = os.path.split(f)
            save_path = os.path.join(_dir,FOLDER_NAME)
            crop_path = os.path.join(save_path, "crop")
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            if not os.path.exists(crop_path):
                os.makedirs(crop_path)
            _file = f"{_file.split('.')[0]}.jpg"

            save_path = os.path.join(save_path, _file)
            crop_path = os.path.join(crop_path, _file)
            # print(save_path, crop_path)
            # _path = cutout.image_enhance(f,save_path)
            bg, enh = cutout.download(f,quality,save_path)
            bg_img, enh_img = resize_image(bg, enh)
            angle, vals = rotate_until_ratio(bg_img)
            # print(angle, vals)
            rot_img = rotate_image(enh_img, angle, save_path=save_path)
            crop_image(rot_img, vals, save_path=crop_path)

            enh_files_done.append(save_path)
            # bg_files_done.append(bg)
            os.remove(bg)
        except Exception as e:
            print(e)
            error_files.append(f)

    # rotate_45(_path)
    # os.remove(bg)
    print("-----------------------")
    print(f"filse done: {len(enh_files_done)}/{len(files)}")
    if input("do you wanna delete original the files? (y/n)").lower() == "y":
        for f in enh_files_done:
            os.remove(f)
    # if input("do you wanna delete png the files? (y/n)").lower() == "y":
    #     for f in bg_files_done:
    #         os.remove(f)
    if len(error_files) > 0:
        print("Error files: ", error_files)
        x = input("do you wanna try again? (y/n)")
        if x.lower() == "y":
            crop_to_ratio(error_files)

arg_list = sys.argv

print("EnhanceAndCrop is started!")


files = []
if len(arg_list) > 1:
    files = [
        f for f in arg_list if os.path.isfile(f)
        and not f.lower().endswith(".py")
    ]
    print("the files recieved are: ")
    print("\n".join(files))
else:
    # todo:
    exit()

crop_to_ratio(files)

input("press enter to exit")
# except Exception as e:
#     print(e)
#     input("press enter to exit")