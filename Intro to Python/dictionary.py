person = {}#empty dict
person2 = dict()#empty
print(type(person))

person3 ={
    'first_name':'Winnie','second_name':'Njeri','age':50
}
print(person3)

print(person3['first_name'])

winnie_name = person3['first_name']
winnie_age = person3['age']
print(winnie_age,winnie_name)


person3 ={
    'first_name':'Winnie','second_name':'Njeri','age':50
}

miaka = person3.get('age')

print(miaka)

#getting

fruits ={
    'lemons':20,'oranges':40,'mangoes':50
}
print(fruits)

number_lemon = fruits['lemons']
print(number_lemon)

fruits ={
    'lemons':20,'oranges':40,'mangoes':50
}
fruits['mangoes'] = 90
print(fruits)
#adding to the list

fruits['bananas'] =32
print(fruits)



#loop the keys only using FOR LOOP
for each_key in fruits:
    print(each_key)

#values
for each_key in fruits:
    print(fruits[each_key])



#storing keys or values in a list from the dictionary

keys =[]

for each_key in fruits:
    keys.append(each_key)

print(keys)


fruits ={
    'lemons':20,'oranges':40,'mangoes':50
}

















