def CoordinateCalculation(centerCoordinatesList):
    XAdjustment = -3 #correction X postion of the nose
    YAdjjustment = 12 #correctioin Y postion of the nose
    scaleFactor = 0.725 #Robot lengt of picup area divided by the camara lengt of picup area 
    MaxX = 300 #maximum X postion of the pickup area
    maxY = 225 #maximum Y postion of the picup are
    centerCoordinateRoboticarm = []
    print(centerCoordinatesList)
    for centerCoordinate in centerCoordinatesList:
        X, Y = centerCoordinate
        #transfrom the camare coordinate to the robot coordinates
        X *= scaleFactor 
        Y *= scaleFactor 
        #adjust coordinates to the actual position
        X = MaxX - X + XAdjustment  
        Y = maxY - Y + YAdjjustment 
        centerCoordinate = (Y, X)
        centerCoordinateRoboticarm.append(centerCoordinate)
    return centerCoordinateRoboticarm
