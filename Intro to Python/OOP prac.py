#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)


class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print('Hello my name is' +self.name)

p1 = Person('Winnie',36)
p1.myfunc()


class Person:
    def __init__(self,colour,height):
        self.colour = colour
        self.ht= height
    def myfunc(self):
        print('my height is'+str(self.ht))

p1 =Person('black',200)
p1.myfunc()

class Students:
    def __init__(self,colour,height):
        self.ht = height
        self.col = colour
    def my_func(self):
        print('The Students height is '+str(self.ht))

p1 = Students('black',168)
p1.my_func()


class Stationaries:
    def __init__(self,pages,length):
        self.pages = pages
        self.len = length

    def func(self):
        print('The book height is ' +'colour')

p1 = Stationaries('blue',300)
p1.func()















