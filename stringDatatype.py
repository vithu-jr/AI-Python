hello = ''' To learn and test React, you should set up a React Environment on your computer.

This tutorial uses the create-react-app.

The create-react-app tool is an officially supported way to create React applications.

Node.js is required to use create-react-app.

Open your terminal in the directory you would like to create your application.

Run this command to create a React application named my-react-app:'''

# print(len(hello)) #output-> 405

# triple quotes in string is used to define multiple line of strings
# string is also a list like

# the in method is used to, whether a specific word or character in a string, for example

# print('r' in hello)#output->true

# the not in method is used to, whether a specific word or character not in a string, for example

# print('reactJS' not in hello)#output->true
# print('react' not in hello)#output->false

# print(hello.count('react'))#output-> 4
# above method is used to count the apperances of a specific word in string 

test = 'Sri Lanka is a beautiful country!'

text = 'hello world'
# print(text[4:11])

# string manipulation
# to change the letters to upper case
# print(text.upper())#output-> HELLO WORLD

# to change the letters to lower case
# print(text.lower())#output-> hello world

# to remove whitespaces from a string, to be more specific this method only remove white spaces from before and after part of the string, not middle
# name = ' vithu shan  '
# print(name.strip())#output->'vithu shan'

# print(text.replace('h','t'))#output-> tello world
# this replace method is used to replace a specific character in a string

# print(test.replace('country', 'island'))#output->Sri Lanka is a beautiful island!

# split a string
# this method is used to split a string into a list using a specific seperator
# sub_test = test.split(' ')# test = 'Sri Lanka is a beautiful country!'
# print(sub_test)#output->['Sri', 'Lanka', 'is', 'a', 'beautiful', 'country!']
# above we have splited the test string into a list, with using ' ' as the separator
# for x in sub_test:
#     x[0] = x[0].upper()
#     print(x[0])


# write a program to 
# 'sir what if the user inserting everything in caital 
# but we want to convert the first letter of the word in captal how to do that'

# my_var = 'Tennis is my favourite sport'
# my_var_1 = my_var.split(' ')
# print(my_var_1)

# string concatenation
# we can use '+' to concatenate two strings
word_1 = 'Hello'
word_2 = 22

text_1 = word_1 + str(word_2)
# print(text_1)#output->Hello22

# we can't concatenate 2 different types of datatypes
#but we can use f-string to concatenate

# print(f"my name is {word_1}, i am {word_2} years old")#output-> my name is hello, i am 22 years old

# product = 'sugar'
# price = 200.50
# quantity = '1 kg'

# print(f'price of {product} {quantity} is {price} lkr')

# escape character 
print('the exact word for sugar is \'sugar cane\'')
