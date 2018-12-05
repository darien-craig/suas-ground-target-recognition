import numpy as np
import cv2 as cv
import random

MIN_PIXEL_WIDTH = 28
MAX_PIXEL_WIDTH = 320


def addShapes(image, shapeNum):
	for i in range(shapeNum):
		width = (random()*(MAX_PIXEL_WIDTH-MIN_PIXEL_WIDTH))+MIN_PIXEL_WIDTH
		subImage = makeShapeImg(width)

def fileIn():
	input = glob.glob('backgrounds/*.jpg')
	for i in range(len(input)):
		name=input[i]
		image = cv.imread(name, 1)
		image = addShapes(image, 10)
		filename = "./input/{0}"
		cv.imwrite(filename.format(name.split('/')[1]), image)
