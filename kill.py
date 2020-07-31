#!/usr/bin/env python3
from ctypes import *
from adafruit_servokit import ServoKit
import Jetson.GPIO as nano
import numpy as np
import math
import random
import os
import cv2 
import time
import darknet         

def convertBack(x, y, w, h):
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax

def cvDrawBoxes(detections, img, height, width, kit):
    global lastKnown
    for detection in detections:
        x, y, w, h = detection[2][0],\
            detection[2][1],\
            detection[2][2],\
            detection[2][3]
        print("X: %s, Y: %s\n" % (x, y))
        xmin, ymin, xmax, ymax = convertBack(
            float(x), float(y), float(w), float(h))
        pt1 = (xmin, ymin)
        pt2 = (xmax, ymax)
        cv2.rectangle(img, pt1, pt2, (50,168,145), 3)
        cv2.putText(img,
                    detection[0].decode() +
                    " [" + str(round(detection[1] * 100, 2)) + "]",
                    (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    [255,255,255], 2)

        x_angle = int(np.interp(x, [0,608], [110,30]))
        y_angle = int(np.interp(y, [0,608], [55,115]))
        kit.servo[15].angle = x_angle
        kit.servo[11].angle = y_angle
        if abs(lastKnown[0] - x_angle) <= 5:
            if abs(lastKnown[1] - y_angle) <= 5:
                print("\n\n\t\tFIRE!\n\n")
                #nano.output(solenoid, nano.HIGH)
                #time.sleep(.5)		#solenoid burst time
                #nano.output(solenoid, nano.LOW)
        lastKnown = (x_angle, y_angle)
        print("X Angle: %s, Y Angle: %s\n" % (x_angle, y_angle))
    return img

def gstreamer_pipeline(
    capture_width = 3820,
    capture_height = 2464,
    display_width = 960,
    display_height = 616,
    framerate=21,
    flip_method=0
    ):
	return(
    "nvarguscamerasrc ! "
    "video/x-raw(memory:NVMM), "
    "width=(int)%d, height=(int)%d, "
    "format=(string)NV12, framerate=(fraction)%d/1 ! "
    "nvvidconv flip-method=%d ! "
    "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! appsink"
	    % (capture_width,capture_height,framerate,flip_method,display_width,display_height)
	)

netMain = None
metaMain = None
altNames = None
solenoid = 'SPI2_CS0'			#nano mode is TEGRA_SOC
lastKnown = (90,90)

def YOLO():

    global metaMain, netMain, altNames
    
    nano.setup(solenoid, nano.OUT, initial=nano.LOW)

    kit = ServoKit(channels=16)
    init_angle = 80
    kit.servo[15].angle=init_angle
    kit.servo[11].angle=init_angle

    detections = []

    configPath = "/home/naivoder/darknet/feeder_1c.cfg"
    weightPath = "/home/naivoder/darknet/feeder_1c_best.weights"
    metaPath = "/home/naivoder/darknet/feeder_1c.data"

    if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    if netMain is None:
        netMain = darknet.load_net_custom(configPath.encode(
            "ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass
   
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

    darknet_image = darknet.make_image(darknet.network_width(netMain),
                                    darknet.network_height(netMain),3)
    while cv2.waitKey(1) < 0:
        prev_time = time.time()
        has_frame, frame = cap.read()
        if not has_frame:
            cv2.waitKey(3000)
            break
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb,
                                   (darknet.network_width(netMain),
                                    darknet.network_height(netMain)),
                                   interpolation=cv2.INTER_LINEAR)

        darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes())
        detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.30) #confidence threshold 
        image = cvDrawBoxes(detections, frame_resized, frame_height, frame_width, kit)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #print(1/(time.time()-prev_time))
        cv2.imshow('Turret Cam', image)
        detections = []

    cap.release()

if __name__ == "__main__":
    YOLO()
