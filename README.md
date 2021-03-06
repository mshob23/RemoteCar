# A Raspberry Pi remote controlled car

The Flask site used to develop this project is heavily based on https://github.com/EbenKouao/pi-camera-stream-flask.

## Library dependencies
Install the following dependencies to create camera stream.

```
sudo apt-get update 
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python
sudo pip3 install RPi.GPIO

```

## The Car's wiring

The car is wired so that the left turn, right turn, forward, and backward are controlled by pin 2, 3, 4, and 17 respectively. Each pin is connected to a 100k Ohm resistor which connects to the base of a transistor that runs across the terminals of the button on the deconstructed controller for the car. The car can be seen in action here: https://youtu.be/g0C2OMWqAbU.
