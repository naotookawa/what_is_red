import cv2
import numpy as np
import time

image = cv2.imread('red.jpg')

def red_hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



    lower_red1 = np.array([0, 150, 0])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 150, 0])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = mask1 | mask2

    # print(np.unique(red_mask[0]))

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    result[red_mask > 0] = image[red_mask > 0] 

    return result

if __name__ == '__main__':
    result = red_hsv(image)

    start_time = time.time()

    while True:
        cv2.imshow('Original Image', image)
        cv2.imshow('Red Extracted Image', result)

        if (cv2.waitKey(100) & 0xFF == ord('q')) | (time.time() - start_time > 3):
            break
        

    cv2.destroyAllWindows()
    print('quit')