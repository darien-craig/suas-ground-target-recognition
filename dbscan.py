from sklearn.cluster import DBSCAN as dbscan
import numpy as np
import cv2 as cv
import numpy as np
import time

def runCluster(image, eps):
	keypoints = getKeypoints(image)
	clusters = dbscan(eps=eps, min_samples=10).fit(keypoints)
	n_clusters = len(set(clusters.labels_))
	print(n_clusters)
	return getBounds(clusters, keypoints)

def getKeypoints(image):
	orb = cv.FastFeatureDetector_create()
	keypoints = orb.detect(image, None)
	points=[keys.pt for keys in keypoints]
	return points

def getBounds(clusters, keypoints):
	groupedPoints = {}
	bounds = []
	for i, group in enumerate(clusters.labels_):
		if group == -1:
			continue
		if group not in groupedPoints:
			groupedPoints[group] = []
		groupedPoints[group].append(keypoints[i])
	for group in groupedPoints:
		data = np.array(groupedPoints[group]).astype(int)
		x = data[:, 0]
		y = data[:, 1]
		bounds.append([(x.max(), y.max()), (x.min(), y.min())])
	return bounds

def plotFrame(image, bounds):
	for i in bounds:
		cv.rectangle(image, i[0], i[1], (0,0,255), 3)
	cv.imshow("window", image)

print('loading video source...')
try:
    #uses built-in webcam for capture device
    cap = cv.VideoCapture(0)
    time.sleep(2)
    if cap is None or cap == None:
        raise IOError
except IOError:
    sys.exit('video load failure')

while(True):
	ret, frame = cap.read()
	bounds = runCluster(frame, 10)
	plotFrame(frame, bounds)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
