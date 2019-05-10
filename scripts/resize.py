"""
Crops and resizes all images in specified folder.
Cropped size and folder path can be changed in the code.
"""

import cv2
import os

folder = 'assets/images/gallery'
root = os.path.dirname(os.getcwd())

img_path = os.path.join(root, folder)
file_names = os.listdir(img_path)

for file_name in file_names:
    full_path = os.path.join(img_path, file_name)
    img = cv2.imread(full_path)
    # crop a center square
    if not (img.shape[0] == img.shape[1]):
        if img.shape[0] > img.shape[1]:
            crop_size = img.shape[1]
            start = img.shape[0] / 2 - crop_size / 2
            img = img[start:start+crop_size, :]
        else:
            crop_size = img.shape[0]
            start = img.shape[1] / 2 - crop_size / 2
            img = img[:, start:start+crop_size]
    # resize to 500x500 pixels
    img = cv2.resize(img, (500, 500))
    cv2.imwrite(full_path, img)