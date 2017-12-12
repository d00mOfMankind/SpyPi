#Dependencies (use pip install [package name])
#    gpiozero
#    picamera

print("Importing motion sensor...")
from gpiozero import MotionSensor #Imports the motion sensor functions from gpiozero
pir = MotionSensor(18) #what gpio pin to take motion detector input from

print("Importing time...")
from datetime import datetime #imports date getting function

print("Importing camera...")
from picamera import PiCamera #guess what this imports?
cam = PiCamera()

import os

print("Load sequence complete.")




def normal():
	if not (os.path.isdir("vid")):
		os.makedirs("vid")

	while True:
	    pir.wait_for_motion()
	    
	    now = str(datetime.now())
	    log = "Motion detected at >" + now
	    vidLoc = "vid/image_" + now + ".h264"
	    
	    print(log)
	    
	    with open("log.txt", "a") as file:
	        file.write(log + "\n")
	        file.close()
	        
	    
	    cam.start_recording(vidLoc)
	    pir.wait_for_no_motion()
	    cam.stop_recording()



def low_fps():
	if not (os.path.isdir("imgFPS")):
		os.makedirs("imgFPS")

	while True:
	    pir.wait_for_motion()
	    
	    now = str(datetime.now())
	    log = "Motion detected at >" + now
	    imgLoc = "imgFPS/image_" + now + ".png"
	    
	    print(log)
	    
	    with open("log.txt", "a") as file:
	        file.write(log + "\n")
	        file.close()




def static():
	if not (os.path.isdir("img")):
		os.makedirs("img")

	while True:
	    pir.wait_for_motion()
	    
	    now = str(datetime.now())
	    log = "Motion detected at >" + now
	    imgLoc = "img/image_" + now + ".png"
	    
	    print(log)
	    
	    with open("log.txt", "a") as file:
	        file.write(log + "\n")
	        file.close()


	    cam.capture(imgLoc)


#uncomment what one you want
static() #take a static image every time it sees movement
#low_fps() #take a static image every second while it sees movement
#normal() #take video while it sees movement