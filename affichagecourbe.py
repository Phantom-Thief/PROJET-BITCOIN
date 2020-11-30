import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def main(a,b,c):

    x = domaine(a,b,c)
    graph(a,b,x)
    
def domaine(a,b,c):
    if a >= 0 :
        x1=a
        x=pow(x1,3) + a*x1 + b
        while x>0 :
            x=pow(x1,3) + a*x1 + b
            x1=x1-c
        print(x1)
        x = np.linspace(x1,10,100000)
        
    if a < 0 :
        
        x1=sqrt(-a/3)
        x2=-sqrt(-a/3)
        
        if pow(x1,3)+a*x1+b >= 0 :
            zero1=pow(x2,3) + a*x2 + b
            while zero1>=0 :
                zero1=pow(x2,3) + a*x2 + b
                x2=x2-c
            x = np.linspace(x2,100,100000)     
            
            
        else :
            x2prime = x2
            zero1 = pow(x1,3) + a*x1 + b
            zero2 = pow(x2,3) + a*x2 + b
            zero3 = pow(x2prime,3) + a*x2prime + b
            while zero1<0 :
                zero1=pow(x1,3) + a*x1 + b
                x1=x1+c
                
            while zero2>0 :
                zero2=pow(x2,3) + a*x2 + b
                x2=x2+c
            while zero3>0 :
                zero3=pow(x2prime,3) + a*x2prime + b
                x2prime=x2prime-c
                
            x = np.concatenate((np.linspace(x1,100,100000),np.linspace(x2prime,x2,100000)))
            
    return x

def graph(a,b,x):
    
    y = pow(x,3) + a*x + b
    plt.ylim([-5,5])
    plt.xlim([-5,5])
    plt.plot(x,y**2)
    plt.plot(x,-y**2)
    
    
if __name__ == '__main__':
    main(0.5,1,0.00001)