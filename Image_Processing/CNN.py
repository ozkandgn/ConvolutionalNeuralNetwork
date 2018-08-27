import cv2
import numpy
from matplotlib import pyplot as py
from Image_Processing import mean


class Processing(object):
    def __init__(self,adress):
        self.adress=adress
        self.img=cv2.imread(self.adress)
        self.Size()

    def main(self):
        filt=[[1,1,1],[0,0,0],[-1,-1,-1]]
        self.Convolution(filt)
        filt=[[1,0,-1],[1,0,-1],[1,0,-1]]
        self.Convolution(filt)
        filt=[[-1,0,-1],[0,1,0],[-1,0,-1]]
        self.Convolution2D(filt)
        self.img=mean.MeanFilter(self.img,2)
        self.Pooling(2,2)
        #cv2.imshow("asd",self.img)
        self.Pooling(2,2)
        self.Pooling(2,2)
        self.img=mean.MeanFilter(self.img,3)
        #cv2.imshow(self.adress,self.img)
        print("H ",len(self.img)," + W ",len(self.img[0]))
        return self.GiveForNN()
    
    def Size(self):
 #       height=len(self.img)
 #       width=len(self.img[0])
 #        while height>640:
 #           height=height/1.25
 #       while width>360:
 #           width=width/1.25
        img = cv2.resize(self.img,(int(90),int(60)), interpolation = cv2.INTER_CUBIC)
        self.img=img
    
    def Convolution(self,filt):
        actImg=[]
        img=self.img
        for i in range(len(img)-len(filt)+1):
            actImg.append([])
            for j in range(len(img[i])-len(filt)+1):
                layers=[]
                actImg[i].append([])
                for k in range(len(img[i][j])):
                    total=0
                    for l in range(len(filt)):
                        for m in range(len(filt)):
                            total+=img[i+l][j+m][k]*filt[l][m]
                    if total<0:#ReLu
                        actImg[i][j].append(0)   
                    elif total>255:
                        actImg[i][j].append(255)
                    else:
                        actImg[i][j].append(total)   
        self.img=numpy.uint8(actImg)
        #cv2.imshow("Convolution Image",self.img)

    def Convolution2D(self,filt):
        actImg=[]
        img=self.img
        for i in range(len(img)-len(filt)+1):
            actImg.append([])
            for j in range(len(img[i])-len(filt)+1):
                total=0
                try:
                    for k in range(len(img[i][j])):
                        for l in range(len(filt)):
                            for m in range(len(filt)):
                                total+=img[i+l][j+m][k]*filt[l][m]
                except:
                    for l in range(len(filt)):
                        for m in range(len(filt)):
                            total+=img[i+l][j+m]*filt[l][m]
                total/=3
                if total<0:#ReLu
                    actImg[i].append(0)   
                elif total>255:
                    actImg[i].append(255)
                else:
                    actImg[i].append(total)   
        self.img=numpy.uint8(actImg)
        #cv2.imshow("Convolution Image",self.img)


    def Pooling(self,slip,filt):
        img=self.img
        pool=[]
        for i in range(0,len(img)-filt,slip):
            pool.append([])
            for j in range(0,len(img[i])-filt,slip):
                max=0
                for k in range(filt):
                    for l in range(filt):
                        if max<img[i+k][j+l]:
                            max=img[i+k][j+l]
                pool[int(i/slip)].append(max)
        self.img=numpy.uint8(pool)
        #cv2.imshow("Pooling",self.img)

    def GiveForNN(self):
        newImg=[]
        img=self.img
        for i in range(len(img)):
            for j in range(len(img[i])):
                newImg.append(round(float(img[i][j]/300),4))
        return list(newImg)

#Processing("images/animals2.jpg").main();
