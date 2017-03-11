# Face Tracking Example
#
# This example shows off using the keypoints feature of your OpenMV Cam to track
# a face after it has been detected by a Haar Cascade. The first part of this
# script finds a face in the image using the frontalface Haar Cascade.
# After which the script uses the keypoints feature to automatically learn your
# face and track it. Keypoints can be used to automatically track anything.
#
# NOTE: LOTS OF KEYPOINTS MAY CAUSE THE SYSTEM TO RUN OUT OF MEMORY!

import sensor, time, image
from pyb import I2C
from pyb import LED
#red in openmv is green in mvd: LED(1)
#green in openmv is blue in mvd:LED(2)
#LED(3) doesn't work in MVD, red(led(3)) in MVD is always on

green_led = LED(1)
blue_led = LED(2)

#init IIC as master
i2c = I2C(2, I2C.MASTER) # The i2c bus must always be 2.


# Normalized keypoints are not rotation invariant...
NORMALIZED=False
# Keypoint extractor threshold, range from 0 to any number.
# This threshold is used when extracting keypoints, the lower
# the threshold the higher the number of keypoints extracted.
KEYPOINTS_THRESH=30
# Keypoint-level threshold, range from 0 to 100.
# This threshold is used when matching two keypoint descriptors, it's the
# percentage of the distance between two descriptors to the max distance.
# In other words, the minimum matching percentage between 2 keypoints.
MATCHING_THRESH=70

#greenled = pyb.LED(1)
#blueled = pyb.LED(2)
# Reset sensor
sensor.reset()

# Sensor settings
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.HQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)

# Skip a few frames to allow the sensor settle down
# Note: This takes more time when exec from the IDE.
#for i in range(0, 10):
#    img = sensor.snapshot()
#    img.draw_string(0, 0, "Please wait...")

# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
face_cascade = image.HaarCascade("frontalface", stages=25)
print(face_cascade)

# First set of keypoints
hzy_kpts = None
hjf_kpts = None
hmy_kpts = None
sf_kpts = None

# load faces!
img_hjf = image.Image("/hjfface2-hqvga.bmp",copy_to_fb=True)
#img = img2
#img.draw_string(0, 0, "Looking for a face...")
    # Find faces
hjf_objects = img_hjf.find_features(face_cascade, threshold=0.7, scale=1.5)
if hjf_objects:
        print("he jianfei's face loaded!")
        # Expand the ROI by 11 pixels in each direction (half the pattern scale)
        hjf_face = (hjf_objects[0][0]-31, hjf_objects[0][1]-31,hjf_objects[0][2]+31*2, hjf_objects[0][3]+31*2)
        # Extract keypoints using the detect face size as the ROI
        hjf_kpts = img_hjf.find_keypoints(threshold=10, scale_factor=1.3, max_keypoints=100, normalized=True)
        # Draw a rectangle around the first face
        #img.draw_rectangle(objects[0])

# Draw keypoints
print("he jianfei's key points")
print(hjf_kpts)
#img.draw_keypoints(kpts1, size=12)
#time.sleep(1000)
#img_pic.clear()

img_sf = image.Image("/sfface2-hqvga.bmp",copy_to_fb=True)
#img = img2
#img.draw_string(0, 0, "Looking for a face...")
    # Find faces
sf_objects = img_sf.find_features(face_cascade, threshold=0.7, scale=1.5)
if sf_objects:
        print("sun fang's face loaded!")
        # Expand the ROI by 11 pixels in each direction (half the pattern scale)
        sf_face = (sf_objects[0][0]-31, sf_objects[0][1]-31,sf_objects[0][2]+31*2, sf_objects[0][3]+31*2)
        # Extract keypoints using the detect face size as the ROI
        sf_kpts = img_sf.find_keypoints(threshold=10, scale_factor=1.3, max_keypoints=100, normalized=True)
        # Draw a rectangle around the first face
        #img.draw_rectangle(objects[0])

# Draw keypoints
print("sun fang's key points")
print(sf_kpts)
#img.draw_keypoints(kpts1, size=12)
time.sleep(1000)
#img_pic.clear()

img_hzy = image.Image("/hzyface3-hqvga.bmp",copy_to_fb=True)
#img = img2
#img.draw_string(0, 0, "Looking for a face...")
    # Find faces
hzy_objects = img_hzy.find_features(face_cascade, threshold=0.7, scale=1.5)
if hzy_objects:
        print("he zhiyuan's face loaded!")
        # Expand the ROI by 11 pixels in each direction (half the pattern scale)
        hzy_face = (hzy_objects[0][0]-31, hzy_objects[0][1]-31,hzy_objects[0][2]+31*2, hzy_objects[0][3]+31*2)
        # Extract keypoints using the detect face size as the ROI
        hzy_kpts = img_hzy.find_keypoints(threshold=10, scale_factor=1.3, max_keypoints=100, normalized=True)
        # Draw a rectangle around the first face
        #img.draw_rectangle(objects[0])

            # Expand the ROI by 31 pixels in every direction
            #face = (objects[0][0]-31, objects[0][1]-31,objects[0][2]+31*2, objects[0][3]+31*2)
            # Extract keypoints using the detect face size as the ROI
            #kpts1 = img.find_keypoints(scale_factor=1.2, max_keypoints=100, roi=face)
            # Draw a rectangle around the first face
            #img.draw_rectangle(objects[0])

# Draw keypoints
print("he zhiyuan's key points")
print(hzy_kpts)
#img.draw_keypoints(kpts1, size=12)
time.sleep(1000)

#img_pic.clear()

img_hmy = image.Image("/hmyface2-hqvga.bmp",copy_to_fb=True)
#img = img2
#img.draw_string(0, 0, "Looking for a face...")
    # Find faces
hmy_objects = img_hmy.find_features(face_cascade, threshold=0.7, scale=1.5)
if hmy_objects:
        print("he muyuan's face loaded!")
        # Expand the ROI by 11 pixels in each direction (half the pattern scale)
        hmy_face = (hmy_objects[0][0]-31, hmy_objects[0][1]-31,hmy_objects[0][2]+31*2, hmy_objects[0][3]+31*2)
        # Extract keypoints using the detect face size as the ROI
        hmy_kpts = img_hmy.find_keypoints(threshold=10, scale_factor=1.3, max_keypoints=100, normalized=True)
        # Draw a rectangle around the first face
        #img.draw_rectangle(objects[0])

# Draw keypoints
print("he muyuan's key points")
print(hmy_kpts)
#img.draw_keypoints(kpts1, size=12)
time.sleep(1000)

# FPS clock
clock = time.clock()
c=[0,0,0,0,0]# 1-4:number of matchpoints for hjf,sf,hzy,hmy;0:temp value
i=[0,0,0,0,0]# 1-4:times of match for hjf,sf,hzy,hmy;0:temp value


sensor.reset()
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.GRAYSCALE)

while (True):
    clock.tick()
    img = sensor.snapshot()
    img_objects = img.find_features(face_cascade, threshold=0.7, scale=1.5)
    if img_objects:
            print("a new face detected!")
            # Draw a rectangle around the first face
            #img.draw_rectangle(img_objects[0])
            # Expand the ROI by 11 pixels in each direction (half the pattern scale)
            img_face = (img_objects[0][0]-31, img_objects[0][1]-31,img_objects[0][2]+31*2, img_objects[0][3]+31*2)
            # Extract keypoints using the detect face size as the ROI
            kpts2 = img.find_keypoints(threshold=10, scale_factor=1.3, max_keypoints=100, normalized=True)
    # Extract keypoints using the detect face size as the ROI
    #kpts2 = img.find_keypoints(threshold=KEYPOINTS_THRESH, normalized=NORMALIZED)

            if (kpts2):
                img.draw_rectangle(img_objects[0])
                print("keypoints found!")
                # Match the first set of keypoints with the second one
                c1 = image.match_descriptor(hjf_kpts, kpts2,threshold=60)
                c2 = image.match_descriptor(sf_kpts, kpts2,threshold=60)
                c3 = image.match_descriptor(hzy_kpts, kpts2,threshold=60)
                c4 = image.match_descriptor(hmy_kpts, kpts2,threshold=60)
                # If more than 10% of the keypoints match draw the matching set
                # find the maximum in C1-4[6]
                c[0]= 0
                c[1]=c1[6]
                c[2]=c2[6]
                c[3]=c3[6]
                c[4]=c4[6]
                print(c)
                c[0]=c[1] #init c[0]
                m=1
                for j in range(2):
                    if (c[0]<c[j+2] ):
                        m=j+2
                        c[0]=c[j+2]

                if (c[0]>0 ): # above a bar = matching someone
                    if (m==1):
                        img.draw_cross(c1[0], c1[1], size=5)
                        img.draw_string(0, 10, "Match %d%%"%(c1[6]))
                        print("He jianfei DETECTED","Match %d%%"%(c1[6]))
                        i[1]=i[1]+1
                        green_led.on()
                        time.sleep(1000)
                        green_led.off()
                    if (m==2):
                        img.draw_cross(c2[0], c2[1], size=5)
                        img.draw_string(0, 10, "Match %d%%"%(c2[6]))
                        print("sun fang DETECTED","Match %d%%"%(c2[6]))
                        i[2]=i[2]+1
                        green_led.on()
                        time.sleep(300)
                        green_led.off()
                    if (m==3):
                        img.draw_cross(c3[0], c3[1], size=5)
                        img.draw_string(0, 10, "Match %d%%"%(c3[6]))
                        print("He zhiyuam DETECTED","Match %d%%"%(c3[6]))
                        i[3]=i[3]+1
                        blue_led.on()
                        time.sleep(1000)
                        blue_led.off()
                    if (m==4):
                        img.draw_cross(c4[0], c4[1], size=5)
                        img.draw_string(0, 10, "Match %d%%"%(c4[6]))
                        print("He muyuan DETECTED","Match %d%%"%(c4[6]))
                        i[4]=i[4]+1
                        blue_led.on()
                        time.sleep(300)
                        blue_led.off()

            # Draw FPS
            img.draw_string(0, 0, "FPS:%.2f"%(clock.fps()))
            # make decision based on times of matching for each person
            # find the maximum in i[1-4]
            i[0]=i[1] #init i[0] and m
            m=1
            for j in range(2):
                if (i[0]<i[j+2] ):
                    m=j+2
                    i[0]=i[j+2]
            if (i[m]>5): # conclue the decision and init the i[1-4]
                if (m==1):
                    i2c.send('j',22)
                if (m==2):
                    i2c.send('f',22)
                if (m==3):
                    i2c.send('z',22)
                if (m==4):
                    i2c.send('m',22)
                for j in range(4):
                    i[j]=0





