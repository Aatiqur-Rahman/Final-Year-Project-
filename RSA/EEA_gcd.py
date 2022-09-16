import io,time,sys
x=1
y=0
def GCD(a,b,x,y):
    a_=a
    b_=b
    x_=0
    y_=1
    while (b_>0):
        q=int(a_/b_)
        #print ("q = ",q)
        x,x_=x_,int(x-q*x_)
        #print ("x = ",x)
        #print ("x1 = ",x_)
        y,y_=y_,int(y-q*y_)
        #print("y = ",y)
        #print("y1 = ",y_) 
        a_,b_=b_,a_-q*b_
        #print("a_ = ",a_)
        #print("b_ = ",b_)
    return (a_,x,y)