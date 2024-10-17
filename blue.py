import cv2
import numpy as np
import time

image = cv2.imread('red.jpg')

def blue_hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([120, 255, 255])


    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    result[blue_mask > 0] = image[blue_mask > 0] 

    return result

if __name__ == '__main__':
    result = blue_hsv(image)

    start_time = time.time()

    while True:
        cv2.imshow('Original Image', image)
        cv2.imshow('Red Extracted Image', result)

        if (cv2.waitKey(100) & 0xFF == ord('q')) | (time.time() - start_time > 3):
            break
        

    cv2.destroyAllWindows()
    print('quit')