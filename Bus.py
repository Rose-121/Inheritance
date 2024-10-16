class Vehicle:
    
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity *100
    
class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()
        amount = amount+((amount*10)/100)
        return amount
    
SchoolBus = Bus("School Volvo", 180, 12, 50)

print(f"Vehiocle name : {SchoolBus.name}\nspeed : {SchoolBus.max_speed} \nMileage: {SchoolBus.mileage}")
print(f"\nBUS FARE = {SchoolBus.fare()}")    