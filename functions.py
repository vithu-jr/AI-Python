# there are 4 types of arguments in python
# 1-> default parameter
def greet(name, greet='hey'):
    return(f'{greet}, {name}')

# print(greet('vithu'))
# print(greet('bob','hello'))

# above method is example for default parameters, and the used method for greet is default arguments

# 2-> keyword argument is allow us to arguments not in the order of arguments, we can pass arguments with mentioning keyword

# def student(f_name, l_name):
#     print(f_name, l_name)

# student('boo', 'foo')

def check_power_even(a, b, c=2):
    if(a**b % c == 0):
        return True
    else:
        return False

# print(check_power_even(b=3, a=2))
# print(check_power_even(c=4, b=4, a=3))

# above is example for keyword argument

# 3-> positional arguments
# when passing arguments to a function without any keyword, it's positional arguments. python basically assign the values to the
# same order as in the argument list

# 3-> arbitary positional arguments is passing any number of arguments to a function

def cat_names(*names):
    for name in names:
        print (name)

# cat_names('kaipu', 'grey', 'ginger', 'snow')

def summation(*nums):
    total = 0
    for num in nums:
        total += num
    return total

# print(summation(1,2,3,4,5))

# 4-> arbitary keyword arguments is a combination of arbitary arguments + keyword arguments

# example
# def arbitrary_keyword_argements(**kwargs):

#     for key, value in kwargs.items():
#         print(f'{key} = {value}')

# arbitrary_keyword_argements(name="John", age=28, city="Colombo")

# write a function 

def summary_grades(**grades):
    total = 0
    for key,values in grades.items():
        print(f'{key}, - {values}')
        total += values
    
    print('Total is: ', total)
    print('Average is: ', total/len(grades))

summary_grades(maths=98, science=70, english=79)

# remember the argument.items() in for loop, other wise the program will throw an value error