import cv2
import numpy as np
b = input("enter a filename:   ")
path = ("C:\\Users\\vineesha thoutam\\Downloads\\" + b )
img = cv2.imread(path)
img = cv2.resize(img, (900,900))
logo = (r'C:\Users\vineesha thoutam\Pictures\logo.jpg')
logo = cv2.resize(logo, (900,900))
res = cv2,addWeighted(img, 0.9, logo, 0.4, 0.0)
cv2.imshow('logo', logo)
cv2.imshow('result', res)
cv2.waitKey(0)