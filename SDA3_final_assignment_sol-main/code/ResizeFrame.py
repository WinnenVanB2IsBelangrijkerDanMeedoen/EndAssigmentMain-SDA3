import cv2
 
def ResizeFrame():
    vidCapture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    frameWidth = int(vidCapture.get(3))
    frameHeight = int(vidCapture.get(4))

    def TrackBars():
        global show
        show = True
        pass

    cv2.namedWindow("SliderWindow",cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("xMax", "SliderWindow", frameWidth, frameWidth, TrackBars)
    cv2.createTrackbar("xMin", "SliderWindow", 0, frameWidth, TrackBars)
    cv2.createTrackbar("yMax", "SliderWindow", frameWidth, frameHeight, TrackBars)
    cv2.createTrackbar("yMin", "SliderWindow", 0, frameHeight, TrackBars)

    while(vidCapture.isOpened()):
        ret, frame = vidCapture.read()
        if ret == True:
            xMax = cv2.getTrackbarPos("xMax", 'SliderWindow')
            xMin = cv2.getTrackbarPos("xMin", 'SliderWindow')
            yMax = cv2.getTrackbarPos("yMax", 'SliderWindow')
            yMin = cv2.getTrackbarPos("yMin", 'SliderWindow')
            if xMax <= xMin:
                xMax = xMin + 50
            if yMax <= yMin:
                yMax = yMin + 50
            frame = frame[xMin:xMax, yMin:yMax]
            cv2.imshow("ResizeFrame", frame)
            key = cv2.waitKey(20)
            if key == ord("q"):
                print(xMin,":",xMax, '\t', yMin,":",yMax)
                cv2. destroyWindow("ResizeFrame")
                cv2. destroyWindow("SliderWindow")
                break
        else:
            break
    return frame, (xMin,xMax, yMin, yMax)

