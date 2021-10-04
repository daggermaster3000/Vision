# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:29:50 2021
Code to analyse colored samples
@author: daggermaster3000
"""

import cv2
import os
import numpy as np
import csv

header = ['name','ratio','treat']
log = []
directory = 'C:/Users/BIC-Mobility/Documents/Quillan/iGem/VISION/input-data4/crop'#input
path = 'C:/Users/BIC-Mobility/Documents/Quillan/iGem/VISION/output-data4'#output

#filter values
lf_damage = [0, 75, 0]
hf_damage = [179, 255, 255]
lf_total = [0, 0, 0]
hf_total = [254, 254, 254]

prefix_dic = {
        "buffer":"buffer",
        "Ffibp":"FFIBP",
        "FfIBP":"FFIBP",
        "FfiBP+RiAFP":"RI+FF-4",
        "RiAFP":"RIAFP"
        }


for filename in os.listdir(directory):
    
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print('Processing:',os.path.join(directory, filename)) 
               
        #Process image for damaged area
        image = cv2.imread(os.path.join(directory, filename))
        original = image.copy()
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
        
        
        '''
        cv2.imshow('mask', mask)
        cv2.imshow('original', original)
        cv2.imshow('opening', opening)
        
        '''
        

        
        #process image for total area
        
        
        original_tot = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array(lf_total, dtype="uint8")
        upper = np.array(hf_total, dtype="uint8")
        mask_tot = cv2.inRange(image, lower, upper)
     
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(mask_tot, cv2.MORPH_OPEN, kernel, iterations=1)
     
        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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



        #write to log
        for i in prefix_dic.keys():
            if filename.startswith(i):
                log.append([filename,(np.round(damaged_area/area,2))*100,str(prefix_dic[i])])    
        
    else:
        continue

    #output log file
with open('C:/Users/BIC-Mobility/Documents/Quillan/iGem/VISION/output-data4/data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(log)

    