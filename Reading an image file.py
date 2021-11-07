import cv2 as cv
# img = cv.imread('im2.jfif')
# cv.imshow('Dog', img)
# cv.waitKey(0)
video=cv.VideoCapture('video1.mp4')
while True:
    istrue,frame=video.read()
    cv.imshow("video",frame)
    if cv.waitKey(20) & 0xFF==ord('f'):
        break
video.release()
cv.destroyAllWindows()