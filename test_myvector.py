import unittest
import myvector
import math
from myvector import V

'''def main():'''

class test_vector(unittest.TestCase):

    def test__add__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        self.assertAlmostEqual(x+y,V(2,4,6))
        "Should be V(2,4,6)"
    def test__sub__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        self.assertAlmostEqual(x-y,V(0,0,0))
        "Should be V(0,0,0)"
    def test__mul__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        self.assertAlmostEqual(x*10,V(10,20,30))
        "Should be V(10,20,30)"
    def test__truediv__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        self.assertAlmostEqual(x/10,V(0.1,0.2,0.3))
    def test__eq__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        assert x==y, "Should be True"
    def test__ne__(self):
        x=V(1,2,3)
        y=V(12,2,3)
        assert x!=y, "Should be True"
    def test__iadd__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        x+=y
        self.assertAlmostEqual(x,V(2,4,6))
        "Should be V(2,4,6)"
    def test__isub__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        x-=y
        self.assertAlmostEqual(x,V(0,0,0)),"Should be V(0,0,0)"
    def test__imul__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        x*=10
        self.assertAlmostEqual(x,V(10,20,30)), "Should be V(10,20,30)"
    def test__itruediv__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        x/=10
        self.assertAlmostEqual(x,V(0.1,0.2,0.3)), "Should be V(0.1,0.2,0.3)"
    def test__neg__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        -x
        self.assertAlmostEqual(x,V(-1,-2,-3)), "Should be V(-1,-2,-3)"
    def test__pos__(self):
        y=V(-1,-2,-3)
        V.__pos__(y)
        # V.print(y)
        self.assertAlmostEqual(V(1,2,3),y), "Should be V(1,2,3)"
    
    def test__rmul__(self):
        x=V(1,2,3)
        y=V(1,2,3)
        # V.print(x*y)
        # print("######################^^^", x*y)
        self.assertAlmostEqual(14,V.__rmul__(x,y)), "Should be 14"
    def test_normalize(self):
        x=V(1,2,3)
        y=V(1,2,3)
        self.assertAlmostEqual(V.normalize(x),V(1/math.sqrt(14),2/math.sqrt(14),3/math.sqrt(14))), "Should be V(0.267,0.534,0.801)"
    def test_project(self):
        x=V(1,2,3)
        y=V(1,2,3)
        self.assertAlmostEqual(V.project(x,y),x), "Should be V(1,2,3)"
    def test_gram_schmidt(self):
        x=V(1,1,1)*3
        y=V(1,-2,3)*4
        z=V(1,3,-2)*5
        x,y,z= x.gram_schmidt(y,z)
        self.assertAlmostEqual(V.__rmul__(x,x),1), "Should be V(0.57735 , 0.57735 , 0.57735)"
        self.assertAlmostEqual(V.__rmul__(y,y),1), "Should be V(0.57735 , 0.57735 , 0.57735)"
        self.assertAlmostEqual(V.__rmul__(z,z),1), "Should be V(0.57735 , 0.57735 , 0.57735)"
        # x=V(1,0,0)
        # y=V(0,1,0)
        # z=V(0,0,1)
        # x,y,z=x.gram_schmidt(y,z)
        # self.assertAlmostEqual(x,V(1 , 0 , 0)), "Should be V(1,0,0)"
        # self.assertAlmostEqual(y,V(0 , 1 , 0)), "Should be V(0,1,0)"
        # self.assertAlmostEqual(z,V(0 , 0 , 1)), "Should be V(0,0,1)"
       
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")