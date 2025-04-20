import cv2
from utils.screen import capture_screen
from utils.vision import find_image_and_click
from core.runner import auto_run_loop
from config import STEP_TIME, REST_TIME, TEMPLATE_DIR
import os

def main():
    template_path = os.path.join(TEMPLATE_DIR, "start_button.png")

    # 啟動自動跑圖
    auto_run_loop(template_path=template_path, step_time=STEP_TIME, rest_time=REST_TIME)

if __name__ == "__main__":
    main()