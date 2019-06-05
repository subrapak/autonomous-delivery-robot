# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Arohan Subramonia 19/5/19

Code to convert video into sequence of images with accompanying timestamp txt file
"""



import cv2
import os


input_source = "pitest7.mp4"
output_folder = input_source[:-4]+"_test"
img_folder = output_folder+"/rgb"
first_timestamp = 1305031102.175304     # 1305031102.175304 based on TUM1 dataset #0 for KITTI
textfile = output_folder+"/rgb.txt"

if not os.path.exists(output_folder):   os.makedirs(output_folder)
if not os.path.exists(img_folder):  os.makedirs(img_folder)

f = open(textfile,"w+")
f.write("# color images\n")  # for TUM
f.write("# file: '"+input_source[:-4]+"' \n")  # for TUM
f.write("# timestamp filename\n")  # for TUM

cap = cv2.VideoCapture(input_source)
no_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

input_fps = cap.get(cv2.CAP_PROP_FPS)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
   

for i in range(1,no_frames+1):
    hasFrame, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # required for KITTI
    cur_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    pos_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
    raw_timestamp = first_timestamp + (pos_ms/1000)
    cur_timestamp = round(raw_timestamp,6)
    # sci_timestamp = ("{:.6e}".format(cur_timestamp))
    f.write("%f rgb/%f.png\n" % (cur_timestamp, cur_timestamp))  # for TUM
    print(str(int((cur_frame/no_frames)*100)))
    imname = img_folder+"/%f.png" %(cur_timestamp) # for TUM
    n = str(i-1)
    cv2.imwrite(imname,gray_frame);
 
f.close()
