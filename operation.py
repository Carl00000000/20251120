import numpy as np

class Sigmoid:
    def __init__(self):
        self.out=None

    def forward(self,i):
        out=1/(1+np.exp(-i.data))
        self.out=out
        return out

    def backward(self,dout):
        dx=dout*(1.0-self.out)*self.out
        return dx


class Add:
    def __init__(self):
        self.out=None
        self.input1=None
        self.input2=None

    def forward(self,x1,x2):
        out=x1.data+x2.data
        self.input1=x1
        self.input2=x2
        self.out=out
        return out

    def backward(self,dout):
        return dout


class Take:
    def __init__(self):
        self.out=None
        self.input1=None
        self.input2=None

    def forward(self,x1,x2):
        out=x1.data*x2.data
        self.input1=x1
        self.input2=x2
        self.out=out
        return out

    def backward(self,dout,x1):
        if x1==self.input1:
            dx=dout*x2.data
        elif x1==self.input2:
            dx=dout*x1.data
        else:
            raise ValueError() 
