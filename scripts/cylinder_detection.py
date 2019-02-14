#!/usr/bin/env python
import os, sys
import numpy as np
import cv2
import matplotlib.image as mpimg


def find_circles(img, cimg, minDist, param1, param2, min_rad, max_rad):

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist,
                                param1=param1,param2=param2,minRadius=min_rad,maxRadius=max_rad)

    circles = np.uint16(np.around(circles))
    print circles
    for i in circles[0,:]:
        # draw the outer circle
        #cv2.circles(image_to_draw_on, centre_coords, radius, rgb, pixel thickness)
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def callback():

    # Read image
    img = mpimg.imread(r'/home/ecse-robotics-lab/cylinder_images/1.jpg',0)

    

    # Convert to HSV
    cimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(cimg, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    # Converting image to greyscale
    grey = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)


    #cv2.imshow('res',res)
    #cv2.imshow('grey',grey)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #img = cv2.medianBlur(img,5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    find_circles(grey, res, 20, 50, 30, 20, 150)




# def listener():
# 	rospy.init_node('cylinderDetection', anonymous=True)
#     #Subscribe to image topic
# 	rospy.Subscriber("scan_objects/goal_markers", MarkerArray, callback)
# 	rospy.spin()

# if __name__ == '__main__':
# 	listener()

callback()