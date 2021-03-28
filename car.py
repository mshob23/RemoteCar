import RPi.GPIO as gpio
import time 

class CarControls:

    def __init__(self, left, right, forward, backward):
        self.lNum = left
        self.rNum = right
        self.fNum = forward
        self.bNum = backward

        gpio.setmode(gpio.BCM)
        gpio.setup(left,gpio.OUT)
        gpio.setup(right,gpio.OUT)
        gpio.setup(forward,gpio.OUT)
        gpio.setup(backward,gpio.OUT)

        self.stop()

    def stop(self):
        gpio.output(self.lNum, gpio.LOW)
        gpio.output(self.rNum, gpio.LOW)
        gpio.output(self.fNum, gpio.LOW)
        gpio.output(self.bNum, gpio.LOW)
    
    def tStop(self):
        gpio.output(self.lNum, gpio.LOW)
        gpio.output(self.rNum, gpio.LOW)

    def gStop(self):
        gpio.output(self.fNum, gpio.LOW)
        gpio.output(self.bNum, gpio.LOW)

    def left(self):
        gpio.output(self.rNum, gpio.LOW)
        gpio.output(self.lNum, gpio.HIGH)

    def right(self):
        gpio.output(self.lNum, gpio.LOW)
        gpio.output(self.rNum, gpio.HIGH)

    def forward(self):
        gpio.output(self.bNum, gpio.LOW)
        gpio.output(self.fNum, gpio.HIGH)

    def backward(self):
        gpio.output(self.fNum, gpio.LOW)
        gpio.output(self.bNum, gpio.HIGH)

