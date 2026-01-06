import numpy as np

class Variable
    def __init__(self,data):
        self.data=data
        self.grad=None  #导数
        self.creator=None #父类
        

    def backward(self):
        if self.grad is None:
            self.grad=1
        funcs=[self.creator]
        while funcs:
            f=funcs.pop()
            if type(f) is list
                funcs.extend(f)
            else:
                x,y=f.input,f.output
                x.grad=f.backward(y.grad)

                if x.creator is not None:

                    funcs.append(x.creator)
