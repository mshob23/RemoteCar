#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from car import CarControls
from camera import VideoCamera
import time
import threading
import os

left = 2
right = 3
forward = 4
backward = 17

CControl = CarControls(left,right,forward, backward)

pi_camera = VideoCamera(flip=True) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/stopt', methods=['POST'])
def tStop():
    CControl.tStop()
    return('',204)

@app.route('/stopg', methods=['POST'])
def gStop():
    CControl.gStop()
    return('',204)

@app.route('/movel', methods=['POST'])
def leftTurn():
    CControl.left()
    return('',204)

@app.route('/mover', methods=['POST'])
def rightTurn():
    CControl.right()
    return('',204)

@app.route('/movef', methods=['POST'])
def foward():
    CControl.forward()
    return('',204)

@app.route('/moveb', methods=['POST'])
def backward():
    CControl.backward()
    return('',204)

@app.route('/moves', methods=['POST'])
def stop():
    CControl.stop()
    return('',204)

@app.route('/')
def index():
    return render_template('index.html', carC = CControl) #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


