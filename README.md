﻿# vesicleDistanceForMPFI
 
 1. navigate to directory holding this script plus needed data files
 2. run this command:
 
 python distance.py [path_to_landmark_asciiFile] [path_to_activeZoneOBJ] [xVoxDim] [yVoxDim] [zVolDim]
 
 ex: python distance.py vesiclePoints.landmarkAscii activeZone.obj 1.0 1.0 1.0
 
 If you use the voxel dimension ration modifier be sure to but the float version of the number, not just and integer.
