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

print("Load sequence complete.")

while True:
    pir.wait_for_motion()
    
    now = str(datetime.now())
    log = "Motion detected at >" + now
    imgLoc = "img/image_" + now + ".png"
    vidLoc = "vid/image_" + now + ".h264"
    
    print(log)
    
    with open("log.txt", "a") as file:
        file.write(log + "\n")
        file.close()
        
    #cam.capture(imgLoc) #take static image
    
    cam.start_recording(vidLoc)
    
    pir.wait_for_no_motion()
    cam.stop_recording()
    