import pyautogui
import numpy as np
import cv2

# 設定螢幕擷取區域
screen_width, screen_height = pyautogui.size()
screen_area = (0, 0, screen_width, screen_height)  # 螢幕大小

def capture_screen():    
    screenshot = pyautogui.screenshot(region=screen_area)
    screenshot = np.array(screenshot)  
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  
    return screenshot

def save_screenshot(filename="screenshot.png"):
    screenshot = capture_screen()
    cv2.imwrite(filename, screenshot)
    print(f"螢幕截圖已儲存為 {filename}")
    
# 測試
if __name__ == "__main__":
    save_screenshot("test_screenshot.png")