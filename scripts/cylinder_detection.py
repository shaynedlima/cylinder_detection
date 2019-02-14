#!/usr/bin/env python
import os, sys
import numpy as np
import cv2
import matplotlib.image as mpimg


def find_circles(red_circles, img, cimg, minDist, param1, param2, min_rad, max_rad):

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
        

        if(red_circles):
            print "Red Cylinder " + str(i) + ":"
            print "Centre: (" + str(i[0]) + "," + str(i[1]) +")"
            print "Radius: " + str(i[2])
        else:
            print "Blue Cylinder " + str(i) + ":"
            print "Centre: (" + str(i[0]) + "," + str(i[1]) +")"
            print "Radius: " + str(i[2])


    cv2.imshow('cimg',cimg)
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
    mask1 = cv2.inRange(cimg, lower_blue, upper_blue)


    # define range of red color in HSV
    lower_red = np.array([352,50,110])
    upper_red = np.array([255,255,130])
    # Threshold the HSV image to get only red colors
    mask2 = cv2.inRange(cimg, lower_red, upper_red)


    # Bitwise-AND mask and original image
    blue_objects = cv2.bitwise_and(img,img, mask= mask1)
    red_objects = cv2.bitwise_and(img,img, mask= mask2)

    # Converting image to greyscale
    grey = cv2.cvtColor(blue_objects,cv2.COLOR_BGR2GRAY)


    #cv2.imshow('res',res)
    #cv2.imshow('grey',grey)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #img = cv2.medianBlur(img,5)
    #cimg = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    # find_circles(greyscale_img, img_to_draw_on, minDist, parma1, param2, min_rad, max_rad)
    find_circles(0, grey, blue_objects, 20, 50, 30, 25, 100)




# def listener():
# 	rospy.init_node('cylinderDetection', anonymous=True)
#     #Subscribe to image topic
# 	rospy.Subscriber("scan_objects/goal_markers", MarkerArray, callback)
# 	rospy.spin()

# if __name__ == '__main__':
# 	listener()

callback()