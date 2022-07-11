import os
import cv2
from random import choice

ImgPath = r"C:\Users\SV00253771\Desktop\test"
nameList = os.listdir(ImgPath)

rootPath = r"C:\Users\SV00253771\Desktop\ok"

count = 4
for i in range(4):
    for j in range(count):
        temp = choice(nameList)

        readPath = ImgPath + temp
        savePath = rootPath + str(i + 1) + "/" + temp

        img = cv2.imread(readPath)
        cv2.imwrite(savePath, img)

        nameList.remove(temp)

print(nameList)
print("end !")