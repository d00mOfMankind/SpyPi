# SpyPi

## To view images on terminal

- Install `fbi`
- Run `fbi [file name]`
- Press enter to quit

## To run program

- Make sure dependencies are installed (first time)
- Run `python detector.py`

## Pin configuration

(With the sensor facing away from you and the sensitivity controls at the bottom.)
The pins go (from left to right) ground, output, power(5V).  
On the pi with ethernet facing down:
- put power in pin 4
- put ground in pin 6
- put output in pin 12

The pins then should run like this.  
1  2  
3  4 <-- pwr  
5  6 <-- gnd  
7  8  
9  10  
11 12 <-- output  
towards S-Video
