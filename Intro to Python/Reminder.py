class Person:
    def __init__(self,colour,height):
        self.rangi = colour
        self.urefu = height
    def myfunc(self):
        print('Hello my height is ' + str(self.urefu))
p1 = Person('black',140)
p1.myfunc()


class Breed:
    def __init__(self,colour,length):
        self.rangi = colour
        self.len = length

    def myfunc(self,fur):
        print('the colour is {} and the fur is {}'.format(self.rangi,fur))


B1 = Breed('white',20)
B1.myfunc('fluffy')


class Quality:
    def __init__(self,textuere,colour):
        self.tex = textuere
        self.col = colour

    def fun_quan(self,height,appearance):
        print('The texture should be {} and should be {}'.format(self.tex,appearance))


q1 = Quality('smooth','black')
q1.fun_quan(168,'slender')



class Circumfrence:

    p = 3.14

    def __init__(self,radius):
        self.radius = radius


    def calculate(self):
        area = self.p*self.radius*self.radius
        print(area)


c1 = Circumfrence(7)
c1.calculate()

