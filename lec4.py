'''
lec 4
dict
tuple
'''

my_tuple = 'a','b','c','d','e'
print(my_tuple)

my_2nd_tuple = ('a','b','c','d','e')
print(my_2nd_tuple)

not_a_tuple = ('a')
print( type(not_a_tuple))

id_a_tuple = ('a',)
print(type(id_a_tuple))

print(my_tuple[1])
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[:3])
print(my_tuple[:])

my_car = {
           'color':'red',
           'maker':'toyota',
           'year': 2015
           }
print(my_car)
print(my_car['year'])
print(my_car['color'])