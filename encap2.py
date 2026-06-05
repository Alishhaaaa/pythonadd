class Car:
     def __init__(self, brand, model, battery_size):
        self.brand  = brand
        self.model = model
        self.battery_size = battery_size
     def full_name(self):
        return f"{self.brand} {self.model}"
my_car = Car("toyota", "camry", "100kwh")
print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
print(my_car)
print(my_car.full_name())
