class Person():

    height = 200
    colour = 'black'
    hair_colour ='black'

    def __init__(self,fname,secname):
        self.firstname = fname
        self.secondname = secname

    def naming(self):
         print(self.firstname,self.secondname)



class Child(Person):
    pass


p1 = Person('Winnie','Njeri')
p1.naming()


c1 = Child('David','Rudisha')
c1.naming()
# print(c1.height)


