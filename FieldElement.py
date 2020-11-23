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


a = FieldElement(5,7)
b = FieldElement(2,7)
c = FieldElement(5,11)

print(a//b)
