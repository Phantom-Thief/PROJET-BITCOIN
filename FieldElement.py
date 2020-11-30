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


    def __ne__(self,other): 
        if other is None:
            return False
        else:
            return self.num != other.num or self.prime != other.prime

    def __add__(self,other):
        if other is None:
            return self
        
        elif self.prime != other.prime:
            error = "Les nombres ne font pas parti du même corps"
            raise ValueError(error)
    
        else:
            return FieldElement((self.num + other.num) % self.prime,self.prime) 

    def __sub__(self,other):  
        if other is None:
            return self
        
        elif isinstance(other,int):
            return FieldElement((self.num - other) % self.prime,self.prime)

        elif self.prime != other.prime:
            error = "Les nombres ne font pas parti du même corps"
            raise ValueError(error)

        else:
            return FieldElement((self.num - other.num) % self.prime,self.prime) 
    
    def __neg__(self):
        return FieldElement((-self.num)%self.prime,self.prime)

    def __mul__(self,other): 
        if other is None:
            return FieldElement(0,self.prime)
        
        elif self.prime != other.prime:
            error = "Les nombres ne font pas parti du même corps"
            raise ValueError(error)
    
        else:
            return FieldElement((self.num * other.num) % self.prime,self.prime) 

    def __pow__(self,val):
        if val is None:
            return FieldElement(1,self.prime)
        else :
            return FieldElement(pow(self.num,val,self.prime),self.prime) 
        
    def __truediv__(self,other):
        if other is None:
            return self
             
        elif self.prime != other.prime:
            error = "Les nombres ne font pas parti du même corps"
            raise ValueError(error)

        else:
            return FieldElement((self.num * other.num**(self.prime-2))%self.prime,self.prime)



    def __rmul__(self,val):
        if val is None:
            return FieldElement(0,self.prime)
        else:
            return FieldElement((self.num * val) % self.prime,self.prime)
        
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

        return FieldElement(x2 % self.prime,self.prime)

    def to_int(self):
        return self.num


 

class Point(object):
    def __init__(self,x,y,a,b,Infinity):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.isInfinity = Infinity

        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a*self.x + self.b   :
            raise ValueError("Le point ({},{}) n'est pas sur la courbe \n".format(self.x,self.y))
        else:
            print("Le point ({},{}) est sur la courbe y^2 = x^3 + {}x + {} \n".format(self.x,self.y,self.a,self.b))
    
    def __repr__(self):
        if self.x is None:
            return "Point(infini)"
        if self.isInfinity == True:
            return "Point(infini)"
        else:
            return "({}, {})".format(self.x, self.y)
    
    def __eq__(self,other):
      return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b and self.isInfinity == other.isInfinity
    
    def __ne__(self,other):
        return not(self == other)

    def __add__(self,other):
        if other.x is None:
            return self
        if self.x is None:
            return other
        if other.isInfinity == True:
            return self 
        if self.isInfinity == True:
            return other

        else:

            if self == other:
                S = (3*self.x**2 + self.a)*((2*self.y).mod_inverse())
                X = S**2 - 2*self.x
                Y = S*(self.x-X)-self.y
                C = Point(X,Y,self.a,self.b,False)
                return C

            if self.x == other.x and self.y != other.y:
                inf1= FieldElement(0,self.x.prime)
                inf2 = FieldElement(0,self.x.prime)
                return Point(inf1,inf2,self.a,self.b,True)

            if self.x != other.x:
                S = (other.y-self.y)*((other.x-self.x).mod_inverse())
                X = S**2-self.x-other.x
                Y = S*(self.x-X)-self.y
                C = Point(X,Y,self.a,self.b,False)
                return C  

            if self == other and self.y == FieldElement(0,self.x.prime):
                inf1= FieldElement(0,self.x.prime)
                inf2 = FieldElement(0,self.x.prime)
                return Point(inf1,inf2,self.a,self.b,True)
            
            
    def __rmul__(self,val):
        rmul = Point(None,None,self.a,self.b,False)
        for i in range(val):
            rmul = self + rmul
        return rmul





x = FieldElement(0,5)
y = FieldElement(1,5)

a = FieldElement(2,5)
b = FieldElement(1,5)

p1=Point(x,y,a,b,False)

x2 = FieldElement(1,5)
y2 = FieldElement(3,5)

p2=Point(x2,y2,a,b,False)
p3=p1+p2
p4 =p1+p3