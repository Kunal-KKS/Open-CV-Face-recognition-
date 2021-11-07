import cv2 as cv
def rescaling(frame,scale=0.50):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimentions=(width,height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)
#img=cv.imread("im1.jpg")
#cv.imshow("dog",img)
video=cv.VideoCapture("video1.mp4")
while True:
    istrue,frame=video.read()
    rescaled_video=rescaling(frame)
    cv.imshow("dog1",frame)
    cv.imshow("DOG2",rescaled_video)
    if cv.waitKey(20) & 0xff==ord('q'):
      break
video.release()
cv.destroyAllWindows()

cv.waitKey(0)