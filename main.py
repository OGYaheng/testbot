import os
from config import STEP_TIME, REST_TIME, TEMPLATE_DIR
from core.runner import auto_run_loop

def main():
    template_path = os.path.join(TEMPLATE_DIR, "start_button.png")

    # 啟動自動跑圖
    auto_run_loop(template_path=template_path, step_time=STEP_TIME, rest_time=REST_TIME)

if __name__ == "__main__":
    main()