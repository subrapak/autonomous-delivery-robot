#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:33:34 2019

@author: arohan
"""

import numpy as np
import cv2
import glob
import os

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001) # perhaps using some form of Kmeans clustering to solve calibration?

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# NB: 7,7 is for the NO. OF POINTS to detect. So in a chessboard of 8x8, you would detect 7x7 corners
objp_raw = np.zeros((7*7,3), np.float32)
objp_raw[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)

# multiply objp by the size of a square to get an answer in mm/m (measure in real life)
objp = objp_raw*23

# Arrays to store object points and image points from all the images
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane

images = glob.glob('*.jpeg') # imports any jpg images in the directory

output_folder = "drawn_imgs"

if not os.path.exists(output_folder):   os.makedirs(output_folder)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,7), None) #ret is the image, corners is the 'output edge map'
    
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria) #finding the edges. arguments are just various parameters
        imgpoints.append(corners2)
        
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,7), corners2, ret)
        cv2.imwrite((output_folder+"/img"+fname[3:-5]+".jpg"),img);


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)










      
    