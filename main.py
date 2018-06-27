from Image_Processing import CNN as cnn
from Simple_Neural_Network import main as nn
print("CNN Started!!!")
network=nn
img=cnn.Processing("Image_Processing/images/kangal.jpg").main()
print("İmage-1 Was Processed")
img2=cnn.Processing("Image_Processing/images/cat.jpg").main()
print("İmage-2 Was Processed")
img3=cnn.Processing("Image_Processing/images/dog.jpg").main()
print("İmage-3 Was Processed")
img4=cnn.Processing("Image_Processing/images/cat2.jpg").main()
print("İmage-4 Was Processed")
images=[]
images.append(img)
images.append(img2)
images.append(img3)
images.append(img4)
outs=[0,1,0,1]#dog 0
print("Train Starting")
nodeWeight,weight=network.main(images,outs)
nodeWeight[0]=img3
nodeWeight[0],result,difference=network.TryNetwork.Try(nodeWeight,weight)
print("Result ",result)
nodeWeight[0]=img4
nodeWeight,result,difference=network.TryNetwork.Try(nodeWeight,weight)
print("Result ",result)
