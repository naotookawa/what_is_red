import cv2
import numpy as np
import time

image = cv2.imread('red.jpg')

def green_hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



    lower_green = np.array([20, 150, 0])
    upper_green = np.array([80, 255, 255])


    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    result[green_mask > 0] = image[green_mask > 0] 

    return result

if __name__ == '__main__':
    result = green_hsv(image)

    start_time = time.time()

    while True:
        cv2.imshow('Original Image', image)
        cv2.imshow('Red Extracted Image', result)

        if (cv2.waitKey(100) & 0xFF == ord('q')) | (time.time() - start_time > 3):
            break
        

    cv2.destroyAllWindows()
    print('quit')