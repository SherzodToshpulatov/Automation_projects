# This is a sample Python script.
import time

import pyautogui

# print(pyautogui.size())
# print(pyautogui.position())
#pyautogui.moveTo(100,100,5)
time.sleep(3)
#pyautogui.scroll(-500,1)

##draw star
# pyautogui.mouseDown(600,200, button="left")
# pyautogui.moveTo(400,600,3)
# pyautogui.moveTo(800,300,3)
# pyautogui.moveTo(400,300,3)
# pyautogui.moveTo(800,600,3)
# pyautogui.moveTo(600,200,3)

##spiral drawing
# distance = 400
# while distance >0:
#     pyautogui.dragRel(distance,0,1,button="left")
#     distance = distance-20
#     pyautogui.dragRel(0,distance,1,button="left")
#     pyautogui.dragRel(-distance,0,1,button="left")
#     distance = distance-20
#     pyautogui.dragRel(0,-distance,1,button="left")
#     time.sleep(2)


pyautogui.FAILSAFE = True

time.sleep(3)
for i in range(100):
    pyautogui.write("TEXT")
    pyautogui.press("enter")