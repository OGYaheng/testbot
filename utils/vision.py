import cv2
import numpy as np
from utils.input import click_button

def find_image(template_path, screen_image, threshold=0.8):
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    gray_screen = cv2.cvtColor(screen_image, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(gray_screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)  # 取得匹配位置

    if loc[0].size > 0:
        x, y = loc[1][0], loc[0][0]
        click_button(x + w // 2, y + h // 2)
        return (loc[1][0], loc[0][0], w, h)
    else:
        return None

def draw_rectangle(screen_image, box):
    x, y, w, h = box
    cv2.rectangle(screen_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 測試：結果
if __name__ == "__main__":
    screen_image = cv2.imread("test_screenshot.png")
    result = find_image("resources/templates/your_template.png", screen_image)
    if result:
        print(f"找到匹配位置：{result}")
        draw_rectangle(screen_image, result)
        cv2.imshow("Matched Image", screen_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("找不到匹配的圖案")
