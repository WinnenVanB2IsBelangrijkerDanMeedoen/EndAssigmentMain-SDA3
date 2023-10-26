import cv2
import numpy as np
import ObjectDetection
vidCapture = cv2.VideoCapture(2, cv2.CAP_DSHOW)

def shapeDetection(contour):
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    #how many conrners does the contour have?
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        return "Quadrilateral"
    elif len(approx) == 5:    
        return "Pentagon"
    elif len(approx) == 6:
        return "Hexagon"
    else:   #when the contour has no corners, it is a cirlce
        (x,y), radius = cv2.minEnclosingCircle(contour)
        aspectRatio = cv2.arcLength(contour, True)/(2*np.pi*radius)
        if aspectRatio > 0.8:
            return "Circle"
        else:
            return "Unknown"

while vidCapture.isOpened():
    ObjectDetection()
    shape = shapeDetection(contour)
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.putText(frame, f"{color} {shape}", (approx[0][0][0]-40, approx[0][0][1]-8), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 0), 1)
    cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    cv2.imshow("image", frame)

    #close program wheb q key is pressed
    key = cv2.waitKey(20)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
