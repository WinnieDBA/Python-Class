# class Person():
#     name = 'Winnie'
#     num_legs = 2
#
#
# p1 = Person()
# print(p1.name)
# print(p1.num_legs)

#functions in a class are called methods....it has an arguement called self.


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print('Hello my name is' + ' '+self.name)

p1 = Person('Winnie',36)
p1.myfunc()


