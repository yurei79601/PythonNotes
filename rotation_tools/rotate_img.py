"""
image rotation utilities
"""
from math import sin, cos, radians, fabs
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from src.id_ocr_config import rotation_mark_angle_dict


def rot_by_tilt_angle(img: np.ndarray, tilt_angle: int) -> np.ndarray:
    """
    Rotate image according to given tilt angle

    Args:
        img: image with numpy array
        tilt_angle: rotate angle

    Returns:
        rotated image
    """
    if tilt_angle == 0:
        imgRotation = img
    else:
        height, width = img.shape[:2]
        heightNew = int(width*fabs(sin(radians(tilt_angle))) +
                        height*fabs(cos(radians(tilt_angle))))
        widthNew = int(height*fabs(sin(radians(tilt_angle))) +
                       width*fabs(cos(radians(tilt_angle))))

        matRotation = cv2.getRotationMatrix2D((width/2, height/2),
                                              tilt_angle, 1)

        matRotation[0, 2] += (widthNew-width)/2
        matRotation[1, 2] += (heightNew-height)/2

        imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew),
                                     borderValue=(255, 255, 255))
    return imgRotation


def calc_feature_quadrant(img: np.ndarray, boxes: pd.DataFrame) -> int:
    """
    Calculate feature quadrant
    (e.g., passbook inner barcode, id card flag...)
    這裡的「象限」是以 plt.imshow 的角度去看，
    因為 plt.imshow 的座標軸跟笛卡爾座標是 x, y 顛倒的；
    但我們是以人眼直接看 plt.imshow 的相對位置，
    所以在 quadrant 的定義會有點不同

    Args:
        img (array): image
        boxes (pd.DataFrame): feature coordinate detected by yolo model

    Returns:
        quadrant (int): 1 / 2 / 3 / 4
    """
    quadrant = None
    if boxes.empty:
        raise Exception('Cannot get barcode boxes.')
    elif len(boxes) > 1:
        raise Exception('Get more than 1 boxes.')
    else:
        x = int((boxes['x_min']+boxes['x_max'])/2)
        y = int((boxes['y_min']+boxes['y_max'])/2)
        y_center, x_center = get_img_center(img)
        x_diff = x - x_center
        y_diff = y - y_center
        if (x_diff > 0) & (y_diff < 0):
            quadrant = 1
        elif (x_diff < 0) & (y_diff < 0):
            quadrant = 2
        elif (x_diff < 0) & (y_diff > 0):
            quadrant = 3
        elif (x_diff > 0) & (y_diff > 0):
            quadrant = 4
        return quadrant


def calc_feature_rot_angle(quadrant: int, rotation_mark: str) -> int:
    """
    To calculate the angle to rotate by rotation_mark

    Args:
        quadrant: the location of quadrant of rotation_mark related to the original image
        rotation_mark: the mark in image.
            all possible options are: flag, barcode, logo

    Returns:
        the angle should rotate
    """
    try:
        return rotation_mark_angle_dict[rotation_mark][quadrant]
    except:
        raise ValueError('off-spec quadrant')


def remove_white_border(img: np.ndarray) -> np.ndarray:
    """
    To remove the white border for the input image

    Args:
        img: the input image with the form np.array

    Returns:
        an image without the white border of the input image
    """
    try:
        # (1) Convert to gray, and threshold
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

        # (2) Morph-op to remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

        # (3) Find the max-area contour
        cnts = cv2.findContours(
            morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        cnt = sorted(cnts, key=cv2.contourArea)[-1]

        # (4) Crop and save it
        x, y, w, h = cv2.boundingRect(cnt)
        dst = img[y:y+h, x:x+w]
        return dst
    except:
        raise


def get_img_center(img: np.ndarray) -> np.ndarray:
    '''
    Get image center point

    Args:
        - img: image

    Returns:
        center point of image
    '''
    height, width = img.shape[:2]
    return np.array([height / 2, width / 2], dtype=np.int)


def get_rotation_matrix(angle: float) -> np.ndarray:
    '''
    Get rotation matrix

    Args:
        - angle: rotation angle

    Returns:
        rotation matrix
    '''
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))
    return R


def get_rotated_poly(poly: np.ndarray, angle: float) -> np.ndarray:
    '''
    把 input 的點去旋轉，方向是順時針

    Args:
        - poly: array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        - angle: 想要旋轉的角度，單位是「度」

    Returns:
        rotated polys
    '''
    rotation_arr = get_rotation_matrix(angle)
    rotated_poly = np.dot(poly, rotation_arr)
    return rotated_poly


def get_rotated_poly_by_images(
    img_before_rotated: np.ndarray,
    poly_before_rotated: np.ndarray,
    img_after_rotated: np.ndarray,
    angle: float
) -> np.ndarray:
    '''
    根據現在的照片，現在的點，想要轉過去的照片，要轉的角度，
    來找到轉過去的點的座標是多少

    Args:
        - img_before_rotated: 旋轉前的影像檔
        - poly_before_rotated: 旋轉前的點座標
        - img_after_rotated: 旋轉過後的影像檔
        - angle: 影像旋轉的角度，單位是「度」

    Returns:
        轉過來的點座標，以 (n, 2) 的 np.ndarray 呈現

    Example:
        一張圖片 (img_before_rotated) 裡面有斜斜的長方形 (poly_before_rotated)
        我們想要知道轉正以後的影像檔，其中轉正的長方形座標 (img_after_rotated) 是多少
        就是用這個函數來求得
    '''
    center_before_rotated = get_img_center(img=img_before_rotated)[::-1]
    center_after_rotated = get_img_center(img=img_after_rotated)[::-1]
    relative_poly = poly_before_rotated - center_before_rotated
    rotated_relative_poly = get_rotated_poly(poly=relative_poly, angle=angle)
    poly_after_rotated = rotated_relative_poly + center_after_rotated
    return poly_after_rotated


def trans_poly_to_list(poly: np.ndarray) -> list:
    """
    將 poly 以 np.ndarray 格式轉成 list of tuple 的格式
    因為要給 json 取用

    Args:
        - poly: 點座標，以 (n, 2) 的 np.ndarray 呈現
    Returns:
        點座標，
        以 [(x1, y1), (x2, y2), (x3, y3), (x4, y4)] 呈現
    """
    list_of_tuples = [
        (int(poly[0][0]), int(poly[0][1])),
        (int(poly[1][0]), int(poly[1][1])),
        (int(poly[2][0]), int(poly[2][1])),
        (int(poly[3][0]), int(poly[3][1]))
    ]
    return list_of_tuples
