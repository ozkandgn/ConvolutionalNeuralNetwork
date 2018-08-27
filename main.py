from Image_Processing import CNN as cnn
from Simple_Neural_Network import main as nn

def Try(adress,outp,nodeWeight,weight):
    nodeWeight[0]=cnn.Processing(str(adress)).main()
    nodeWeight[0].append(1)#bias
    nodeWeight[-1]=outp#output
    return nn.TryNetwork.Try(nodeWeight,weight)
print("CNN Started!!!")
images=[]
images.append(cnn.Processing("Image_Processing/images/animals.jpg").main())
print("İmage-1 Was Processed")
images.append(cnn.Processing("Image_Processing/images/dog2.jpg").main())
print("İmage-2 Was Processed")
images.append(cnn.Processing("Image_Processing/images/cat3.jpg").main())
print("İmage-3 Was Processed")
images.append(cnn.Processing("Image_Processing/images/dog2.jpg").main())
print("İmage-4 Was Processed")
images.append(cnn.Processing("Image_Processing/images/dog3.jpg").main())
print("İmage-5 Was Processed")
images.append(cnn.Processing("Image_Processing/images/cat.jpg").main())
print("İmage-6 Was Processed")
images.append(cnn.Processing("Image_Processing/images/NewCat2.jpg").main())
print("İmage-7 Was Processed")
outs=[[1,0,0],[0,1,0],[0,0,1],[0,1,0],[0,1,0],[0,0,1],[0,0,1]]\
      #other=1,0,0 -- dog=0,1,0 -- cat=0,0,1
print("Train Starting")
nodeWeight,weight=nn.main(images,outs,True,0.01)#true=read Weight
nodeWeight,result,difference=Try("Image_Processing/images/kangal.jpg",\
                                [0,1,0],nodeWeight,weight)
print("Result ",result," Diff",difference)
nodeWeight,result,difference=Try("Image_Processing/images/cat2.jpg",\
                                [0,0,1],nodeWeight,weight)
print("Result ",result," Diff",difference)
nodeWeight,result,difference=Try("Image_Processing/images/animals2.jpg",\
                                [1,0,0],nodeWeight,weight)
print("Result ",result," Diff",difference)
nodeWeight,result,difference=Try("Image_Processing/images/NewCat1.jpg",\
                                [0,0,0],nodeWeight,weight)
print("Result ",result," Diff",difference)
