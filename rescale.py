import cv2 as cv

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Resized_image = rescaleFrame(img)
# cv.imshow('Image Resized', Resized_image)

def changeRes(width, height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

#Reading videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()