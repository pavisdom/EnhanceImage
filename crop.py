import cv2
import numpy as np



def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

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
    return rotated_mat

# image = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
#
# r_img = rotate_image(image, 45)
# cv2.imwrite("rot_image.png", r_img)
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# cv2.imshow('image', image)
# cv2.imshow('r_image', r_img)
# cv2.waitKey(0)
def bounding_box(img):
    # Load image, grayscale, Gaussian blur, threshold
    image = img.copy()
    # bgr = image[:,:,:3] # Channels 0..2
    # gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x, y, w, h = cv2.boundingRect(gray)
    print(f"x:{x}, y:{y}, w:{w}, h:{h}")
    print(f"ratio:{w/h}")


    # img_h, img_w, _ = image.shape
    # img = cv2.imread('test.jpeg')
    #
    # img = cv2.resize(img, (img_h, img_w), interpolation = cv2.INTER_CUBIC)
    #
    color = (0, 255, 0)
    thickness = 2
    # # dimensions = img.shape
    # #
    # # print("dimensions",dimensions)
    #
    # cv2.rectangle(image, (x,y), (x+w,y+h), color, thickness)

    # cv2.imwrite("final.png", image)
    # cv2.imshow('image', image)
    # cv2.waitKey()

image = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)

bounding_box(image)

img2 = rotate_image(image, -45)
bounding_box(img2)

img3 = rotate_image(image, -30)
bounding_box(img3)
# img_h, img_w, _ = image.shape
#
# blur = cv2.GaussianBlur(gray, (3,3), 0)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)[1]
#
# # Find contours
# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# c = max(cnts, key=cv2.contourArea)
#
# # Obtain outer coordinates
# left = tuple(c[c[:, :, 0].argmin()][0])
# right = tuple(c[c[:, :, 0].argmax()][0])
# top = tuple(c[c[:, :, 1].argmin()][0])
# bottom = tuple(c[c[:, :, 1].argmax()][0])
#
# # Draw dots onto image
# cv2.drawContours(image, [c], -1, (36, 255, 12), 2)
# cv2.circle(image, left, 8, (0, 50, 255), -1)
# cv2.circle(image, right, 8, (0, 255, 255), -1)
# cv2.circle(image, top, 8, (255, 50, 0), -1)
# cv2.circle(image, bottom, 8, (255, 255, 0), -1)
#
# print('w: {} h: {}'.format(img_w,img_h))
#
# print('left: {}'.format(left))
# print('right: {}'.format(right))
# print('top: {}'.format(top))
# print('bottom: {}'.format(bottom))
#
# cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
#
# cv2.imshow('thresh', thresh)
# cv2.imshow('image', image)
# cv2.waitKey()


