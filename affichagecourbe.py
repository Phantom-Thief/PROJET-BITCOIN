import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def main(a,b,c):

    x = domaine(a,b,c)
    graph(a,b,x)
    
def domaine(a,b,c):
    if a >= 0 :
        x=a
        if pow(x,3)+a*x + b < 0:
            while pow(x,3)+a*x + b < 0:
                x += c
            x -= c 
        
        else:
            while pow(x,3)+a*x + b > 0:
                x -= c
            x += c
        x_start = x
        return [x_start]
        
    else:
        
        x1=-np.sqrt(-a/3)
        x2=np.sqrt(-a/3)
        
        if pow(x1,3)+a*x1 + b < 0:
            x = x2
            while pow(x,3)+a*x + b < 0:
                x += c
            x -= c      
            return [x]
        elif pow(x2,3)+a*x2 + b > 0:
            x = x1
            while pow(x,3)+a*x + b > 0:
                x -= c
            x += c
            return [x] 
            
            
        else:
            x = x1
            while pow(x,3)+a*x + b > 0:
                x -= c
            x += c
            x_0 = x
            x = x1
            while pow(x,3)+a*x + b > 0:
                x += c
            x -= c
            x_1 = x
            x = x2
            while pow(x,3)+a*x + b < 0:
                x += c
            x_2 = x
            return [x_0,x_1,x_2] 

def graph(a,b,x):
    
    if len(x) == 1:
        x_start = x[0]
        x = np.linspace(x_start, x_start + 6, 100)

        y1 = np.sqrt(pow(x,3)+a*x + b)
        y2 = -np.sqrt(pow(x,3)+a*x + b)

        plt.plot(x,y1,x,y2, c = 'b')

        axes = plt.gca()
        axes.set_xlim([x_start-5, x_start+6])
        axes.set_ylim([x_start-5, x_start+6])
    else:
        x_0,x_1,x_2 = x
        xgauche = np.linspace(x_0, x_1, 100)
        xdroite = np.linspace(x_2, x_2+6, 100)

        ygauche1 = np.sqrt(pow(xgauche,3)+a*xgauche + b)
        ygauche2 = -np.sqrt(pow(xgauche,3)+a*xgauche + b)

        ydroite1 = np.sqrt(pow(xdroite,3)+a*xdroite + b)
        ydroite2 = -np.sqrt(pow(xdroite,3)+a*xdroite + b)

        plt.plot(xgauche,ygauche1,xgauche,ygauche2, c = 'b')
        plt.plot(xdroite,ydroite1,xdroite,ydroite2, c = 'b')
        axes = plt.gca()
        axes.set_xlim([x_0-5, x_2+6])
        axes.set_ylim([x_0-5, x_2+6])

    plt.show()
    
    
if __name__ == '__main__':
    main(-2,1,0.001)


"""import numpy as np
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
        
        print(pow((x1+c*2),3) + a*(x1+c*2) + b)
        x = np.linspace((x1+c*2),10,100000)
        
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
    
    y1 = np.sqrt(pow(x,3) + a*x + b)
    y2 = - np.sqrt(pow(x,3) + a*x + b)
    plt.ylim([-5,5])
    plt.xlim([-5,5])
    plt.plot(x,y1**2)
    plt.plot(x,y2**2)
    plt.show()
    
    
if __name__ == '__main__':
    main(1,1,0.001) """