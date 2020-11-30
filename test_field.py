import unittest
from FieldElement import FieldElement


a = FieldElement(5,7)
b = FieldElement(2,7)
c = FieldElement(5,11)
error = "Les nombres ne font pas parti du même corps"

class TestFieldElement(unittest.TestCase):

    
    def test__eq__(self):    
        self.assertTrue(FieldElement.__eq__(a,a))
        self.assertFalse(FieldElement.__eq__(a,c))
    
    def test__add__(self):
        self.assertEqual(FieldElement.__add__(a,None),a)
        self.assertRaises(ValueError,FieldElement.__add__,a,c)
        self.assertEqual(FieldElement.__add__(a,b),FieldElement(0,7))
        
    
    def test__sub__(self):
        self.assertEqual(FieldElement.__sub__(a,b),FieldElement(3,7))
        self.assertRaises(ValueError,FieldElement.__sub__,a,c)
        self.assertEqual(FieldElement.__add__(a,None),a)

    def test__neg__(self):
        self.assertEqual(FieldElement.__neg__(a),FieldElement(2,7))
        self.assertEqual(FieldElement.__neg__(b),FieldElement(5,7))
    
    def test__mul__(self):
        self.assertEqual(FieldElement.__mul__(a,None),FieldElement(0,7))
        self.assertRaises(ValueError,FieldElement.__mul__,a,c)
        self.assertEqual(FieldElement.__mul__(a,b),FieldElement(3,7))
        
        
    def test__pow__(self):
        self.assertEqual(FieldElement.__pow__(a,None),FieldElement(1,7))
        self.assertEqual(FieldElement.__pow__(a,2),FieldElement(4,7))
        
    
    def test__truediv__(self):
        self.assertEqual(FieldElement.__truediv__(a,None),a)
        self.assertRaises(ValueError,FieldElement.__truediv__,a,c)
        self.assertEqual(FieldElement.__truediv__(a,b),FieldElement(6,7))
        
        

    def test__rmul__(self):
        self.assertEqual(FieldElement.__rmul__(a,2),FieldElement(3,7))
        self.assertEqual(FieldElement.__rmul__(a,None),FieldElement(0,7))

if __name__ == '__main__':
    unittest.main() 