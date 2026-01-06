def batch(self,a,b,c):
    z=[]
    for i in len(a):
        a1=a[i]
        b1=b[i]
        z1=c(a1,b1)
        z.append(z1)

    return z