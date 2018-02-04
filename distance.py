import numpy
import sys
import os
import glob
import code
import math

def importOBJ(path):
	with open(path, 'r') as f:
		l = f.readlines()
		emptyArray = []
		for each in l:
			if each[0] == 'v':
				emptyArray.append(each.strip()[2:].split(" "))
		aa = numpy.asarray(emptyArray, dtype=float)
		return aa

def findNearestDistance(point, listNeighbors):
	minDistance = sys.float_info.max
	
	for each in listNeighbors:
		neighPoint = each
		distance = math.sqrt((point[0] - neighPoint[0])**2 + (point[1] - neighPoint[1])**2 + (point[2] - neighPoint[2])**2)
		if distance <= minDistance:
			minDistance = distance
		
	return minDistance

def importAsciiAmira(path):
	with open(path, 'r') as f:
		collect = False
		l = f.readlines()
		emptyArray = []
		for each in l:
			if each.strip() == '':
				continue
			if collect:
				e = each.strip().split(" ")
				e = [float(i) for i in e]
				emptyArray.append(e)
			if each.strip() == '@1':
				collect = True

		aa = numpy.asarray(emptyArray)
		return aa


# accept input from user to paths of these files
pointsPath = sys.argv[1]
activeZonePath = sys.argv[2]
xVoxelDim = float(sys.argv[3])
yVoxelDim = float(sys.argv[4])
zVoxelDim = float(sys.argv[5])



points = importAsciiAmira(pointsPath)
activeZonePoints = importOBJ(activeZonePath)

print(points[0])
points = [[p[0] * xVoxelDim, p[1] * yVoxelDim, p[2] * zVoxelDim] for p in points]
print(points[0])



returnList = []
for each in points:
	minDistance = findNearestDistance(each, activeZonePoints)
	print(minDistance)
	returnList.append(minDistance)
	
numpy.savetxt("minDistances.csv", returnList, delimiter=",")









