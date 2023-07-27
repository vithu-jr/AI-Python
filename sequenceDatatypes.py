# there are 4 types of sequence data types
# list, turple, range, dictonary

# list - using list we can store multiple values, need to use '[]' brackets
# we can add new values to the list at the end
# and we can add duplicate items in list
# length of the list is count of items in the list
# we can have different type of data types in same list

fruits = ['apple', 'orange', 'grapes', 'pears', 'mangoes']
# print(fruits[0])
# print(fruits[1])
# print(len(fruits))

# we can create a sub list from a list
# sub_fruits = fruits[1:4]
# print(sub_fruits)

# person_1 = ['Vithushan', 27, 178.2, 78.5, 'Web Developer']
# print(len(person_1))
# print(person_1[-5])

students_names = ['Samantha', 100, True, 'Chamodha', 'Ishani', 'Rishi']

sub_list = students_names[3:5]
# print(sub_list)
sub_list_2 = students_names[2:]
# print(sub_list_2)
sub_list_3 = students_names[-4:-1]
# print(sub_list_3)

# manipulating list
# students_names[1] = 100.2
# print(students_names)
# students_names[1:3] = ['Kalani', 'Vithushan']
# print(students_names)

# students_names[3:] = (200, 300, 400)
# print(students_names)

# add new items to the  list
# append is the method to add new value to a list at the last

# fruits.append('papaya')
# print(fruits)

# we also can add new value to the list at the desired place using insert method
# fruits.insert(2, 'gragon fruit')
# print(fruits)

students_names.insert(0, 'new name')
# print(students_names)

# students_names.append(sub_list_2)
# print(students_names)

# extend method is used to add new array to an existing array
students_names.extend(sub_list_2)
print(students_names)

