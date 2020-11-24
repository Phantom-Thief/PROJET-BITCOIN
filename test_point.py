import unittest
from FieldElement import FieldElement
from FieldElement import Point

x1= FieldElement(0,5)
x2= FieldElement(1,5)
x3= FieldElement(3,5)

v= Point(x1,x2,2,1)
u= Point(x2,x3,2,1)

r1= FieldElement(1,5)
r3= FieldElement(3,5)
class TestPoint(unittest.TestCase):

    def test_eq_(self):
        self.assertTrue(Point.__eq__(v,v))
        self.assertFalse(Point.__eq__(v,u))
        self.assertFalse(Point.__eq__(v,None))

    def test_add_(self):
        self.assertFalse(Point.__add__(v,None))
        self.assertEqual(Point.__add__(v,v),Point(r1,r3,2,1))
        self.assertEqual(Point.__add__(v,u),Point(r3,r3,2,1)) 


if __name__ == '__main__':
    unittest.main() 