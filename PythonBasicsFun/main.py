import math 

# this is a one line comment
# a line of "code" that is ignored by Python when it runs the program
# we use comments to document our code

'''
this is a multi line
comment
AKA a block comment

asdlfkjas
sdflkj;s
'''

# VARIABLES
x = 5 # "x is assigned 5" or "x stores 5" NOT "x equals 5"
print(x)
# a variable stores a value
# the value has a "data type" which defines the range of values
# int (short for integer) is a data type that stores integers (whole numbers)
print(type(x))
# let's overwrite x with a new value
x = 5.5
print(x)
print(type(x))
# float is a data type that stores decimal numbers (numbers with a fractional part)
x = "hello"
print(x)
print(type(x))
# a string is a data type that stores a sequence of characters

# OPERATORS
# * is multiplication
print(4 * 5)
# / is floating point division (this is the "normal" division)
print(5 / 2)
# // is integer division (this is just the whole number results of division)
print(5 // 2) 
# % is modulus (this is the remainder from integer division)
print(5 % 2) 
# ** is exponentiation (power)
print(2 ** 5)
# we have a pow() function for exponentiation, it is in the math module
# we have to "import" the math module
print(math.pow(2, 5))

print("hello world")

# GETTING INPUT FROM THE USER
print("Enter your favorite number: ")
favorite_number = input()
print("Your favorite number is: ", favorite_number)
print("Your favorite number doubled is: ", 2 * favorite_number)
print(type(favorite_number))
# let's say, we really do want favorite_number to be a numeric type
# e.g. int or float
# this is called type conversion
favorite_number_int = int(favorite_number)
print(type(favorite_number_int))
print("Your favorite number doubled is:", favorite_number_int * 2, sep="", end=":):)")
print() 

# FORMATTING floating point numbers
# a few ways to do this
print(math.pi)
print("%.2f" %(math.pi)) # C/C++ styles (old skool)
print("{:.2f}".format(math.pi)) # Pythonic way
# this last approach actually rounds the number (you can store it rounded)
print(round(math.pi, 2))
