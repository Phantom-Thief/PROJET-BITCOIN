class FieldElement(object):
    def __init__(self,num,prime):
        if num >= prime or num < 0:
            error = "L'attribut num = {} n'est pas dans le corps 0....{}".format(num,prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
    def __repr__(self):
        return "{}".format(self.num)
    
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
        
        elif isinstance(other,int):
            return (self.num - other) % self.prime

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

    def to_int(self):
        return self.num


 

class Point(object):
    def __init__(self,x,y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a*self.x + self.b :
            raise ValueError("Le point ({},{}) n'est pas sur la courbe \n".format(self.x,self.y))
        else:
            print("Le point ({},{}) est sur la courbe \n".format(self.x,self.y))
    
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
                S = (3*self.x + self.a)*(FieldElement(2*self.y,y.prime).mod_inverse())
                #S = ((3*self.x + a)*mod_inverse(2*self.y))
                X = (S**2 - 2*self.x)
                X = FieldElement(X,x.prime)
                Y = (FieldElement(S*(self.x-X),x.prime)-self.y)
                Y = FieldElement(Y,x.prime)
                C = Point(X,Y,self.a,self.b)
                return C
            else:
                S = (other.y-self.y)*(FieldElement(other.x-self.x,x.prime).mod_inverse())
                #S =((p2.y-self.y)*mod_inverse(other.x-self.x))
                X = (S**2-self.x.to_int()-other.x.to_int())
                X = FieldElement(X,x.prime)
                Y = (FieldElement(S*(self.x-X),x.prime)-self.y)
                Y = FieldElement(Y,x.prime)
                C = Point(X,Y,self.a,self.b)
                return C  

    #def __rmul__




x = FieldElement(0,5)
y = FieldElement(1,5)

p1=Point(x,y,2,1)

x2 = FieldElement(1,5)
y2 = FieldElement(3,5)

p2=Point(x2,y2,2,1)

print(p1+p2)
