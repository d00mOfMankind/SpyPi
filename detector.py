#Dependencies (use pip install [package name]), must have pip installed, (apt install python-pip)
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
#cam.resolution(400, 400) #set resolution of image to take, default is 640x480

import os #this is used to check if folders exist and create folders

print("Load sequence complete.")




def normal():
	if not (os.path.isdir("vid")): #if folder does not exist
		os.makedirs("vid") #create folder

	while True: #loop forever
	    pir.wait_for_motion() #when PIR detects motion
	    
	    now = str(datetime.now()) #get datetime and cast to string
	    log = "Motion detected at >" + now #create log string
	    vidLoc = "vid/video_" + now + ".h264" #create location to save file (.h264 is MP4)
	    
	    print(log) #print the log string
	    
	    with open("log.txt", "a") as file: #open the file (will also create if doesn't exist
	        file.write(log + "\n") #write the log string (and a newline) to the file
	        file.close() #close file (saves memory and prevents write bugs)
	        
	    
	    cam.start_recording(vidLoc) #start recording
	    pir.wait_for_no_motion() #wait until there is no motion detected
	    cam.stop_recording() #stop recording



def low_fps(): #not finished, DNU
#	if not (os.path.isdir("imgFPS")):
#		os.makedirs("imgFPS")
#
#	while True:
#	    pir.wait_for_motion()
#	    
#	    now = str(datetime.now())
#	    log = "Motion detected at >" + now
#	    imgLoc = "imgFPS/image_" + now + ".png"
#	    
#	    print(log)
#	    
#	    with open("log.txt", "a") as file:
#	        file.write(log + "\n")
#	        file.close()
	pass



def static(): #take static images
	if not (os.path.isdir("img")): #if folder does not exist
		os.makedirs("img") #create folder

	while True: #loop forever
	    pir.wait_for_motion() #wait until motion detected
	    
	    now = str(datetime.now()) #get current datetime
	    log = "Motion detected at >" + now #create log string
	    imgLoc = "img/image_" + now + ".png" #create location to save image
	    
	    print(log) #print log test to screen
	    
	    with open("log.txt", "a") as file: #open log file
	        file.write(log + "\n") #write log string (and newline)
	        file.close() #close file, prevents errors and is generally just good practice


	    cam.capture(imgLoc) #take a image, save it at location we generate earlier


#uncomment what one you want
static() #take a static image every time it sees movement
#low_fps() #take a static image every second while it sees movement
#normal() #take video while it sees movement
