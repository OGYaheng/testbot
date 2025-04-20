import pyautogui
import time

def click_button(x, y):
    pyautogui.click(x, y)
    print(f"點擊位置：({x}, {y})")

def move_mouse(x, y):
    pyautogui.moveTo(x, y)
    print(f"滑鼠移動到：({x}, {y})")

def press_key(key):
    pyautogui.press(key)
    print(f"按下按鍵：{key}")

def hold_key(key, duration=1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
    print(f"按住 {key} {duration} 秒")
