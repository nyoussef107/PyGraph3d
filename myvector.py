import math

class V:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __eq__(self,other):
        if math.isclose(self.i,other.i)and math.isclose(self.j,other.j)and math.isclose(self.k,other.k):
            return True
        return False
        
    def __ne__(self,other):
        if not math.isclose(self.i,other.i)or not math.isclose(self.j,other.j)or not math.isclose(self.k,other.k):
            return True
        return False
        
    # def __print__(self):
    #     print(self.i,self.j,self.k)
        
    def print(self):
        print('V(%g, %g,%g)' % (self.i, self.j, self.k))

    def __add__(self,other):
    # result = V(0,0,0)
        x=V(self.i+other.i, self.j+other.j, self.k+other.k)
    #    result.i=x[0]
    #    result.j=x[1]
    #    result.k=x[2]
        return x
    
    def __sub__(self,other):
        result = V(self.i-other.i, self.j-other.j, self.k-other.k)
        return result
    
    
    
    def __truediv__(self,other):
        result = V(self.i/other, self.j/other, self.k/other)
        return result
    
    def __isub__(self, other):
        self.i-=other.i
        self.j-=other.j
        self.k-=other.k
        return self
    
    def __iadd__(self, other):
        self.i+=other.i
        self.j+=other.j
        self.k+=other.k
        return self
    
    def __imul__(self, other):
        self.i*=other
        self.j*=other
        self.k*=other
        return self
    
    def __itruediv__(self, other):
        self.i/=other
        self.j/=other
        self.k/=other
        return self
    
    def __neg__(self):
        self.i/=-1
        self.j/=-1
        self.k/=-1
        return self
    
    def __pos__(self):
        if self.i<0:
            self.i*=-1
        if self.j<0:
            self.j*=-1
        if self.k<0:
            self.k*=-1
        return self

    def __mul__(self,other):
        if not V.is_vector(other):
            # print('it works')
            result = V(self.i*other, self.j*other, self.k*other)
            return result
        else:
            return self.__rmul__(other)


    def __rmul__(self,other):
        # V.print(self)
        # V.print(other)
        # print((self.k*other.k))
        # if V.is_vector(other):
        result = (self.i*other.i)+ (self.j*other.j) +(self.k*other.k)
        return result

    def is_vector(self):
        y = str(type(self))
        if  y  == "<class '__main__.V'>":
            return True
        return False
    
    def normalize(self):
        length=math.sqrt(V.__rmul__(self,self))
        self=V.__truediv__(self,length)
        if length==0:
           raise RuntimeError('cannot normalize zero length vector')
        return self

    def project(self,other):
        # x=V(self*(V.__rmul__(self,other)/math.sqrt(V.__rmul__(other,other))))
        # x=(self*(V.normalize(other)))
        # x=((V.__rmul__(self,other))/((V.__rmul__(other,other)))*other)
        y=(V.__rmul__(self,other))/(V.__rmul__(other,other))
        # print(y,"y")
        x=V.__mul__(other,y)
        return x
    
    def gram_schmidt(self, v2, v3):
        # if math.isclose(V.__rmul__(vector,v2),0) and math.isclose(V.__rmul__(vector,v3),0) and math.isclose(V.__rmul__(v3,v2),0):
        self=self
        v2=v2-V.project(self,v2)
        v3=v3-V.project(self,v3)-V.project(v2,v3)
        if V.__eq__(self,V(0,0,0)) or V.__eq__(v2,V(0,0,0)) or V.__eq__(v3,V(0,0,0)):
            raise RuntimeError('cannot orthonormalize linearly dependent vectors')
        else:
            return V.normalize(self),V.normalize(v2),V.normalize(v3)
            
