#these functions are bulit in python

#to remove sign of a number, we can use the abs() function

# x = -1

# print(abs(x))

#map function
# nums = [1, 2, 3, 4, 5]

# def square(x):
#     return x**2

# sqr = map(square, nums)

# print(list(sqr), type(sqr))

#^map is a built in function which takes a function and a sequence datatype as parameters, what it's actually do is, it apply the function 
#^ to each element of that sequence datatype, like in the above elements, this function return a map type of data

# nums = [10, 25, 37, 41, 58]

# def divide_by_3(x):
#     reminder = x % 3
#     return reminder

# reminders = map(divide_by_3, nums)
# print(list(reminders))

#in a map function we can pass more than one sequence data types, like below
# num_1 = [10, 11, 12]
# num_2 = [20, 21, 22]

# def sum(x, y):
#     return (x + y)

# list_of_sum = list(map(sum, num_1, num_2))
# print(list_of_sum)

# nums_1 = [1, 2, 3]
# nums_2 = [10, 20, 30]

# def multiplication(x, y = 5):
#     return x * y

# multiplication_list = list(map(multiplication, nums_1, nums_2))

# print(multiplication_list)

#^ instead of below code we can write
# strings = ['1', '2', '3', '4', '5']

# def convert_to_int(x):
#     return int(x)

# integers = list(map(convert_to_int, strings))
# print(integers)

#^ in this manner
# strings = ['1', '2', '3', '4', '5']
# integers = list(map(int, strings))
# print(integers)

# todo filter(), another built in function
# ^ this function only acepts exacly 2 parameters, one function and one sequence data type
# ^ this filter function only return boolean value

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even_numbers(x):
#     return x % 2 == 0

# even_number_list = list(filter(even_numbers, numbers))
# print(even_number_list) #-> output for filter [2, 4, 6, 8, 10]

# ^ using map method
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even_numbers(x):
#     return x % 2 == 0

# even_number_list = list(map(even_numbers, numbers))
# print(even_number_list) #-> output map [False, True, False, True, False, True, False, True, False, True]

# strings = ["This is apple", "I love carrot", "This city is beautiful", "Australia has apple gardens"]

# def find_apples(x):
#     return 'apple' in x
        
# apples = list(filter(find_apples, strings))
# print(apples)


# todo python lambda functions or one-line functions
# ^ syntax -> lambda <arguments> : <expressions>
# ^ 

# sum = lambda x, y: x + y 
# print(sum(4,5))

# def tripler():
#     return lambda a: a*3
# my_double = tripler()
# num = int(input('enter a number to triple it:'))
# print(my_double(num))

# def funct(n):
#     return lambda a: a*n

# res = funct(10) #here what happen is, funct will return a lambda function, actually look like res = lambda a: a*10
# print(res(10)) # here res is holding the lambda, it'll lool like res = lamda a(a=10): a(10)*10 //return 100

# # using if in lambda

# max =  lambda a,b: a if(a>b) else b
# print(max(13,45)) 

nums = [1,2,3,4,5,6]
# is_even = lambda a: a % 2 == 0
print(list(filter(lambda a: a % 2 == 0, nums)))









