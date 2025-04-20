import time
from utils.screen import capture_screen
from utils.vision import find_image
from utils.input import hold_key, press_key

def auto_run_loop(template_path=None, step_time=3, rest_time=1):
    print("開始自動跑圖... 按 Ctrl+C 停止")
    while True:
        if template_path:
            screen_image = capture_screen()
            match = find_image(template_path, screen_image, threshold=0.8, auto_click=False)

            if match:
                print("畫面中找到圖，開始移動")
            else:
                print("沒找到圖，跳過")
                time.sleep(1)
                continue

        time.sleep(rest_time)