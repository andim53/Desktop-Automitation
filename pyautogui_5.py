import pyautogui
from time import sleep

ytname= pyautogui.prompt(text="", title="write your youtube channel")
sleep(1)
print(ytname)
# Make a python script that'll find a youtube channel
pyautogui.hotkey("ctrl","t")
sleep(1)

pyautogui.write("https://www.youtube.com/")

pyautogui.hotkey("enter")

sleep(1.5)

res=pyautogui.locateCenterOnScreen("image/ytser.png",confidence=0.9)
pyautogui.moveTo(res)
#click
pyautogui.click()