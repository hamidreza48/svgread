from xml.dom import minidom
from svg.path import *
import cv2
from google.colab.patches import cv2_imshow
import numpy as np
import random
import math
#reza
def svgtoimg(filepath, thickness=2 ):
    img1 = np.zeros((800, 800, 3), dtype=np.uint8)
    doc = minidom.parse(filepath)  # parseString also exists
    path_strings = [path.getAttribute('d') for path
                    in doc.getElementsByTagName('path')]
    print(len(path_strings))
    logic = True
    cc = img1.shape[0]/maxx(path_strings)

    for path_string in path_strings:
        n = 1000
        points = []
        path1 =''
        points2 = np.zeros((n,2))
        path1 = path_string  
        path1 = path1.replace('C', 'T')   
        rr = random.randint(150,255)
        gg = random.randint(150,255)
        bb = random.randint(150,255)
        rgb = [rr,gg,bb]
        p = parse_path(path1)
        for r in range(n):
            points.append(p.point(r/n))
        i = 0    
        for point in points:
          x= point.real
          y = point.imag
          if i < n :
            points2[i]= [x, y]
            i= i+1
        

        # print('max' ,np.max(points2))
        # if logic:
        #   cc = 1/2 * img1.shape[1] / np.max(points2) 
          
        for i in range(n):
            points2[i, 0] = points2[i,0]*cc
            points2[i,1] =  points2[i,1]*cc 
        
        g = 0
        for i in range(n-1):
            x = points2[i,0]
            y = points2[i,1]
            xx = points2[i+1, 0]
            yy = points2[i+1, 1]
            if math.sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy)) > 20 :
                img1 = cv2.polylines(img1, np.int32([points2[g:i,:]]),False, rgb,thickness)
                g =i+1
            elif i==n-2:
                img1 = cv2.polylines(img1, np.int32([points2[g:n-2,:]]),False, rgb,thickness)

        logic = False
        # img1 = cv2.polylines(img1, np.int32([points2]), True, rgb,2)
    # img1 = cv2.flip(img1, 1)
    cv2_imshow(img1)
  
    return img1
def maxx(path_strings):
  max = 0
  for path_string in path_strings:
        n = 200
        points = []
        path1 =''
        points2 = np.zeros((n,2))
        path1 = path_string  
        path1 = path1.replace('C', 'L')   
        rr = random.randint(100,255)
        gg = random.randint(100,255)
        bb = random.randint(100,255)
        rgb = [rr,gg,bb]
        p = parse_path(path1)
        for r in range(n):
            points.append(p.point(r/n))
        i = 0    
        for point in points:
          x= point.real
          y = point.imag
          if i < n :
            points2[i]= [x, y]
            i= i+1
        if np.max(points2) > max:    
            max  = np.max(points2)
  return max

# files = os.listdir("/content/gdrive/MyDrive/svg/")
# for file in files:  
#     svgtoimg('/content/gdrive/MyDrive/svg/'+file) 
f = svgtoimg('/content/gdrive/MyDrive/svg/flamingo-svgrepo-com (1).svg', 1)   
