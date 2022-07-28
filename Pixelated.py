import cv2
im1 = cv2.imread('scrambled1.png') #image read
im2 = cv2.imread('scrambled2.png')
# we guess we will +,-,*,^,... two image
# and with using hint: + , so cv2 help us
cv2.imshow('flag',im1+im2) # flag: picoCTF{0542dc1d}
cv2.waitKey(0) 