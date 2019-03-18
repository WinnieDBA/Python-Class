schools =['Mangu','Alliance','Loreto']
print(schools[1])

schools2=['Mangu','Alliance','Loreto',['pumwani','jamhuri','mama Lucy',['gashie','kamangu','Wangige']]]



languages =['python','javascript','php']
print(languages)

languages[0] ='java'
print(languages)


fruits =['mangoes','bananas','lemon']
if 'mangoes' in fruits:
    print(fruits)
fruits[2]='pineapple'
print(fruits)


flavours =['vanilla','strawberry','mango','chocolate']
print(len(flavours))


flavours =['vanilla','strawberry','mango','chocolate']

flavours.append('peach')
print(flavours)

flavours =['vanilla','strawberry','mango','chocolate']
if 'chocolate' in flavours:
    print('chocolate already exists')
else:
    print('peach does not exist')


print(len(flavours))
#adding an item in a list
#insert...it has two arguements

flavours.append('quava')
flavours.insert(2,'lemon')

print(flavours)




