import numpy as np
import matplotlib.pyplot as plt

class Point(object):
    """
    Create a single point. 

    """
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, Q):
        return (self.x, self.y) == (Q.x, Q.y) 
          
############################
class EllipticCurve(object):
    """Represents a single elliptic curve defined over a finite field.

    p must be prime, since we use the modular inverse to compute point
    addition.

    """
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def has_point(self, x, y):
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

    def __str__(self):
        return 'y^2 = x^3 + {}x + {}'.format(self.a, self.b)

def mod_inverse(a,n):
    """Return the inverse of a mod n.

    n must be prime.

    >>> mod_inverse(42, 2017)
    1969

    """
    b = n
    if abs(b) == 0:
        return (1, 0, a)

    x1, x2, y1, y2 = 0, 1, 1, 0
    while abs(b) > 0:
        q, r = divmod(a, b)
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

    return x2 % n

def addPoint(p1,p2,p,a):
    if p1 == p2:
        S = ((3*p1.x + a)*mod_inverse(2*p1.y,p))%p
        X = (S**2 - 2*p1.x)%p
        Y = (S*(p1.x-X)-p1.y)%p
        C = Point(X,Y)
        return C
    else:
        S =((p2.y-p1.y)*mod_inverse(p2.x-p1.x,p))%p
        X = (S**2-p1.x-p2.x)%p
        Y = (S*(p1.x-X)-p1.y)%p
        C = Point(X,Y)
        return C   

############################
def main(x1,y1,x2,y2):
    E = EllipticCurve(2,1,5)
    A = Point(x1,y1)
    B = Point(x2,y2)
    C = addPoint(A,B,E.p,E.a)
    print(C)

if __name__ == '__main__':
    main(0,1,1,3)