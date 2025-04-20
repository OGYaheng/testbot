import cv2
import numpy as np
from utils.input import click_button
from config import DEFAULT_THRESHOLD

def find_image(template_path, screen_image, threshold=DEFAULT_THRESHOLD, auto_click=True):
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        print(f"[錯誤] 找不到圖片：{template_path}")
        return None

    result = cv2.matchTemplate(screen_image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    h, w = template.shape[:2]
    if loc[0].size > 0:
        x, y = loc[1][0], loc[0][0]
        if auto_click:
            click_button(x + w // 2, y + h // 2)
        return (x, y, w, h)
    return None