import os
import cv2
import numpy as np

def main():
    
    mydir = "/home/occ/neural/images/test/"
    mydstdir = "/home/occ/neural/images/new_test/"

    for filename in os.listdir(mydir):
        print(filename)
        dst = os.path.splitext(filename)[0] + ".jpg"
        src = mydir + filename
        dst = mydstdir + dst
        print("dst: "+ dst)
        print("src: "+ src)
        img = cv2.imread(src)
        resized_image = cv2.resize(img, (img.shape[1],img.shape[0]))
        cv2.imwrite(dst,resized_image)       

if __name__ == '__main__':
    main()
