# python tuples are immutable or unchangaable
# we use () to define tuples

sports = ('cricket', 'football', 'tennis')
# print(type(sports))
# print(len(sports))
# print(sports)

# if you want to create a tuple with a single element, always add ',' after the first elememnt

sports_1 = ('Hockey',)
# print(type(sports_1)) #output <class 'tuple'>

sports_2 = ('hockey')
# print(type(sports_2)) #output <class 'str'>

my_tuple = ('tennis', 30, True, 'Cricket', 'football')
my_tuple_2 = my_tuple[1:4]
# print(my_tuple_2)



# tuples are basically immutable, but we can update a tupe by converting it into a list, then we can change it back to tuple

a = ('a', 1, 'c')
# print(type(a))
b = list(a)
# print(type(b))

x = ('tennis', 'cricket', 'football')

xlist = list(x)

xlist.sort()
# print(xlist)

x = tuple(xlist)

# nested tuples

# RANGE is an in-built function
# immutable sequence of numbers 

range_x = range(3,12,2) 
# print(len(range_x)) #3,5,7,9,11

# in the syntax 1st part is starting point, next is end of range and last is increment or decrement
