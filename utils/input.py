import pyautogui
import time

def click_button(x, y):
    pyautogui.click(x, y)

def move_mouse(x, y):
    pyautogui.moveTo(x, y)

def press_key(key):
    pyautogui.press(key)

def hold_key(key, duration=1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
    