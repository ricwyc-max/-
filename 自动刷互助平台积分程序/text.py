#coding=utf-8
__author__ = 'Eric'

import cv2
import pytesseract

template_1 = cv2.imread('./pictures/all.png')
img_1 = cv2.imread('./pictures/clicGood.png')
#灰度化
gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
#二值化
_,dst =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
_,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)
res_1 = cv2.matchTemplate(dstImg,dst,cv2.TM_SQDIFF_NORMED)
min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
roi = dst[min_loc_1[1]+10:min_loc_1[1]+50,min_loc_1[0]+200:min_loc_1[0]+370]
ifRe = pytesseract.image_to_string(roi,lang='chi_sim+eng',config = '--psm 7 --oem 3')

img1 = cv2.imread('./pictures/reText.png')
grayImg1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
_,dstImg1 =cv2.threshold(grayImg1,200,255,cv2.THRESH_BINARY)
ifReText = pytesseract.image_to_string(dstImg1,lang='chi_sim+eng',config = '--psm 7 --oem 3')

print(ifRe)
print(ifReText)



cv2.imshow('img',roi)

cv2.imshow('img1',dstImg1)

cv2.waitKey(0)
cv2.destroyAllWindows()
