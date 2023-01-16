import pyautogui as robo
import time
q = int(robo.prompt(text='',title="Enter amount to be printed"))
time.sleep(5)
for x in range(q):
    print("waiting 10 second")
    time.sleep(10)
    robo.keyDown('ctrl')
    robo.press("p")
    robo.keyUp('ctrl')
    time.sleep(3)
    robo.press("enter")
    print("printing "+str(x+1))

robo.alert("Printing Completed")


