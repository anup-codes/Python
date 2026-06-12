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
