import cv2
import numpy as np

img = cv2.imread("6.jpg")
img=cv2.resize(img,(500,492))
p=img.shape
ar=[0,0,0,0,0,0,0,0,0]
cv2.imshow('img',img)
img1=np.zeros(p,dtype=None)

#img = cv2.GaussianBlur(img,(3,3),0)
#canny = cv2.Canny(img, 50, 150)
#cv2.imshow('image',img)

#cv2.imshow('Canny', canny)
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
#cv2.imshow('hsv',hsv)
#lower_val = (36, 25, 25)
#upper_val = (70,255,255)        
# Threshold the HSV image to get only green colors
#mask = cv2.inRange(hsv, lower_val, upper_val)
# apply mask to original image
#green = cv2.bitwise_and(img,img, mask= mask)
#show imag
#cv2.imshow("green", green)




#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV


    # Threshold the HSV image to get only blue colors


    # Bitwise-AND mask and original image
#blue = cv2.bitwise_and(img,img, mask= mask)

#cv2.imshow("Result", blue)

# FOR BLUE

s=img[82,82]
if(s[0]>130 and s[1]<100 and s[2]<100 ):
   ar[0]=1

s=img[82,250]
if(s[0]>130 and s[1]<100 and s[2]<100 ):
   ar[1]=1

s=img[82,410]
if(s[0]>130 and s[1]<100 and s[2]<100):
   ar[2]=1

s=img[250,82]
if(s[0]>130 and s[1]<100 and s[2]<100):
   ar[3]=1

s=img[250,250]
if(s[0]>130 and s[1]<100 and s[2]<100):
   ar[4]=1

s=img[250,410]
if(s[0]>130 and s[1]<100 and s[2]<100 ):
   ar[5]=1

s=img[410,82]
if(s[0]>130 and s[1]<100 and s[2]<100 ):
   ar[6]=1

s=img[410,250]
if(s[0]>130 and s[1]<100 and s[2]<100):
   ar[7]=1

s=img[410,410]
if(s[0]>130 and s[1]<100 and s[2]<100):
   ar[8]=1






# FOR GREEN

s=img[82,82]
if(s[1]>120 and s[0]<100 ):
   ar[0]=2

s=img[82,250]
if(s[1]>120 and s[0]<100 ):
   ar[1]=2

s=img[82,410]
if(s[1]>120 and s[0]<100 ):
   ar[2]=2

s=img[250,82]
if(s[1]>120 and s[0]<100  ):
   ar[3]=2

s=img[250,250]
if(s[1]>120 and s[0]<100 ):
   ar[4]=2

s=img[250,410]
if(s[1]>120 and s[0]<100 ):
   ar[5]=2

s=img[410,82]
if(s[1]>120 and s[0]<100 ):
   ar[6]=2

s=img[410,250]
if(s[1]>120 and s[0]<100 ):
   ar[7]=2

s=img[410,410]
if(s[1]>120 and s[0]<100 ):
   ar[8]=2




# FOR RED

s=img[82,82]
if(s[2]>210 and s[0]<100 and s[1]<100):
   ar[0]=3

s=img[82,250]
if(s[2]>210 and s[0]<100 and s[1]<100):
   ar[1]=3

s=img[82,410]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[2]=3

s=img[250,82]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[3]=3

s=img[250,250]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[4]=3

s=img[250,410]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[5]=3

s=img[410,82]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[6]=3

s=img[410,250]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[7]=3

s=img[410,410]
if(s[2]>130 and s[0]<100 and s[1]<100):
   ar[8]=3


# FOR WHITE

s=img[82,82]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[0]=6

s=img[82,250]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[1]=6

s=img[82,410]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[2]=6

s=img[250,82]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[3]=6

s=img[250,250]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[4]=6

s=img[250,410]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[5]=6

s=img[410,82]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[6]=6

s=img[410,250]
if(s[0]>210 and s[1]>210 and s[2]>210):
   ar[7]=6

s=img[410,410]
if(s[0]>210 and s[1]>210 and s[2]>210 ):
   ar[8]=6



# FOR YELLOW

s=img[82,82]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[0]=5

s=img[82,250]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[1]=5

s=img[82,410]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[2]=5

s=img[250,82]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[3]=5

s=img[250,250]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[4]=5

s=img[250,410]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[5]=5

s=img[410,82]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[6]=5

s=img[410,250]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[7]=5

s=img[410,410]
if(s[0]<100 and s[1]>210 and s[2]>210):
   ar[8]=5



#FOR ORANGE
s=img[82,82]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[0]=4

s=img[82,250]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[1]=4

s=img[82,410]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[2]=4

s=img[250,82]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[3]=4

s=img[250,250]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[4]=4

s=img[250,410]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[5]=4

s=img[410,82]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[6]=4

s=img[410,250]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[7]=4

s=img[410,410]
if(s[0]<100 and s[1]>130 and s[2]>210 and s[1]<200):
   ar[8]=4

a1=[ar[0],ar[1],ar[2]]
a2=[ar[3],ar[4],ar[5]]
a3=[ar[6],ar[7],ar[8]]
print(a1)
print(a2)
print(a3)

cv2.waitKey(0)