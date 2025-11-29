def numerical_diff(f,x,eps=le-4):
    x0=x+eps
    x1=x-eps
    y0=f(x0)
    y1=f(x1)
    return (y0-y1)/(2*eps)