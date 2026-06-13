'''
Problem-1: Class inheritence
Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

Total Bus fare is: 5500.0
'''


class Vehicle :

  def __init__(self,vehicle,seat):
    self.vehicle = vehicle
    self.seat = seat 

  def fare(self):
    return 100*self.seat
  

class Bus(Vehicle):

  def fare(self):
    base_fare = super().fare()
    bus_fare = base_fare + 0.1*base_fare
    return bus_fare 

veh = Vehicle('truck',50)
print(veh.fare())

bus = Bus('heheh',50)
print(bus.fare())



'''
Problem-3: Write a program that has a class Point. Define another class Location which has two objects (Location & Destination) of class Point. Also define a function in Location that prints the reflection of Destination on the x axis.
'''

class Point :
  
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def show_point(self):
    return '{},{}'.format(self.x,self.y)


class Location:
  
  def __init__(self,x1,y1,x2,y2):
    self.source = Point(x1,y1)
    self.destination = Point(x2,y2)

  def show(self):
    print('source is ', self.source.show_point())
    print('destination is', self.destination.show_point())

  def reflection(self):
    self.destination.y = -self.destination.y
    print('reflection is',self.destination.show_point())


l = Location(0,0,1,1)
l.show()
l.reflection()



'''
Problem-4: Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triamgle from Polygon and write methods to get the details of their dimensions and hence calculate the area.
'''

from abc import ABC,abstractmethod
class Polygon :

  def __init__(self,a,b):
    self.a = a
    self.b = b 

  @abstractmethod
  def area (self):
    pass

  @abstractmethod
  def dimensions(self):
    pass

class Rectangle(Polygon) :

  def area(self):
    return self.a * self.b
  
  def dimensions(self):
    # return 'dimensions are {},{}'.format(self.a,self.b)
    return f"Dimensions are {self.a}, {self.b}"


class Triangle(Polygon):

  def area(self):
    return (self.a*self.b)*0.5
  
  def dimensions(self):
    return 'dimensions are {},{}'.format(self.a,self.b)




rec = Rectangle(4,8)
print(rec.dimensions())     
print(rec.area())

tri = Triangle(2,3)
print(tri.dimensions())
print(tri.area())

