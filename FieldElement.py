class FieldElement(object):
    def __init__(self,num,prime):
        if num >= prime or num < 0:
            error = "L'attribut num = {} n'est pas dans le corps 0....{}".format(num,prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime,self.num)
    
    def __eq__(self,other):
        if other is None:
            return False
        else:
            return self.num == other.num and self.prime == other.prime


    #def __ne__(self,other): 
        

    def __add__(self,other):
        if other is None:
            return False
        
        elif self.prime != other.prime:
            return False
    
        else:
            return (self.num + other.num) % self.prime 

    def __sub__(self,other):  
        if other is None:
            return False
        
        elif self.prime != other.prime:
            return False

        else:
            return (self.num - other.num) % self.prime 
    
    def __neg__(self):
        return (-self.num) % self.prime

    def __mul__(self,other): 
        if other is None:
            return False
        
        elif self.prime != other.prime:
            return False
    
        else:
            return (self.num * other.num) % self.prime 

    def __pow__(self,val):
        if val is None:
            return False
        else :
            return (self.num ** val) % self.prime 
        
    def __truediv__(self,other):
        if other is None:
            return False
             
        elif self.prime != other.prime:
            return False

        else:
            return (self.num / other.num) % self.prime

    def __floordiv__(self,other):
        if other is None:
            return False
             
        elif self.prime != other.prime:
            return False

        else:
            return (self.num // other.num) % self.prime

    def __rmul__(self,val):
        if val is None:
            return False

        else:
            return (self.num * val) % self.prime
        
    def mod_inverse(self):

        b = self.prime
        if abs(b) == 0:
            return (1, 0, self.num)

        x1, x2, y1, y2 = 0, 1, 1, 0
        while abs(b) > 0:
            q, r = divmod(self.num, b)
            x = x2 - q * x1
            y = y2 - q * y1
            self.num, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

        return x2 % self.prime


 

class Point(object):
    def __init__(self,x,y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.x*self.a + self.b :
            raise ValueError("Le point ({},{}) n'est pas sur la courbe".format(self.x,self.y))
    
    def __repr__(self):
        if self.x is None:
            return "Point(infini)"
        else:
            return "({}, {})".format(self.x, self.y)
    
    def __eq__(self,other):
        if other is None:
            return False
        else:
            return self.x == other.x and self.y == self.y

    #def __ne__(self,):
 
    def __add__(self,other):
        if other is None:
            return False
        else:
            if self == other:
                S = (3*self.x + a)*(2*self.y.mod_inverse())
                #S = ((3*self.x + a)*mod_inverse(2*self.y))
                X = (S**2 - 2*self.x)
                Y = (S*(self.x-X)-self.y)
                C = Point(X,Y,self.a,self.b)
                return C
            else:
                S = (other.y-self.y)*((other.x-self.x).mod_inverse())
                #S =((p2.y-self.y)*mod_inverse(other.x-self.x))
                X = (S**2-self.x-other.x)
                Y = (S*(self.x-X)-self.y)
                C = Point(X,Y,self.a,self.b)
                return C  

    #def __rmul__




x = FieldElement(0,5)
y = FieldElement(1,5)

p=Point(x,y,2,1)

x2 = FieldElement(1,5)
y2 = FieldElement(3,5)

p2=Point(x2,y2,2,1)

print(p2+p)
