# dictionaries are used to store values in key: value pair

new_dict = {
    'name' : 'Vithushan',
    'age': 27,
    'education' : 'HNDIT'
}

# print(new_dict)#^ output->{'name': 'Vithushan', 'age': 27, 'education': 'HNDIT'}

# a dictionary is ordered changeable not allow duplicate values
# if we try to add duplicate key, the last entry will over-write the previous one

# we can access value using the key value
# print(new_dict['age'])#output-> 27
# print(f'age is {new_dict["age"]}')

# there's another method called get to access values
# print(new_dict.get('name'))
# print(f'name is {new_dict.get("name")}')

# & change the dictionary value 
# new_dict['education'] = 'BIT'
# print(new_dict)

#& we can change the dictionary value using in-built method called update()
new_dict.update({'education':'bit'})
# print(new_dict) #^ output-> {'name': 'Vithushan', 'age': 27, 'education': 'bit'}

#& to add a new item to the dictionary
new_dict['hometown'] = 'Vavuniya'
# print(new_dict)#^ {'name': 'Vithushan', 'age': 27, 'education': 'bit', 'hometown': 'Vavuniya'}

#& to remove an item to the dictionary using pop method, using this method we can remove any value from the dictionary using key
new_dict.pop('hometown')
# print(new_dict)#^ output-> {'name': 'Vithushan', 'age': 27, 'education': 'bit'}

#& to remove an item to the dictionary using popitem, this can remove only the last item
new_dict.popitem()
# print(new_dict)#^ output-> {'name': 'Vithushan', 'age': 27}

#& to remove an item to the dictionary using del
del new_dict['age']
# print(new_dict)#^ output-> {'name': 'Vithushan'}

#! del new_dict will remove the whole dictionary from the memory, but
#! if we use clear method, it'll only clear the properties of the dictionary, not the actual dictionary

#& to copy a dictionary using copy method
new_dict_2 = new_dict.copy()
# print(new_dict_2)

#& to copy a dictionary using constructor method
new_dict_3 = dict(new_dict_2)
new_dict_3['age'] = '27'
# print(new_dict_3)#^ output-> {'name': 'Vithushan', 'age': '27'}

#& nested dictionaries
student = {
    'name' : 'john',
    'age':15,
    'marks':{
        'maths':'A',
        'science':'B',
        'english':'A'
    }
}

print(student['marks']['english'])