import numpy
import cv2
def MeanFilter(image,filt):
    for i in range(1,len(image)-1):
        for j in range(1,len(image[i])-1):
            total=0
            for k in range(filt):
                for l in range(filt):
                    total+=image[k+i-1][l+j-1]
            image[i][j]=int(total/(filt**2))
    image=numpy.uint8(image)
    return image

def Mean3D(image,filt):
    for i in range(1,len(image)-1):
        for j in range(1,len(image[i])-1):
            total=[0 for a in range(len(image[i][j]))]
            for k in range(filt):
                for l in range(filt):
                    for m in range(len(image[i][j])):
                        total[m]+=image[k+i-1][l+j-1]
            for k in range(len(total)):
                image[i][j][k]=int(total[k]/(filt**2))
    image=numpy.uint8(image)
    return image
