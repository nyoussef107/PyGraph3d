

from functions import *
from vector import V
from gradient import Gradient
from polygon import Polygon

def lerp(x, a, b, c, d):
   return ((x-a)/(b-a))*(d-c) + c

class ParametricSurface():
   def __init__(self, func, n):
      self.func = func.function
      self.n = n
      self.xrange = func.xrange
      self.yrange = func.yrange
      self.gradient = Gradient(func.zrange)
      self.makeHeightfield()

   def makeHeightfield(self):
      """calculate nxn 3d points in xrange x yrange
         store V(x,y,z) in self.heightfield[i,j]"""
      self.HeightField={}
      xmin,xmax=self.xrange
      ymin,ymax=self.yrange
      for i in range (self.n):
         x=lerp(i,0,self.n-1,xmin,xmax)
         for j in range (self.n):
            y=lerp(j,0,self.n-1,ymin,ymax)
            pt=self.func(x,y)
            self.HeightField[i,j]=pt


   def projectPoints(self, eye):
      """project 3d points in heightfield to
            2d points (x,y) in plane of camera
            store in self.points[i,j]
         also calculate for these points
            self.minx, maxx, miny, maxy
         also calculate color based on gradient and height and normal
            store in self.color[i,j]
         also calculate eye distance
            store in self.distance[i,j]"""
      eye
      forward=-eye
      up=V(0,0,1)
      right=V.cross(forward,up)
      forward,up,right=V.gram_schmidt(forward,up,right)
      self.points={}
      self.distance={}
      self.xmin=10**10
      self.xmax=-10**10
      self.ymin=10**10
      self.ymax=-10**10
      self.color={}
      for key in self.HeightField:
         pt=self.HeightField[key]
         x=V.__mul__(pt-eye,right)
         y=V.__mul__(pt-eye,up)
         d=(pt-eye).length()
         self.points[key]=x/d,y/d
         self.distance[key]=d
         self.color[key]= pt.z  #(pt.x*pt.y*pt.z)
         # xmin=min(xmin,x/d)
         # xmax=max(xmax,x/d)
         # ymin=min(ymin,y/d)
         # ymax=max(ymax,y/d)
         self.xmin=min(self.xmin,x/d)
         self.xmax=max(self.xmax,x/d)
         self.ymin=min(self.ymin,y/d)
         self.ymax=max(self.ymax,y/d)
      # dict=self.points
      # self.perspective={}
      # for key,value in dict:
      #    self.xmin=min(xmin,value[0])
      #    self.xmax=max(xmax,value[0])
      #    self.ymin=min(ymin,value[1])
      #    self.ymax=max(ymax,value[1])
      #    a=lerp(x,xmin,xmax,0,self.w-1)
      #    b=lerp(y,ymin,ymax,self.h-1,0)
      #    self.perspective[key]=a,b

   def scale(self,size):
      width,height=size
      xmin,xmax=self.xmin,self.xmax
      ymin,ymax=self.ymin,self.ymax
      for i in range(self.n):
         for j in range(self.n):
            x,y=self.points[i,j]
            a=lerp(x,xmin,xmax,0,width-1)
            b=lerp(y,ymin,ymax,height-1,0)
            self.points[i,j]=a,b

   

   def makePolygons(self,eye,size):
      self.projectPoints(eye)
      self.scale(size)
      n=self.n
      pts=self.points
      d=self.distance
      # color='#0000ff' 
      polys=[]
      self.shade={}
      for i in  range(n-1):
         for j in  range(n-1):
            x=self.color[i,j]
            # x='#0000ff'
            d1=d[i,j]
            d2=d[i+1,j]
            d3=d[i+1,j+1]
            d4=d[i,j+1]
            origin=self.HeightField[i,j]
            v1=self.HeightField[i+1,j]
            v2=self.HeightField[i,j+1]
            p1=v2-origin
            p2=v1-origin
            V.normalize(p1)
            V.normalize(p2)
            normal=V.cross(p2,p1)
            light_vect=V(2,-1,4)
            # print(light_vect)
            V.normalize(light_vect)
            # print(light_vect)
            dot=normal*light_vect
            # print(dot)
            if dot>0.25:
               self.shade[i,j]=dot
            else:
               self.shade[i,j]=0.25
            color=self.gradient.color(x,self.shade[i,j])
            dist=(d1+d2+d3+d4)/4
            p1=pts[i,j]
            p2=pts[i+1,j]
            p3=pts[i+1,j+1]
            p4=pts[i,j+1]



            p=Polygon([p1,p2,p3,p4],color,dist)
            polys.append(p)
            # Polygon.sort_polygons(polys)
            polys = sorted(polys, key=lambda x: x.distance, reverse=True)
            self.polygons=polys
            
            # with open("file.txt","w") as file:
            #    for i in self.polygons:
            #           file.write(str(i.distance))
            
   def normal(self, i, j):
      """find normal to surface at self.heightfield[i,j]
         use cross product of vectors from [i,j] to [i+1,j]
         and from [i,j] to [i,j+1]"""
      v1=self.HeightField[i+1,j]-self.HeightField[i,j]
      v2=self.HeightField[i,j+1]-self.HeightField[i,j]
      norm=V.cross(v1,v2)


      pass
      
   # def makePolygons(self, eye):
   #    """project the points with self.projectPoints(eye)
   #       then build polygons from self.points, self.color, self.distance
   #       using [i,j], [i+1,j], [i+1,j+1], [i,j+1] indices
   #       then sort the polygons based on distance (farthest first)
   #    """
   #    self.polygons = [Polygon([(100,100), (200,100), (200,200), (100,200)],
   #                            '#0000ff',
   #                            1.0),
   #                      Polygon([(150,150), (250,150), (250,250), (150,250)],
   #                            '#ff0000',
   #                            2.0)
   #                      ]
      
      
   # def scale(self, size):
   #    '''loop over all the points in all the polygons
   #       lerping their x,y from minx,maxx and miny,maxy ranges
   #       into screen size ranges, flipping y
   #       optional: first shrink the screen range 10% if you like
   #       modifies points in place
   #    '''
   #    pass
   
               
      
      
      
      
      
         
