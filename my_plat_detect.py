from hyperlpr_py3 import  pipline as  pp
import hyperlpr_py3.config as hyperConfig
import cv2
import sys
import os

debugInfo = hyperConfig.configuration["global"]["debug"]
testPath = hyperConfig.configuration["detectTest"]["detectPath"]
outPath = hyperConfig.configuration["detectTest"]["outputPath"]

def detectPlateTest(filepath):
    for filename in os.listdir(filepath):
        if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png"):
            fileFullPath = os.path.join(filepath,filename)
            image = cv2.imread(fileFullPath)
            print(fileFullPath)
            image_c = image.copy()
            image_c,res  = pp.SimpleRecognizePlateByE2E(image_c)
            pathName = filename.split('.')[0]
            if debugInfo:
            	if os.path.exists(os.path.join(outPath,pathName)) == False:
            		os.mkdir(os.path.join(outPath,pathName))
            	cv2.imwrite(os.path.join(outPath,pathName,"out_"+pathName+".png"),image_c)

if __name__ == "__main__":
    detectPlateTest(testPath)

