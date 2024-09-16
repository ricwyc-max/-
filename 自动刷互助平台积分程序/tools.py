#coding=utf-8
__author__ = 'Eric'

#导包
import cv2
import numpy as np
import pyautogui as pg
import time
import pytesseract


#为了简化代码，后续可以把查找图像并点击封装成为一个函数

class Tools:
    #定义变量options表示不同的模式
    def __init__ (self,_time=0,numb=0,stop=0):
        self._time = _time
        self.numb = numb
        self.stop = stop
        self.count = 0
        self.reGood = 0



    #截屏方法
    def sotWindowsAndSave(self):
        pg.screenshot('D:/机器视觉/自建有趣项目/自动刷互助平台积分程序/pictures/all.png')
        url ='./pictures/all.png'
        return (url)





    #预处理程序
    def pre_run(self):
        screen_with,screes_high = pg.size()
        #识别电脑屏幕的尺寸
        #元组类型返回值

        #pyCharm图标坐标位置
        pc_x = 0
        pc_y = 0

        #输出屏幕的宽和高
        print('屏幕的宽为：'+str(screen_with))
        print('屏幕的高为：'+str(screes_high))

        #鼠标移动到右下角，点击返回桌面
        pg.click(2555,1550,clicks=1,interval=0,button='left',duration=0)


        time.sleep(0.7)
        #双击鼠标打开浏览器
        pg.doubleClick(56,203)

        #找到全屏按钮，单击，使浏览器全屏
        time.sleep(0.7)
        url = Tools.sotWindowsAndSave(self)

        template_1 = cv2.imread(url)
        gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)

        img_1 = cv2.imread('./pictures/big.png')
        grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)

        #二值化
        _,dst =cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        _,dstImg=cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)

        res_1 = cv2.matchTemplate(dst,dstImg,cv2.TM_SQDIFF_NORMED)
        min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)

        pg.click(min_loc_1[0]+154,min_loc_1[1]+32,clicks=1,interval=0,button='left',duration=0)


        #以下为调试程序，框出寻找浏览器的范围
        #print(max_loc)
        #print(min_loc)
        #img = cv2.rectangle(template_1,min_loc_1,(min_loc_1[0]+205,min_loc_1[1]+55),(0,0,255),2)
        #cv2.namedWindow('template',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('template',(2560,1600))
        #cv2.imshow('template',template_1)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #找到收藏文件夹，打开网站
        time.sleep(0.4)
        url = Tools.sotWindowsAndSave(self)
        #灰度化+读图片
        template_1 = cv2.imread(url)
        gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)

        img_1 = cv2.imread('./pictures/doc1.png')
        grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)

        #二值化
        _,dst =cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        _,dstImg=cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)

        #cv2.imshow('img',dstImg)
        #cv2.imshow('img1',dst)
        #cv2.waitKey(0)

        res_1 = cv2.matchTemplate(dst,dstImg,cv2.TM_SQDIFF_NORMED)
        min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
        pg.click(min_loc_1[0]+37,min_loc_1[1]+24,button='left')

        #找到并点击网站
        time.sleep(0.4)
        url=Tools.sotWindowsAndSave(self)

        template_1 = cv2.imread(url)
        gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)

        img_1 = cv2.imread('./pictures/web1.png')
        grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)

        #二值化
        _,dst =cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        _,dstImg=cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY)

        res_1 = cv2.matchTemplate(dst,dstImg,cv2.TM_SQDIFF_NORMED)
        min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
        pg.click(min_loc_1[0]+178,min_loc_1[1]+23,button='left')




        #点击以下屏幕防止出现其他什么东西
        time.sleep(2)
        pg.click(200,800,button='left')

        #找到任务中心（去助力）并进入
        time.sleep(0.5)
        url = Tools.sotWindowsAndSave(self)
        template_1 = cv2.imread(url)
        img_1 = cv2.imread('./pictures/goToHelp.png')
        res_1 = cv2.matchTemplate(img_1,template_1,cv2.TM_SQDIFF_NORMED)
        min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
        pg.click(min_loc_1[0]+93,min_loc_1[1]+41,button='left')





    #完播任务方法
    def overPlayMode(self):

        #找到完播的赚取积分按钮，点击一下
        time.sleep(0.2)
        url = Tools.sotWindowsAndSave(self)
        template_1 = cv2.imread(url)
        img_1 = cv2.imread('./pictures/EarnScore.png')
        res_1 = cv2.matchTemplate(img_1,template_1,cv2.TM_SQDIFF_NORMED)
        min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
        pg.click(min_loc_1[0]+317,min_loc_1[1]+159,button='left')

        #点击观看视频
        while True:
            time.sleep(1)
            url = Tools.sotWindowsAndSave(self)
            template_1 = cv2.imread(url)
            pg.click(1375,1295,button='left')
            time.sleep(5)



    #点赞任务方法
    def clicGoodMode(self):
        #找到点赞的赚取积分按钮，点击一下
        time.sleep(0.2)
        url = Tools.sotWindowsAndSave(self)
        template_1 = cv2.imread(url)
        img_1 = cv2.imread('./pictures/EarnScore.png')
        res_1 = cv2.matchTemplate(img_1,template_1,cv2.TM_SQDIFF_NORMED)
        min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
        pg.click(min_loc_1[0]+1115,min_loc_1[1]+159,button='left')


        while True:
            #找到点赞视频按钮，点击一下
            time.sleep(5)
            url = Tools.sotWindowsAndSave(self)
            template_1 = cv2.imread(url)
            img_1 = cv2.imread('./pictures/clicGood.png')
            #灰度化
            gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
            grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
            #二值化
            _,dst =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

            #cv2.imshow('img',dst)
            #cv2.waitKey(0)

            _,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)


            #cv2.imshow('dst',dst)
            #cv2.imshow('dstImg',dstImg)
            #cv2.waitKey()


            #匹配+点击
            res_1 = cv2.matchTemplate(dstImg,dst,cv2.TM_SQDIFF_NORMED)
            min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
            pg.click(min_loc_1[0]+86,min_loc_1[1]+31,button='left')



            #如果点赞按钮旁边出现重新检测，记录次数，次数超过5跳过本次任务
            roi = dst[min_loc_1[1]+10:min_loc_1[1]+50,min_loc_1[0]+200:min_loc_1[0]+370]
            ifRe = pytesseract.image_to_string(roi,lang='chi_sim+eng',config = '--psm 7 --oem 3')
            img1 = cv2.imread('./pictures/reText.png')
            grayImg1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
            _,dstImg1 =cv2.threshold(grayImg1,200,255,cv2.THRESH_BINARY)
            ifReText = pytesseract.image_to_string(dstImg1,lang='chi_sim+eng',config = '--psm 7 --oem 3')

            #cv2.imshow('img',roi)
            #cv2.waitKey(0)

            print(ifReText)
            print(ifRe)
            if ifRe == ifReText:
                self.count+=1
                print(self.count)
            else:
                self.count =0


            while True:

                #匹配点赞按钮，点击
                time.sleep(5)
                url = Tools.sotWindowsAndSave(self)
                template_1 = cv2.imread(url)
                img_1 = cv2.imread('./pictures/good.png')
                #灰度化
                gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
                grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
                #二值化
                _,dst =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
                _,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)
                #找到感兴趣的区域
                roi = dst[224:1410,663:2046]
                #cv2.imshow('img',roi)
                #cv2.waitKey(0)

                #匹配+点击
                res_1 = cv2.matchTemplate(dstImg,roi,cv2.TM_SQDIFF_NORMED)
                min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
                self.reGood+=1


                #先检查点赞前数量
                #检测是否点赞成功，通过检测点赞数的数字变化
                #再次深度选择感兴趣区域
                roi = roi[min_loc_1[1]+70:min_loc_1[1]+135,min_loc_1[0]+45:min_loc_1[0]+122]
                #点击操作
                pg.click(min_loc_1[0]+28+663,min_loc_1[1]+112+224,button='left')


                #再次检查点赞后数量
                time.sleep(3)
                #重新截图
                url = Tools.sotWindowsAndSave(self)
                template_1 = cv2.imread(url)
                gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
                _,dst =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
                roi_1 = dst[224:1410,663:2046]

                roi_1 = roi_1[min_loc_1[1]+70:min_loc_1[1]+135,min_loc_1[0]+45:min_loc_1[0]+122]

                #对两者进行膨胀操作，增加辨别度，防止出现因为太细而检测不出的问题
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
                roi = cv2.erode(roi,kernel,iterations=1)
                roi_1 = cv2.erode(roi_1,kernel,iterations=1)

                #cv2.imshow('img',np.hstack((roi,roi_1)))
                #cv2.waitKey(0)


                #roi_1为点赞后特征图片、roi为点赞前特征图片,利用光学OCR识别出数字，以str形式储存(识别方式变成数字，防止错误识别成中文)
                preNum = pytesseract.image_to_string(roi,lang='chi_sim+eng',config = '--psm 7 --oem 3')
                aftNum = pytesseract.image_to_string(roi_1,lang='chi_sim+eng',config = '--psm 7 --oem 3')

                print(preNum)
                print(aftNum)

                #判断是否检测成字母
                isnum = 1
                try:
                    #转换数据类型比较大小
                    if (eval(preNum) < eval(aftNum)):
                        isCorrect = 1
                    elif (eval(preNum) > eval(aftNum)):
                        isCorrect = 0
                    else:
                        isCorrect = 2
                except Exception:
                    isCorrect=1
                    isnum = 0


                if  isnum ==1 and isCorrect == 1 :
                    #如果点赞后数字大于点赞前(或者出现识别出字母)，则点赞成功，关闭页面
                    url = Tools.sotWindowsAndSave(self)
                    template_1 = cv2.imread(url)
                    gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
                    _,dst =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
                    roi_1 = dst[224:1410,663:2046]

                    img_1 = cv2.imread('./pictures/close.png')
                    grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
                    _,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)

                    #cv2.imshow('img',dstImg)
                    #cv2.imshow('img1',dst)
                    #cv2.waitKey(0)

                    res_1 = cv2.matchTemplate(dstImg,roi_1,cv2.TM_SQDIFF_NORMED)
                    min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
                    pg.click(min_loc_1[0]+162+663,min_loc_1[1]+20+224,button='left')
                    self.reGood=0
                    break

                elif isCorrect == 2 or self.count>=5 or isnum == 0 or self.reGood>=5:
                    #如果点赞数相等，或者重复5次出现“重新检测”,或者重复5次点赞还循环，表示已经点赞过了，或者点赞检测有问题，关闭页面，退出跳过该任务
                    url = Tools.sotWindowsAndSave(self)
                    template_1 = cv2.imread(url)
                    gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
                    _,dst =cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
                    roi_1 = dst[224:1410,663:2046]

                    img_1 = cv2.imread('./pictures/close.png')
                    grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
                    _,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)

                    #cv2.imshow('img',dstImg)
                    #cv2.imshow('img1',dst)
                    #cv2.waitKey(0)

                    res_1 = cv2.matchTemplate(dstImg,roi_1,cv2.TM_SQDIFF_NORMED)
                    min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
                    pg.click(min_loc_1[0]+162+663,min_loc_1[1]+20+224,button='left')

                    break

                else:
                    #如果点赞不成功，则退出循环，再点赞一次
                    #注意视频要设置成不自动播放下一个和播放完后暂停模式，否则会跳另一个视频，从而导致失败
                    continue

            #点赞完毕关闭窗口后，点击完成按钮
            time.sleep(0.2)
            url = Tools.sotWindowsAndSave(self)
            template_1 = cv2.imread(url)
            gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
            _,dst=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

            img_1 = cv2.imread('./pictures/OK.png')
            grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
            _,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)

            #cv2.imshow('dstImg',dstImg)
            #cv2.imshow('dst',dst)
            #cv2.waitKey(0)

            res_1 = cv2.matchTemplate(dstImg,dst,cv2.TM_SQDIFF_NORMED)
            min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
            pg.click(min_loc_1[0]+535,min_loc_1[1]+159,button='left')
            self.reGood = 0

            if isCorrect == 2 or self.count >= 5 or isnum == 0 or self.reGood>=5:
                time.sleep(3)
                url = Tools.sotWindowsAndSave(self)
                template_1 = cv2.imread(url)
                gray = cv2.cvtColor(template_1,cv2.COLOR_BGR2GRAY)
                _,dst=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

                img_1 = cv2.imread('./pictures/jump.png')
                grayImg = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
                _,dstImg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)

                res_1 = cv2.matchTemplate(dstImg,dst,cv2.TM_SQDIFF_NORMED)
                min_val_1,max_val_1,min_loc_1,max_loc_1 = cv2.minMaxLoc(res_1)
                pg.click(min_loc_1[0]+95,min_loc_1[1]+29,button='left')





