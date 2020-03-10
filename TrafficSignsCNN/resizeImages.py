import cv2
import numpy as np 
import os

directory = 'newData/'
dstDirectory = 'Data/'
IMG_SIZE = 50

for subDirectory in os.listdir(directory):
    print(subDirectory)
    for filename in os.listdir(directory + subDirectory):
        if not os.path.exists(dstDirectory+subDirectory):
            os.makedirs(dstDirectory+subDirectory)
        srcFile = directory + subDirectory + '/' + str(filename)
        dstFile = dstDirectory + subDirectory + '/' + str(filename)
        #print(srcFile)
        img = cv2.imread(srcFile)
        resized_img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        cv2.imwrite(dstFile, resized_img)