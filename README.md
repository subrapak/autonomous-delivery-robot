# autonomous-delivery-robot

This was the final year project for the Mechanical Engineering (MEng) course at Imperial College London.

# Abstract

The recent rise of automated processes has led to an explosion in appetite for robotics in industry. However, due to the high costs involved in developing autonomous robots, education into this field is not very accessible despite this rising interest. The following project therefore outlines the design, development and testing for the electronics and software of an autonomous delivery robot, which can be used as an educational tool for learning. A Raspberry Pi was used with rotary encoders for odometry data collection and the Camera Module v2 as the range measurement device in a VisualSLAM implementation. ORB-SLAM2 was the chosen SLAM algorithm, with a monocular RGB implementation due to hardware constraints. Testing on TUM and KITTI datasets identified strengths and weaknesses of ORB-SLAM2’s monocular and stereo implementations. Monocular sequences were parsed at a minimum of 0.125s per frame (KITTI 06), and stereo sequences at a minimum of 0.484s per frame (KITTI 03), whilst monocular testing on self-recorded sequences achieved speeds of 0.245s per frame (iPhone) and 0.259s per frame (PiCam). The project met the technical objectives as well as the monetary constraints, proving that a low-cost and easy to understand test robot can indeed be developed as a tool for education on SLAM, robotics and autonomous systems.

# Dependencies and Software

* For the Raspberry Pi:
- Etcher
