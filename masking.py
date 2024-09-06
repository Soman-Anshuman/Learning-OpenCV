import cv2 as cv
import numpy as np

#MASKING: Focusing on certain portions of image & removing unwanted parts

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8') # mask should be same size as original image
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)