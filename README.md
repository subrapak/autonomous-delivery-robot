# autonomous-delivery-robot

This was the final year project for the Mechanical Engineering (MEng) course at Imperial College London.

# Abstract

The recent rise of automated processes has led to an explosion in appetite for robotics in industry. However, due to the high costs involved in developing autonomous robots, education into this field is not very accessible despite this rising interest. The following project therefore outlines the design, development and testing for the electronics and software of an autonomous delivery robot, which can be used as an educational tool for learning. A Raspberry Pi was used with rotary encoders for odometry data collection and the Camera Module v2 as the range measurement device in a VisualSLAM implementation. ORB-SLAM2 was the chosen SLAM algorithm, with a monocular RGB implementation due to hardware constraints. Testing on TUM and KITTI datasets identified strengths and weaknesses of ORB-SLAM2’s monocular and stereo implementations. Monocular sequences were parsed at a minimum of 0.125s per frame (KITTI 06), and stereo sequences at a minimum of 0.484s per frame (KITTI 03), whilst monocular testing on self-recorded sequences achieved speeds of 0.245s per frame (iPhone) and 0.259s per frame (PiCam). The project met the technical objectives as well as the monetary constraints, proving that a low-cost and easy to understand test robot can indeed be developed as a tool for education on SLAM, robotics and autonomous systems.

# Dependencies and Software

## For the Raspberry Pi: 

  * Etcher: https://www.balena.io/etcher/
  
  * Microsoft Remote Desktop: https://www.microsoft.com/en-us/p/microsoft-remote-desktop/9wzdncrfj3ps?activetab=pivot:overviewtab
  
  * Raspbian Stretch (with Desktop): https://www.raspberrypi.org/downloads/raspbian/
  
## SLAM Algorithm

  * ORB-SLAM2 was used as the SLAM Algorithm, available at: https://github.com/raulmur/ORB_SLAM2
  
  * Ubuntu 18.04 was the OS used, on a MacBook Pro 2011. This was done by creating a virtual machine using VirtualBox: https://www.virtualbox.org/
  
# Description of contents

**calib_test**
 * drawn_imgs, iPhone_chessboards, calibrate_camera.py is required for camera calibration
 * pins_test.py is to test the functionality of GPIO pins on the Raspberry Pi
 * calibrate_encoders.py is to calibrate pulse counts for the encoders
 * ultrasonic_test.py is to test accuracy of the ultrasonic sensors

**headers**
 * These contain the custom written header files for the LCD, encoders, motors and ultrasonic sensors. [RPLCD](https://pypi.org/project/RPLCD/) is required for the LCD and the PiCamera has to be initialized ([instructions available here](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera))
 
**im_process**

* This contains an example video, and custom written scripts to convert a video into a sequence of images in the TUM and KITTI format.

**main.py** contains the main robot control loop and **pi_compiled_07.mp4** is an example video of the project in action.

[![EXAMPLE VIDEO](http://img.youtube.com/vi/https://youtu.be/iKiXkS0y30M/0.jpg)](http://www.youtube.com/watch?v=https://youtu.be/iKiXkS0y30M)


 
 
 
