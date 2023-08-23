# there are 4 types of sequence data types
# list, turple, range, dictonary

# list - using list we can store multiple values, need to use '[]' brackets
# we can add new values to the list at the end
# and we can add duplicate items in list
# length of the list is count of items in the list
# we can have different type of data types in the same list

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
sub_list_3 = students_names[-1:-4]
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

# extend method is used to add new list to an existing list
students_names.extend(sub_list_2)
# print(students_names)

# we can remove a value from a list using remove command
fruits.remove('apple')
# print(fruits)

# we can remove the item using index, using pop method and without the specific index, pop method will remove the last element of the list
fruits.pop(2)
# print(fruits)

# alternate to above methods there's a delete method also
del fruits[1]
# print(fruits)

# we can use this method to delete this whole list
del fruits
# print(fruits)

# there's another method is clear, which will clear the list's elements not the list
# print(sub_list)
sub_list.clear()
# print(sub_list)

my_list = ["banana", "apple", "carrot", "orange"]

my_list.sort()

# print(my_list)

my_list_2 = [100, 25, 78, 99]

my_list_2.sort(reverse=True)

# print(my_list_2)

my_list_3 = ["banana", "apple", "carrot", "orange",'100', '25', '78', '99']

my_list_3.sort()

# print(my_list_3)

animals = ['dog', 'cat', 'Lion', 'Rat', 'Fish']

# animals.sort()

# print(animals)

# the sort function is case sensitive, which means it usually give priority to the capital first
# if we need to ignore the case sensitive we can use the key = str.lower

animals.sort(key=str.lower)

# print(animals)

animals_1 = ['dog', 'cat', 'lion']

animals_2 = []

animals_2 = animals_1.copy()

animals_2.append('deer')

print(animals_1)
print(animals_2)

# copy method is used  to make a copy of original list, if we do like animals_2 = animals_1 now the both lists are referencing the same 
# memory, so if we make any changes in both lists, both lists will be affected

# combining 2 lists

animals_3 = animals_2 + animals_1

# print(animals_3)