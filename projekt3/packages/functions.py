import cv2 
import numpy as np 
import random

def contrast(img, num):
    img2 = img.copy()
    height, width = np.shape(img)
    for val in range(0, height):
        for val2 in range(0, width):
            img2[val,val2] = int(num* img2[val,val2])
            if img2[val,val2] > 255:
                img2[val,val2] = 255
    return img2
    
def separation(array, limit):
    temp_list = []
    height, width = np.shape(array)
    for val in range(0, height):
        for val2 in range(0, width):
            if array[val,val2] > limit:
                temp = (val, val2)
                temp_list.append(temp)
    return temp_list
    
def extract(list, array, color):
    temp = array.copy()
    for val in list:
        temp[val[0],val[1]] = color
    return temp
    
def unify_simple(dist, points):
    a = 0
    b = 3
    i = 0
    temp = []
    density = True
    while density:
        for val in dist:
            if val[1] in range(a, b):
                temp.extend([val[0]])
                if val[0] in points:
                    points.remove(val[0])
            else:
                i += 1
                if i == len(dist):
                    density = False
                    break             
        a += 2
        b += 2
        i = 0
    if len(temp) == 0:
        print('ERROR')
    return temp
    
def distance(num, list):
    temp = []
    temp2 = []
    for val in list:
        d = int(((num[0]-val[0])**2 + (num[1]-val[1])**2)**0.5)
        temp.append(d)
    for i in range(0, len(list)):
        temp2.extend([[list[i],temp[i]]])
    return temp2
    
def detection(list, array, limit):
    temp_list = []
    for val in list:
            if array[val[0],val[1]] > limit:
                temp = (val[0], val[1])
                temp_list.append(temp)
    return temp_list
    
def extremum(list):
    max_height = 0
    min_height = 10000
    max_width = 0
    min_width = 10000
    for val in list:
        if val[0] > max_height:
            max_height = val[0]
        if val[0] < min_height:
            min_height = val[0]
        if val[1] > max_width:
            max_width = val[1]
        if val[1] < min_width:
            min_width = val[1]
    return max_height, min_height, max_width, min_width
    
def sort(list):
    temp_lenght = len(list[0])
    temp = list[0]
    for val in list:
        if len(val) > temp_lenght:
            temp_lenght = len(val)
            temp = val
    return temp
    
def common(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    result = list1.intersection(list2)
    result = list(result)
    # print("im here", result)
    return result
    
    
    




