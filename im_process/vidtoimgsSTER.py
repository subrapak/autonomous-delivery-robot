# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Arohan Subramonia 19/5/19

Code to convert video into sequence of images with accompanying timestamp txt file
"""



import cv2
import os


input_sourceL = "stereo1LHS.mp4"
input_sourceR = "stereo1RHS.mp4"
output_folder = "seq_0X"  
img_folderL = output_folder+"/image_0"  # image_0 for LHS, image_1 for RHS
img_folderR = output_folder+"/image_1"  # image_0 for LHS, image_1 for RHS
first_timestampL = 0
textfile = output_folder+"/times.txt"

if not os.path.exists(output_folder):   os.makedirs(output_folder)
if not os.path.exists(img_folderL):  os.makedirs(img_folderL)
if not os.path.exists(img_folderR):  os.makedirs(img_folderR)

f = open(textfile,"w+")
f.write("{:.6e}".format(0)+"\n")

#setup left video
capL = cv2.VideoCapture(input_sourceL)
no_framesL = int(capL.get(cv2.CAP_PROP_FRAME_COUNT))
input_fpsL = capL.get(cv2.CAP_PROP_FPS)
frameWidthL = capL.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeightL = capL.get(cv2.CAP_PROP_FRAME_HEIGHT)

#setup right video
capR = cv2.VideoCapture(input_sourceR)
no_framesR = int(capR.get(cv2.CAP_PROP_FRAME_COUNT))
input_fpsR = capR.get(cv2.CAP_PROP_FPS)
frameWidthR = capR.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeightR = capR.get(cv2.CAP_PROP_FRAME_HEIGHT)

#process left video - timestamps are based off this
for i in range(1,no_framesL+1):
    hasFrameL, frameL = capL.read()
    gray_frameL = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY) # required for KITTI
    n = str(i-1)
    imnameL = img_folderL+"/"+str(n.zfill(6))+".png"
    cv2.imwrite(imnameL,gray_frameL);
    #update
    cur_frameL = int(capL.get(cv2.CAP_PROP_POS_FRAMES))
    print("L "+str(int((cur_frameL/no_framesL)*100)))

    # creating times.txt
    pos_msL = capL.get(cv2.CAP_PROP_POS_MSEC)
    raw_timestampL = first_timestampL + (pos_msL/1000)
    cur_timestampL = round(raw_timestampL,6)
    sci_timestampL = ("{:.6e}".format(cur_timestampL))
    f.write(sci_timestampL+"\n")
 
f.close()

#process right video - timestamps are based off this
for i in range(1,no_framesR+1):
    hasFrameR, frameR = capR.read()
    gray_frameR = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY) # required for KITTI
    n = str(i-1)
    imnameR = img_folderR+"/"+str(n.zfill(6))+".png"
    cv2.imwrite(imnameR,gray_frameR);
    cur_frameR = int(capR.get(cv2.CAP_PROP_POS_FRAMES))
    print("R "+str(int((cur_frameR/no_framesR)*100)))