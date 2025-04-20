import cv2
from utils.screen import capture_screen
from utils.vision import find_image_and_click

screen_image = capture_screen()

template_path = "resources/templates/start_button.png"
if find_image_and_click(template_path, screen_image):
    print("成功點擊按鈕！")
else:
    print("沒有找到匹配的按鈕。")