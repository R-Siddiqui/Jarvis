import pyautogui
import pyperclip as p
from time import sleep
query = "remember it my birthday at 21july at 1.39am "
pyautogui.press('win')
pyautogui.press('tab')
sleep(0.5)
pyautogui.press('enter')
sleep(2)
pyautogui.hotkey('ctrl','N')
query = query.replace("remember it", "")
p.copy(query)
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
sleep(0.5)
pyautogui.hotkey('alt','F4')