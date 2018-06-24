from Image_Processing import CNN as cnn
from Simple_Neural_Network import main as nn
print("CNN Started!!!")
network=nn
img=cnn.Processing("Image_Processing/images/kangal.jpg").main()
print("İmage-1 Was Processed")
img2=cnn.Processing("Image_Processing/images/cat.jpg").main()
print("İmage-2 Was Processed")
images=[]
images.append(img)
images.append(img2)
outs=[0,1]#dog 0
print("Train Starting")
nodeWeight,weight=network.main(images,outs)
img=cnn.Processing("Image_Processing/images/dog.jpg").main()
nodeWeight[0]=img
nodeWeight[0],result,difference=network.TryNetwork.Try(nodeWeight,weight)
print("Result ",result)
nodeWeight[0]=cnn.Processing("Image_Processing/images/cat2.jpg").main()
nodeWeight,result,difference=network.TryNetwork.Try(nodeWeight,weight)
print("Result ",result)
