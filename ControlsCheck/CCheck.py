import RPi.GPIO as gpio
import time 

gpio.setmode(gpio.BCM)
gpio.setup(2,gpio.OUT)
gpio.setup(3,gpio.OUT)
gpio.setup(4,gpio.OUT)
gpio.setup(17,gpio.OUT)

gpio.output(2, gpio.LOW)
gpio.output(3, gpio.LOW)
gpio.output(4, gpio.LOW)
gpio.output(17, gpio.LOW)

gpio.output(2, gpio.HIGH)
time.sleep(1)
gpio.output(2, gpio.LOW)
time.sleep(1)
    
gpio.output(3, gpio.HIGH)
time.sleep(1)
gpio.output(3, gpio.LOW)
time.sleep(1)
    
gpio.output(4, gpio.HIGH)
time.sleep(1)
gpio.output(4, gpio.LOW)
time.sleep(1)
 
gpio.output(17, gpio.HIGH)
time.sleep(1)
gpio.output(17, gpio.LOW)
time.sleep(1)
