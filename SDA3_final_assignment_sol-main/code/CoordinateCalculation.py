def CoordinateCalculation(centerCoordinatesList):


    XAdjustment = -3
    YAdjjustment = 12
    scaleFactor = 0.725
    MaxX = 300
    maxY = 225
    centerCoordinateRoboticarm = []
    print(centerCoordinatesList)
    for centerCoordinate in centerCoordinatesList:
        X, Y = centerCoordinate
        X *= scaleFactor
        Y *= scaleFactor
        X = MaxX - X + XAdjustment
        Y = maxY - Y + YAdjjustment
        centerCoordinate = (Y, X)
        centerCoordinateRoboticarm.append(centerCoordinate)
        print(centerCoordinate)
        print(centerCoordinateRoboticarm)
    return centerCoordinateRoboticarm

#centerList, collorList, frame = ObjectDetection(ResizeFrame())
#cv2.imshow('frame', frame)
#CoordinateCalculation(centerList)
#cv2.waitKey()
#cv2.destroyAllWindows()
 
       

#Y 145, 265
#x = 95, 180
#85 x
#120 y
#max x = 180
