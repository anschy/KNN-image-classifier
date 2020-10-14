#KNN Image Classifier 
import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass
    
    def train(self,x,y):
        
        self.xtr = x   #model is simply memorising the dataset or image here
        self.ytr = y
    
    def predict(self,x):
        num_test = x.shape[0]
        y_pred = np.zeros(num_test,dtype = self.ytr.dtype)  #so that the output matches the exact input type
        
        for i in range(num_test):
            distances = np.sum(np.absolute(self.xtr = x[i,:]),axis = 1)  #uding L1 distance find the nearest image from training dataset to the i'th test image
            min_index = np.argmin(distances)   #the smallest distance, thus resulting the similar image according to the model.
            ypred[i] = self.ytr[min_index]
            
        return y_pred                          #return the label of that image