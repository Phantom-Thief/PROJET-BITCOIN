import unittest
from FieldElement import FieldElement


a = FieldElement(5,7)
b = FieldElement(2,7)
c = FieldElement(5,11)

class TestFieldElement(unittest.TestCase):

    
    def test__eq__(self):    
        self.assertTrue(FieldElement.__eq__(a,a))
        self.assertFalse(FieldElement.__eq__(a,c))
    
    def test__add__(self):
        self.assertEqual(FieldElement.__add__(a,b),0)
        self.assertEqual(FieldElement.__add__(a,c),False)
        self.assertFalse(FieldElement.__add__(a,None),False)
    
    def test__sub__(self):
        self.assertEqual(FieldElement.__sub__(a,b),3)
        self.assertEqual(FieldElement.__sub__(a,c),False)
        self.assertFalse(FieldElement.__add__(a,None),False)

    def test__neg__(self):
        self.assertEqual(FieldElement.__neg__(a),2)
        self.assertEqual(FieldElement.__neg__(b),5)
    
    def test__mul__(self):
        self.assertEqual(FieldElement.__mul__(a,b),3)
        self.assertFalse(FieldElement.__mul__(a,c),False)
        self.assertFalse(FieldElement.__mul__(a,None),False)
    
    def test__pow__(self):
        self.assertEqual(FieldElement.__pow__(a,2),4)
        self.assertFalse(FieldElement.__pow__(a,None),False)
    
    def test__truediv__(self):
        self.assertEqual(FieldElement.__truediv__(a,b),2.5)
        self.assertFalse(FieldElement.__truediv__(a,c),False)
        self.assertFalse(FieldElement.__truediv__(a,None),False)

    def test__floordiv__(self):
        self.assertEqual(FieldElement.__floordiv__(a,b),2)
        self.assertFalse(FieldElement.__floordiv__(a,c),False)
        self.assertFalse(FieldElement.__floordiv__(a,None),False)
    
    def test__rmul__(self):
        self.assertEqual(FieldElement.__rmul__(a,2),3)
        self.assertFalse(FieldElement.__rmul__(a,None),False)

if __name__ == '__main__':
    unittest.main() 