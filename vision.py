# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:29:50 2021
Code to analyse a ratio between two colored areas, initially used to determine damage ratio done to leaves highlighted by trypan blue staining

@author: daggermaster3000
"""

import cv2
import os
import numpy as np
import csv

header = ['name','ratio','treat']
log = []                #temporary for csv output
directory = 'C:/Users/input'      #input path
path = 'C:/Users/output'               #output path

#filter values
lf_damage = [0, 75, 0]                  #thresholds for damaged area
hf_damage = [179, 255, 255]
lf_total = [0, 0, 0]                    #thresholds for total area
hf_total = [254, 254, 254]

# Prefix dictionary that will check in the file name the type of sample and output it in the csv
prefix_dic = {
        "Buffer":"buffer",
        "Ffibp":"FFIBP",
        "FfIBP":"FFIBP",
        "FfiBP+RiAFP":"RI+FF-4",
        "RiAFP":"RIAFP"
        }

#Get files (png or jpg)

for filename in os.listdir(directory):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print('Processing:',os.path.join(directory, filename)) 
               
        #Process image for damaged area
        image = cv2.imread(os.path.join(directory, filename))
        original = image.copy()
        image2 = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array(lf_damage, dtype="uint8")
        upper = np.array(hf_damage, dtype="uint8")
        mask = cv2.inRange(image, lower, upper)
     
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
     
        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
     
        damaged_area = 0
        for c in cnts:
         damaged_area += cv2.contourArea(c)
         cv2.drawContours(original,[c], 0, (0,255,0), 2)
     
        print(damaged_area)
        

           
        #process image for total area
        
        
        original_tot = image2.copy()
        image = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
        lower = np.array(lf_total, dtype="uint8")
        upper = np.array(hf_total, dtype="uint8")
        mask_tot = cv2.inRange(image, lower, upper)
     
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(mask_tot, cv2.MORPH_OPEN, kernel, iterations=1)
        #chainapproxsimple is faster than the none...
        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #just to check not necessary
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
     
        area = 0
        for c in cnts:
         area += cv2.contourArea(c)
         cv2.drawContours(original,[c], 0, (0,255,0), 2)
     
        print(area)
        


        #output processed images to output folder
        
        size = len(filename)
        filename = filename[:size - 4]
        cv2.imwrite(os.path.join(path , filename+'_original.jpg'), original)
        cv2.imwrite(os.path.join(path , filename+'_mask.jpg'), mask)
        cv2.imwrite(os.path.join(path , filename+'_original-tot.jpg'), original_tot)
        cv2.imwrite(os.path.join(path , filename+'_mask-tot.jpg'), mask_tot)



        #write to temporary log for csv output
        for i in prefix_dic.keys():
            if filename.startswith(i):
                log.append([filename,(np.round(damaged_area/area,2))*100,str(prefix_dic[i])])    
        
    else:
        continue

    #output the temp file as csv

with open('C:/Users/BIC-Mobility/Documents/Quillan/iGem/VISION/output-data4/data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(log)

    
