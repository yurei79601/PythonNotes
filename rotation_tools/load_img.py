import base64
import cv2
import numpy as np


class ImageTransfromError(Exception):
    """影像轉換錯誤"""
    pass


def base64_transformer(logger, input_data: dict) -> np.ndarray:
    """
    To transform a base64 string to a image with numpy array

    Args:
        logger: 記 log 的物件
        input_data: 輸入 API 的資料
            image_cv_id: key 值
            image: a string with base64 type representing an image

    Return
        image: an image with numpy array
    """
    try:
        image_cv_id = input_data['image_cv_id']
        base64_string = input_data['image']
        img_base64_binary = base64_string.encode("utf-8")
        img_binary = base64.b64decode(img_base64_binary)
        image = cv2.imdecode(np.frombuffer(
            img_binary, np.uint8), cv2.IMREAD_COLOR)
        return image
    except Exception as error:
        logger.error(
            {
                "process_code": "ERROR_BASE64_TRANSFORM",
                "key": image_cv_id,
                "msg": str(error)
            }
        )
        raise ImageTransfromError(
            f"cannot identify image file. error: {str(error)}")
