# dictionaries are used to store values in key: value pair

new_dict = {
    'name' : 'Vithushan',
    'age': 27,
    'education' : 'HNDIT'
}

print(new_dict)#^ output->{'name': 'Vithushan', 'age': 27, 'education': 'HNDIT'}

# a dictionary is ordered changeable not allow duplicate values
# if we try to add duplicate key, the last entry will over-write the previous one

# we can access value using the key value
# print(new_dict['age'])
# print(f'age is {new_dict["age"]}')

# there's another method called get to access values
# print(new_dict.get('name'))
# print(f'name is {new_dict.get("name")}')

# & change the dictionary value 
# new_dict['education'] = 'BIT'
# print(new_dict)

#& we can change the dictionary value using in-built method called update()
new_dict.update({'education':'bit'})
print(new_dict) #^ output-> {'name': 'Vithushan', 'age': 27, 'education': 'bit'}
