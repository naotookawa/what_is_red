import cv2
# import time
# import math
import red
# import blue
# import green


def main():
    path = input('select mp4! >>> ')
    if path == 'iphone':
        cap = cv2.VideoCapture(0)
    elif path == 'pc':
        cap = cv2.VideoCapture(1)
    else:
        cap = cv2.VideoCapture(path + '.mp4')
    
    if cap.isOpened() == False:
        print('Error opening video stream or file')
        exit()
    
    # currnet_time = time.time()


    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        result_red = red.red_hsv(frame)
        # result_blue = blue.blue_hsv(frame)
        # result_green = green.green_hsv(frame)
        

        cv2.imshow('Original Frame', frame)
        # cv2.imshow('Red Extracted Frame', result_red) if (math.ceil(time.time() - currnet_time) % 3 == 0) else cv2.imshow('Blue Extracted Frame', result_blue) if (math.ceil(time.time() - currnet_time) % 3 == 1) else cv2.imshow('Green Extracted Frame', result_green)
        # if (math.ceil(time.time() - currnet_time) % 3 == 0):
        #     cv2.imshow('Red Extracted Frame', result_red)
        #     cv2.destroyAllWindows()
        # elif (math.ceil(time.time() - currnet_time) % 3 == 1):
        #     cv2.imshow('Blue Extracted Frame', result_blue)
        #     cv2.destroyAllWindows()
        # else:
        #     cv2.imshow('Green Extracted Frame', result_green)
        #     cv2.destroyAllWindows()

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        cv2.imshow('Red Extracted Frame', result_red)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()