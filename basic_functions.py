import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blurring
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image
#dilating is done using a structuring element(in this case, the canny edges we found)
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding (removing noise)
#here we are using dilated image and try to retrieve the original canny image
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)