import numpy as np


def CoordinateCalculation(centerCoordinatesList):
    eenOfAndereWaardeOfZoIets = (100, 50)
    centerCoordinateRoboticarm = []
    print(centerCoordinatesList)
    for centerCoordinate in centerCoordinatesList:

        centerCoordinateRoboticarm.append(np.add(centerCoordinate, eenOfAndereWaardeOfZoIets))
        print(centerCoordinate)
        print(centerCoordinateRoboticarm)

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
