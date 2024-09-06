import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

#AVERAGING
average = cv.blur(img, (3,3)) #average out the surrounding pixels
cv.imshow('Average Blur', average)

#GAUSSIAN BLUR
#assign weights to surrounding pixels & average out products of weights with pixels
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

#MEDIAN BLUR
median = cv.medianBlur(img, 3) #median of surrounding pixels
cv.imshow('Median BLur', median)

#BILATERAL
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)