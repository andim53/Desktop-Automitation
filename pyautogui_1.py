import pyautogui 

# get the location of the "help" menu in the screen
res = pyautogui.locateOnScreen(r"C:/Users/3x4m4/OneDrive/Desktop/python project 2/image/help.png")
print(res)

edit_but= pyautogui.center(res)# find center
print (edit_but)

pyautogui.moveTo(edit_but)# move mouse to 