#!/usr/bin/env python
import os, sys
import numpy as np
import cv2
from PIL import Image


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
    img = cv2.imread('/home/ecse-robotics-lab/Downloads/circles_rectangles.jpg',0)

    # Blur image
    img = cv2.medianBlur(img,5)

    # Convert to HSV
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    # Red range
    #lower_red = np.array([30,150,50])
    #upper_red = np.array([255,255,180])
    #mask = cv2.inRange(cimg, lower_red, upper_red)


    #res = cv2.bitwise_and(img,img, mask= mask)
    #cv2.imshow('res',res)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


    find_circles(img, cimg, 20, 50, 30, 0, 0)




# def listener():
# 	rospy.init_node('cylinderDetection', anonymous=True)
#     #Subscribe to image topic
# 	rospy.Subscriber("scan_objects/goal_markers", MarkerArray, callback)
# 	rospy.spin()

# if __name__ == '__main__':
# 	listener()

callback()