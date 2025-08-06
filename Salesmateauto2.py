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

#Going to add new customer
pyautogui.press(['alt', 'c'])
pyautogui.press('a')

#Setting customer name
pyautogui.press(['tab', 'tab'], 1, 1)
pyautogui.typewrite('Savio')

#Setting customer category as wholesale
pyautogui.press(['tab'] * 8, 1, 1)
pyautogui.press("up")

#Setting membership fee
pyautogui.press(['tab'] * 4, 1, 1)
pyautogui.press(['space', 'tab'])
pyautogui.typewrite("500")

#Setting security deposit
pyautogui.press(['tab', 'space', 'tab'])
pyautogui.typewrite("50")

#Saving the customer info
pyautogui.press(['tab', 'enter'])
pyautogui.press(['enter'], 1, 3)