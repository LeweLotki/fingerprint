import cv2 
import numpy as np 
import random
from packages import functions as fun

obj = []
points = []
new_size = (600, 800)
n =  10*int((new_size[0]*new_size[1])**0.5)
m = 0
img = cv2.imread(r'images\thumb.jpg', 0)
img = cv2.resize(img, new_size)
while m < n:

    x = random.randint(0, new_size[0] - 1)
    y = random.randint(0, new_size[1] - 1)
    points.extend([[y,x]])
    m += 1  
# print(len(points))
points  = fun.detection(points, img, 100)
if len(points) > 1:              
    while len(points) > 10:
        dist = fun.distance(points[0], points)
        uni = fun.unify_simple(dist, points)
        # print(uni)
        obj.append(uni)
# print(obj)
object = fun.sort(obj)
# print(object)
max_height, min_height, max_width, min_width = fun.extremum(object)
img = img[min_height:max_height, min_width + 50:max_width - 50]
# print(np.shape(img))
img_contrast = fun.contrast(img, 0.1) #tutaj
img_contrast = fun.contrast(img, 10) #tutaj
height, width = np.shape(img)
finger_line = fun.separation(img, 100)
contrst_line = fun.separation(img_contrast, 100) #tutaj
imgf = np.zeros(( height, width ))
imgf  = fun.extract(finger_line, imgf, 255)
final_print = fun.common(finger_line, contrst_line)
finger_print = np.zeros(( height, width ))
# print(finger_print, np.shape(finger_print))
finger_print = fun.extract(final_print, finger_print, 255)
# print("im here", finger_print)
# print('now im here',np.shape(finger_print))
# print(len(points), len(obj))      

while True: 
    # cv2.imshow("image", img) 
    # cv2.imshow("image2", img_contrast)
    # cv2.imshow("imagef", imgf) 
    cv2.imshow("fingerprint", finger_print)
    if cv2.waitKey(10) == 27: 
        break
cv2.imwrite(r"fingerprint.jpg", finger_print)
cv2.destroyAllWindows() 