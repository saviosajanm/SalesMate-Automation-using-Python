import pyautogui
from win32api import GetSystemMetrics

pyautogui.FAILSAFE = False

#get the width and height of the monitor
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

#click on the button left to launch the start menu
pyautogui.click(0, height)

pyautogui.typewrite("Salesmate +")

pyautogui.press("enter", 1, 1)

pyautogui.press("right", 1, 1)
pyautogui.press("enter", 1, 1)

#Sometimes SalesMate+ might take 10 seconds to load it. SO 10 sec delay
pyautogui.press("enter")

#Going to add misc. income
pyautogui.press(['alt', 't'])
pyautogui.press('i')

#Setting transaction as compliment
pyautogui.press(['tab', 'tab'], 1, 1)
pyautogui.press(['down', 'down'], 1, 1)

#Setting complement amount to Rs. 500
pyautogui.press(['tab', 'tab'], 1, 1)
pyautogui.typewrite("500")

#Adding description
pyautogui.press('tab', 1, 1)
pyautogui.typewrite("Complement of 500Rs.")

#Saving transaction and closing dialog
pyautogui.press(['enter'], 1, 1)
pyautogui.press(['enter', 'tab', 'enter'], 1, 3)