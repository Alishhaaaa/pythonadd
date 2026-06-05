"""class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Alisha", 20)

print(p1.name)
print(p1.age)
"""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def full_name(self):
        return f"{self.name}{self.age}"

my_user = person("alisha", 20)
print(my_user.name)
print(my_user.age)
print(my_user)
print(my_user.full_name())
