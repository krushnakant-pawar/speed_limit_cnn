import os
import cv2
import numpy as np

def main():
    mysrcdir = "/home/krushnakant/mydocker/speedlimit_dataset/train/00014/"
    mydstdir = "/home/krushnakant/mydocker/OpenCV-Python-Tutorials-for-Beginners/Advance/TrafficSignsCNN/myData/14/"    
    
    pic_num = 1

    for filename in os.listdir(mysrcdir):
       # print(filename)
        
        #rename images
        dst = os.path.splitext(filename)[0] + ".jpg"
        src = mysrcdir + filename
        dst = mydstdir + dst
        print("dst: "+ dst)
        #print("src: "+ src)
        #os.rename(src,dst)

        
        #modify renamed images        
        img = cv2.imread(src)
        resized_image = cv2.resize(img, (32,32))
        
        #save modified images in same directory
        cv2.imwrite(dst,resized_image)
        pic_num +=1        
        

if __name__ == '__main__':
    main()

def create_pos_n_neg():
	for file_type in ['neg']:
		for img in os.listdir(file_type):
			if file_type == 'neg':
				line = file_type+'/'+img+'\n'
				with open('bg.txt','a') as f:
					f.write(line)


#create_pos_n_neg()
