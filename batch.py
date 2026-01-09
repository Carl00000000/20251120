def batch_X2(self,a,b,c):
    z=[]
    for i in len(a):
        a1=a[i]
        b1=b[i]
        z1=c(a1,b1)
        z.append(z1)

    return z

def batch_add_X1(self,a):
    z=0.0
    for i in len(a):
        z=z+a[i]
    return z