import unittest
import PointAdd

class TestPoint(unittest.TestCase):

    def test_mod_inverse(self):
        result = PointAdd.mod_inverse(42,2017)
        self.assertEqual(result,1969)
