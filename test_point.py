import unittest
from FieldElement import FieldElement
from FieldElement import Point

x1= FieldElement(0,5)
x2= FieldElement(1,5)
x3= FieldElement(3,5)


a= FieldElement(2,5)
b= FieldElement(1,5)

v= Point(x1,x2,a,b,False)
# v1= Point(x1,x3,a,b,False)
u= Point(x2,x3,a,b,False)
z= Point(x1,x2,a,b,True)
# z1= Point(x3,x1,a,b,True)
# z2= Point(x3,x2,a,b,True)

r1= FieldElement(1,5)
r3= FieldElement(3,5)
class TestPoint(unittest.TestCase):

    def test_eq_(self):
        self.assertTrue(Point.__eq__(v,v))
        self.assertFalse(Point.__eq__(v,u))
        self.assertFalse(Point.__eq__(v,None))

    def test_add_(self):
        self.assertEqual(Point.__add__(v,None),v)
        self.assertEqual(Point.__add__(None,v),v)
        self.assertEqual(Point.__add__(z,v),v)
        self.assertEqual(Point.__add__(v,z),v)
        self.assertEqual(Point.__add__(v,v),Point(r1,r3,a,b,False))
        # self.assertEqual(Point.__add__(z1,z2),Point(x1,x2,a,b,True))
        self.assertEqual(Point.__add__(v,u),Point(r3,r3,a,b,False)) 
        # self.assertEqual(Point.__add__(z2,z1),Point(x1,x2,a,b,True))


if __name__ == '__main__':
    unittest.main() 