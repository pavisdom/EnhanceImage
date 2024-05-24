import cv2

ASPECT_RATIO = 0.75


def resize_image(target_path,source_path):
    source_image = cv2.imread(source_path, cv2.IMREAD_UNCHANGED)
    target_image = cv2.imread(target_path, cv2.IMREAD_UNCHANGED)
    source_h, source_w, _ = source_image.shape
    target_image = cv2.resize(target_image, (source_h, source_w), interpolation=cv2.INTER_CUBIC)
    return target_image, source_image


def rotate_image(mat, angle, img_path=False, save_path=None):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """
    if img_path:
        mat = cv2.imread(mat, cv2.IMREAD_UNCHANGED)

    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0])
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    # print(f"h:{height}, w:{width} bh:{bound_h}, bw:{bound_w}")
    if save_path:
        cv2.imwrite(save_path, rotated_mat)
    return rotated_mat


def bounding_box(img):
    # Load image, grayscale, Gaussian blur, threshold
    image = img.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x, y, w, h = cv2.boundingRect(gray)
    # print(f"x:{x}, y:{y}, w:{w}, h:{h}")
    ratio = round(w/h, 2)
    # print(f"ratio:{ratio}")

    # color = (0, 255, 0)
    # thickness = 2
    #
    # cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

    return ratio, (x, y, w, h)


def crop_image(image, vals: tuple, save_path=None):
    x, y, w, h = vals
    crop = image[y:y + h, x:x + w]
    if save_path:
        cv2.imwrite(save_path, crop)
    return crop

def rotate_45(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    new_image = rotate_image(image, -45)
    cv2.imwrite(img_path, new_image)


ROTATION_ANGLE_MIN = 0
ROTATION_ANGLE_MAX = -90

def rotate_until_ratio(img, max_iter=15):
    rot_start = ROTATION_ANGLE_MIN
    rot_end = ROTATION_ANGLE_MAX
    rot_angle = 0
    _count = 0
    while True:
        # image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        image = img.copy()
        img_h, img_w, _ = image.shape
        print(f"img_h:{img_h}, img_w:{img_w}")
        image = rotate_image(image, rot_angle)
        ratio, (x,y,w,h) = bounding_box(image)
        print(f"angle:{rot_angle} ratio:{ratio} | start:{rot_start} end:{rot_end}")


        if ratio > ASPECT_RATIO:
            # print("rotate")
            rot_end = rot_angle
        elif ratio < ASPECT_RATIO:
            # print("rotate")
            rot_start = rot_angle
        else:
            # print("done")
            return rot_angle, (x,y,w,h)
        if _count >= max_iter:
            return rot_angle, (x,y,w,h)

        rot_angle = rot_start + round((rot_end - rot_start)/2,2)
        _count += 1


# image, rot_ratio = rotate_until_ratio("test.png")
#
# cv2.imwrite("final.png", image)
# cv2.imshow('image', image)
# cv2.waitKey()

# image = cv2.imread("test.jpeg", cv2.IMREAD_UNCHANGED)
# image = rotate_image(image, -45)
# h, w, _ = image.shape
# print(f"h:{h}, w:{w}")
# cv2.imshow('image', image)
# cv2.waitKey()
