import cv2
import numpy as np
import os
from app.config import consts


def box(fullpath, cwd):
    """
    boxed each word in image for improve results
    """
    # Load image, grayscale, Otsu's threshold
    image = cv2.imread(fullpath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph operations
    opening_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, opening_kernel, iterations=1)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 50))
    dilate = cv2.dilate(opening, kernel, iterations=2)

    # Remove center line
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        ar = w / float(h)
        if area > 10000 and area < 12500 and ar < .5:
            cv2.drawContours(dilate, [c], -1, 0, -1)

    # Dilate more
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    dilate = cv2.dilate(dilate, kernel, iterations=3)

    # Draw boxes
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 100000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 3)

    cv2.imwrite(cwd+consts.path_dic_data+'/thresh.png', thresh)
    cv2.waitKey()


def srceen_image(fullpath):
    """
    get path of image and fix screen burn of image
    """
    cwd = os.getcwd()
    img = cv2.imread(fullpath, -1)
    rgb_planes = cv2.split(img)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)

    cv2.imwrite(cwd + consts.path_dic_data + 'shadows_out.png', result)
    cv2.imwrite(cwd + consts.path_dic_data + 'shadows_out_norm.png', result_norm)
    return cwd + consts.path_dic_data + 'shadows_out.png'
