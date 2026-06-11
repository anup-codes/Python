'''
Write OOP classes to handle the following scenarios:
A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line
'''
class point:

  def __init__(self,x,y):
    self.x_cod= x
    self.y_cod = y

  
  def __str__(self):
    return '<{},{}>'.format(self.x_cod,self.y_cod)

  def eucliden_distance(self,other):
    return ((self.x_cod - other.x_cod)**2 +(self.y_cod - other.y_cod)**2)**0.5

  def origin_distance(self):
    # return(((self.x_cod)**2 + (self.y_cod)**2)**2)
    return self.eucliden_distance(point(0,0))


class Line :

  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C

  def __str__(self):
    return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)

  def point_on_line(self,point):
    self.d  = self.A*point.x_cod + self.B*point.y_cod + self.C
    print(self.d)
    if self.d == 0 :
      return "point lies on the line"
      
    else:
      return "point not lies on the line"
    

  def point_line_distance(self,point):
    
    dis = abs(self.d)/((self.A)**2+ (self.B)**2)**0.5
    return dis

  def intersection_of_line (self,other):
    m1 = -self.A/self.B
    m2 = -other.A/other.B


    if m1 == m2:
      if self.A*other.B == other.A*self.B and self.A*other.C == other.A*self.C :
        return 'intersect at many point(coinside each other)'
      else:
        return 'parallel to each other '

    elif m1 != m2 :
      return 'this lines are intersecting'
    
    else:
      pass
    


  

# p1 = point(1,1)
# p2 = point(1,0)
# print(p1.eucliden_distance(p2))
# print(p1.origin_distance())



# p3 = point(-1,1)
# print(l1.point_on_line(p3))
# print(l1.point_line_distance(p3))

l1 = Line(1,1,-4)
l2 = Line(1,-1,-2)
print(l1.intersection_of_line(l2))

l3 = Line(1,1,-2)
l4 = Line(2,2,-5)
print(l3.intersection_of_line(l4))

l5 = Line(1,1,-2)
l6 = Line(2,2,-4)
print(l5.intersection_of_line(l6))
