import matplotlib.pyplot as plt
import numpy as np
from helper import hash256, hash160, encode_base58_checksum
from random import randint
from io import BytesIO


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
    def __init__(self,x,y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a*self.x + self.b   :
            raise ValueError("Le point ({},{}) n'est pas sur la courbe \n".format(self.x,self.y))
        else:
            print("Le point ({},{}) est sur la courbe y^2 = x^3 + {}x + {} \n".format(self.x,self.y,self.a,self.b))
    
    def __repr__(self):
        if self.x is None and self.y is None:
            return "Point(infini)"
        else:
            return "({}, {})".format(self.x, self.y)
    
    def __eq__(self,other):
      return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b
    
    def __ne__(self,other):
        return not(self == other)

    def __add__(self,other):
        if other.x is None and other.y is None:
            return self
        if self.x is None and self.y is None:
            return other
        else:

            if self == other:
                S = (3*self.x**2 + self.a)*((2*self.y).mod_inverse())
                X = S**2 - 2*self.x
                Y = S*(self.x-X)-self.y
                C = Point(X,Y,self.a,self.b)
                return C

            if self.x == other.x and self.y != other.y:
                return Point(None,None,self.a,self.b)

            if self.x != other.x:
                S = (other.y-self.y)*((other.x-self.x).mod_inverse())
                X = S**2-self.x-other.x
                Y = S*(self.x-X)-self.y
                C = Point(X,Y,self.a,self.b)
                return C  

            if self == other and self.y == FieldElement(0,self.x.prime):
                return Point(None,None,self.a,self.b)
                  
    #binary expansion
    def __rmul__(self,coefficient):
        coef = coefficient
        current = self
        result = Point(None,None,self.a,self.b)
        while coef:
            if coef & 1:
                result +=current
            current +=current
            coef >>= 1
        return result

class S256Field(FieldElement):
    def __init__(self,num):
        self.num = num
        self.prime = 2**256 - 2**32 - 977

class PrivateKey:
    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return '{:x}' .format(self.secret).zfill(64)

    def sign(self, z):
        k = randint(0, N)
        r = (k * G).x.num
        k_inv = pow(k, N-2, N)
        s = (z + r*self.secret)*k_inv%N
        return Signature(r,s)

    def wif(self, compressed=True, testnet=False):
        #Convertir la clé privée int -> 32-bytes big endian
        secret_bytes = self.secret.to_bytes(32, 'big')
        # on préfixe par b'\xef' sur testnet et par b'\x80' sur mainnet
        if testnet:
            prefix = b'\xef'
        else:
            prefix = b'\x80'
        #On ajoute b'\x01' si option compressed
        if compressed:
            suffix = b'\x01'
        else:
            suffix = b''
        #On transforme le tout par la fonction de helper.py encode _base58_checksum
        return encode_base58_checksum(prefix + secret_bytes + suffix)

class Signature(object):
    def __init__ (self,r,s):
        self.r = r
        self.s= s
    def __repr__(self):
        return 'Signature({:x},{:x})'.format(self.r, self.s)
    def der(self):
        rbin = self.r.to_bytes(32, byteorder='big')
        #on enlève tous les bits nuls au début
        rbin= rbin.lstrip('b\x00')
        #si rbin a un premier bit > 80, on ajoute \x00
        if rbin[0] & 0x80:
            rbin = 'b\x00'+rbin
        result = bytes([2, len(rbin)]) +rbin 

        sbin = self.s.to_bytes(32, byteorder='big')
        #on enlève tous les bits nuls au début
        sbin= sbin.lstrip(b'\x00')
        #si rbin a un premier bit > 80, on ajoute \x00
        if sbin[0] & 0x80:
            sbin = b'\x00'+sbin
        result = bytes([2, len(sbin)]) +sbin

        return bytes([0x30,len(result)]) + result

    @classmethod
    def parse(cls, signature_bin):
        s = BytesIO(signature_bin)
        compound = s.read(1)[0]
        if compound != 0x30:
            raise SyntaxError("Bad Signature")
        length = s.read(1)[0]
        if length + 2 != len(signature_bin):
            raise SyntaxError("Bad Signature Length")
        marker = s.read(1)[0]
        if marker != 0x02:
            raise SyntaxError("Bad Signature")
        rlength = s.read(1)[0]
        r = int.from_bytes(s.read(rlength), 'big')
        marker = s.read(1)[0]
        if marker != 0x02:
            raise SyntaxError("Bad Signature")
        slength = s.read(1)[0]
        s = int.from_bytes(s.read(slength), 'big')
        if len(signature_bin) != 6 + rlength + slength:
            raise SyntaxError("Signature too long")
        return cls(r, s)


class S256Point(Point):
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.a = S256Field(0)
        self.b = S256Field(7)

        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a*self.x + self.b   :
            raise ValueError("Le point ({},{}) n'est pas sur la courbe \n".format(self.x,self.y))
        else:
            print("Le point ({},{}) est sur la courbe y^2 = x^3 + {} \n".format(self.x,self.y,self.b))

    def __repr__(self):
        if self.x is None:
            return "S256Point(Infini)"
        else:
            return "S256Point({},{})".format(self.x,self.y)
    
    def __rmul__(self,coefficient):
        N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
        coef = coefficient %N
        P = super().__rmul__(coef)
        return S256Point(P.x,P.y)

    def SEC(self):
        tab = np.array([b'\x04',self.x.num.to_bytes(32,'big'),self.y.num.to_bytes(32,'big')])
        return tab
    
    def SECC(self):
        if(self.y.num%2==0):
            pair=True
        else:
            pair=False
        if(pair==True):
            tab = np.array([b'\02',self.x.num.to_bytes(32,'big')])
        else:
            tab = np.array([b'\03',self.x.num.to_bytes(32,'big')])    
        return tab
         

    def verify(self,z,sig):
        s_inv = pow(sig.s, N-2, N)
        u=z*s_inv%N
        v=sig.r*s_inv%N
        return (u * G + v * self).x.num == sig.r

class Tx:

    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins
        self.tx_outs = tx_outs
        self.locktime = locktime
        self.testnet = testnet

    def __repr__(self):
        tx_ins = ''
        for tx_in in self.tx_ins:
            tx_ins += tx_in.__repr__() + '\n'

        tx_outs = ''
        for tx_out in self.tx_outs:
            tx_outs += tx_out.__repr__() + '\n'

        return 'tx: {}\nversion: {}\ntx_ins:\n{}tx_outs:\n{}locktime: {}'.format(self.id(),self.version, tx_ins, tx_outs, self.locktime)

    def id(self):
        ''' version hexadécimale du hash de la transaction'''
        return self.hash().hex()

    def hash(self):
        '''hash binaire'''
        return hash256(self.serialize())[::-1]

    #@classmethod
    #def parse(cls, serialization):
    #    version = serialization[0:4]

    @classmethod
    def parse(cls, stream):
       serialized_version = stream.read(4)
    
    def serialize(self):
        result = int_to_little_endian(self.version, 4)
        result += encode_varint(len(self.tx_ins))
        for tx_in in self.tx_ins:
            result += tx_in.serialize()
        result += encode_varint(len(self.tx_outs))
        for tx_out in self.tx_outs:
            result += tx_out.serialize()
        result += int_to_little_endian(self.locktime, 4)

#version : en général 1 sauf cas particulier

#pour parser la version : convertir 4 bytes en un entier type"little-endian"

# Inputs
 # nb d'inputs
 # 1. l'Id de la transaction précédente
 # 2. l'index de la transaction précédente
 # 3. ScriptSig
 # 4. Sequence

 #Sequence and locktime : se renseigner (initialement prévu pour faire du trading haute fréquences)

class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xffffffff):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if script_sig is None:
            self.script_sig = Script()
        else:
            self.script_sig = script_sig
        self.sequence = sequence

    def __repr__(self):
        return'{}:{}'.format(self.prev_tx.hex(), self.prev_index)

    def serialize(self):
        ''' retourne une version standart en byte de l'output de la transaction'''
        result = self .prv_tx[::-1]
        result += int_to_little_endian(self.prev_index, 4)
        result += self.script_sig.serialize()
        result += int_to_little_endian(self.sequence, 4)
        return result

class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amount = amount
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return '{}:{}'.format(self.amount, self.script_pubkey)

    def serialize(self):
        result = int_to_little_endian(self.amount, 8)
        result += self.script_pubkey.serialize()


#exercice : parser les différents éléments

#coder une transaction

# a = 0 ; b = 7
#prime = 2**256 -2**32 -977
def Parse(SEC):
    x = int.from_bytes(SEC[1],byteorder='big')
    y = int.from_bytes(SEC[2],byteorder='big')
    return S256Point(S256Field(x),S256Field(y))


def plot_point(p,prime):
    irange=np.zeros(prime)
    pmulx=np.zeros(prime)
    pmuly=np.zeros(prime)

    for i in range(1,prime):
        pmul = i*p
        if pmul != Point(None,None,p.a,p.b):
            pmulx[i]=pmul.x.to_int()
            pmuly[i]=pmul.y.to_int()
            irange[i]=i
            
    plt.title('Nuage de points')   
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(pmulx,pmuly)

    for i in range(1,prime):

        label = i

        plt.annotate(label, # this is the text
                    (pmulx[i],pmuly[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
        
    plt.show()








Gx = S256Field(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798)
Gy = S256Field(0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)

G = S256Point(Gx,Gy)


#Test signature
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
sig = Signature(r,s)

px = S256Field(0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574)
py = S256Field(0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4)
#point = S256Point(px, py)
#P1 = 5000*G
#P1_SEC = P1.SEC()
#print(point.verify(z,sig))

#print(P1_SEC)

#clé priv
e = int.from_bytes(hash256(b'mon secret'), 'big')
privk= PrivateKey(e)

#signature créée
#signature= privk.sign(z)
#print(signature)

#Vérification de la signature
#point = privk.point
#print(point.verify(z,signature))

#Parse(P1_SEC)

#print("nouveau test")

#P2 = (2018**5)*G
#print(P2.SEC())


# Ptest = S256Point(S256Field(50),S256Field(150))
#Ptest= G
#PtestSEC = Ptest.SEC()
#PtestSECC = Ptest.SECC()
#print(PtestSECC)
# Parse(PtestSEC)
