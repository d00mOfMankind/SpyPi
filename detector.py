#Dependencies (use pip install [package name])
#    gpiozero
#    picamera


from gpiozero import MotionSensor #Imports the motion sensor functions from gpiozero
from datetime import datetime #imports date getting function
from picamera import PiCamera #guess what this imports?


pir = MotionSensor(4)
cam = PiCamera()


while True:
    pir.wait_for_motion()
    
    now = str(datetime.now())
    log = "Motion detected at >" + now + "\n"
    imgLoc = "/home/pi/MotionCam/img/image_" + now + ".png"
    
    print(log) #debug, use tail on log file
        
    with open("log.txt", "a") as file:
        file.write(log)
        file.close()
    
    cam.capture(imgLoc)
    