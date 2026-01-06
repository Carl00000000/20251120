import numpy as np

class Sigmoid:
    def __init__(self,creator):
        self.out=None
        self.creator=creator

    def forward(self,i):
        out=1/(1+np.exp(-i.data))
        self.out=out
        return out

    def backward(self,dout):
        dx=dout*(1.0-self.out)*self.out
        self.creator.grad=dx
        return dx


class Add:
    def __init__(self,input1,input2):
        self.out=None
        self.input1=input1
        self.input2=input2

    def forward(self):
        out=x1.data+x2.data
        self.out=out
        return out

    def backward(self,dout):
        self.input1.grad=dout
        self.input2.grad=dout
        return dout


class Take:
    def __init__(self,input1,input2):
        self.out=None
        self.input1=input1
        self.input2=input2

    def forward(self):
        out=input1.data*input2.data
        self.out=out
        return out

    def backward(self,dout,):
        self.input1.grad=dout*input2.data
        self.input2.grad=dout*input1.data

