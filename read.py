import cv2 as cv

#Reading images

img = cv.imread('Photos/cat.jpg')
# img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)

cv.waitKey(0) #wait for any key to be pressed to end program

#Reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read() #each frame is captured

    cv.imshow('Video', frame) #each frame is displayed

    if cv.waitKey(20) & 0xFF==ord('d'): #if key 'd' is pressed, breakout of loop
        break

capture.release()
cv.destroyAllWindows()