import pyautogui as pag
import random
import time

while True: #Create a while loop and setting it to true so it runs the code infinitely
	x = random.randint(600,700) #Random x coordinates for the mouse
	y = random.randint(200,600) #Random y coordinates for the mouse
	pag.moveTo(x,y,0.5) #Telling the mouse to move to these coordinates with a speed of .5
	time.sleep(2) #Sleep for two seconds before running again
