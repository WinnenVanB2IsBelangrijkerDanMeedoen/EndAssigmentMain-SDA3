import cv2
import numpy as np
frame_width,frame_height = 1920,1080
vid_capture = cv2.VideoCapture(2, cv2.CAP_DSHOW)

fps = 60


color_list = [
        ['red', [0, 160, 70], [10, 250, 255]],
        ['green', [40, 50, 70], [70, 255, 255]],
        ['yellow', [15, 50, 70], [30, 255, 255]],
        ['blue', [100, 50, 70], [130, 255, 255]],
        ['red', [170, 50, 70], [180, 160, 255]],
    ]
coordinates = []

def get_color_hsv(frame, x, y):
    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV values at the specified pixel
    h, s, v = hsv_image[y, x]

    # Check if the color at the given coordinate falls within any of the specified ranges
    for color_name, lower, upper in color_list:
        lower_bound = np.array(lower)
        upper_bound = np.array(upper)
        pixel_color = np.array([h, s, v])
        if (lower_bound <= pixel_color).all() and (pixel_color <= upper_bound).all():
            return color_name
    return "Unknown"

def detect_shape(contour):
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    circularity = 4 * np.pi * cv2.contourArea(contour) / (cv2.arcLength(contour, True) ** 2)
    area = cv2.contourArea(contour)

    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        return "Quadrilateral"
    elif len(approx) == 5:
        return "Pentagon"
    elif len(approx) == 6:
        # Adjust these thresholds based on your specific case
        if circularity > 0.85 and 500 < area < 3000:
            return "Hexagon"
        else:
            return "Unknown"
    else:
        # Check if it's close to a circle
        (x, y), radius = cv2.minEnclosingCircle(contour)
        aspect_ratio = cv2.arcLength(contour, True) / (2 * np.pi * radius)
        if aspect_ratio > 0.9:
            return "Circle"
        else:
            return "Unknown"

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    frame = frame[140:400, 100:370]
    if ret:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray_frame, 80, 255, 0)

        cv2.imshow('tresh', thresh)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        frame_width, frame_height = frame.shape[1], frame.shape[0] #return witdh and height of the video
        border_margin = 10  # Adjust this margin as needed
        shape_count = {"Triangle": 0, "Quadrilateral": 0, "Pentagon": 0, "Hexagon": 0, "Circle": 0, "Unknown": 0}
        for contour in contours:
            area = cv2.contourArea(contour)
            if 5000> area > 400:
                if len(contour) > 0:
                    x, y = contour[0][0]
                    if border_margin <= x < frame_width - border_margin and border_margin <= y < frame_height - border_margin:
                        shape = detect_shape(contour)     
                        # Check if the shape is in the dictionary before incrementing
                        if shape in shape_count:
                            shape_count[shape] += 1
                        else:
                            shape_count["Unknown"] += 1

                        M = cv2.moments(contour)
                        if M["m00"] != 0:
                            cX = int(M["m10"] / M["m00"])
                            cY = int(M["m01"] / M["m00"])
                        else:
                            cX, cY = 0, 0                    
                        shape_data = {
                        'Type': shape,
                        'coordinates': (cY,cX)
                        }

                        coordinates.append(shape_data)
                        color = get_color_hsv(frame, cX, cY)
                        cv2.circle(frame, (cX, cY), 5, (0, 255, 255), -1) 
                        epsilon = 0.04 * cv2.arcLength(contour, True)
                        approx = cv2.approxPolyDP(contour, epsilon, True)
                        cv2.putText(frame, f"{color} {shape}", (approx[0][0][0]-40, approx[0][0][1]-8), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 255, 0), 1)
                        cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)       
        cv2.imshow("Image", frame)

        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    else:
        break
vid_capture.release()
cv2.destroyAllWindows()