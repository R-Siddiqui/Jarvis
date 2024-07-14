import pyautogui

from time import sleep
sleep(1)
pyautogui.keyDown('win')
pyautogui.press('a')
pyautogui.keyUp('win')
sleep(2)
pyautogui.click(x=1697, y=586)