import math 
import random 

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
# print("Enter your favorite number: ")
# favorite_number = input()
# print("Your favorite number is: ", favorite_number)
# print("Your favorite number doubled is: ", 2 * favorite_number)
# print(type(favorite_number))
# # let's say, we really do want favorite_number to be a numeric type
# # e.g. int or float
# # this is called type conversion
# favorite_number_int = int(favorite_number)
# print(type(favorite_number_int))
# print("Your favorite number doubled is:", favorite_number_int * 2, sep="", end=":):)")
# print() 

# FORMATTING floating point numbers
# a few ways to do this
print(math.pi)
print("%.2f" %(math.pi)) # C/C++ styles (old skool)
print("{:.2f}".format(math.pi)) # Pythonic way
# this last approach actually rounds the number (you can store it rounded)
print(round(math.pi, 2))

print(4 / 12)
# print(3 / 0)
print(2 ** 4 ** (2 / 4))

# warm up task
# print("Please enter the voltage:")
# voltage = input()
# voltage = float(voltage)

# resistance = float(input("Please enter the resistance:"))
# power = voltage ** 2 / resistance
# print("The power is:", power)

# CONDITIONALS (AKA if statements)
# if some condition (called boolean condition) is true, then
# execute some code
x = 7
if x == 6: # == equality operator (= assignment operator)
    print("x is 6")
    # in Python, identation (1 tab or 4 spaces) is used
    # to group code statements into a block
    # like { } in C/C++
    
# we also have an else keyword
# that we can attach to an if structure 
# else bodies only execute when the condition on the associate if is false
if x == 6:
    print("x is 6")
else: # x == 6 is false -> x != x
    print("x is NOT 6")

# we also have an elif (else if)
# use elif when you want to test multiple conditions in order
# the first one that evaluates to true, will have its body execute
# then an exit from the entire if structure
x = 5
if x < 0:
    print("x is negative")
elif x > 0: # only executes when x is not < 0 -> x >= 0
    print("x is positive")
else: # executes when all previous conditions are false (catch all)
    print("x is 0")

# you can nest if statements (pay attention to indention)

# LOOPS
# there are for loops and while loops
# both are used repeating statements
# for loop structure
# for item in sequence:
#    statements to be repeated (e.g. the body of the loop)
#    do something with the item
# lots of sequences we can use for loops
# lists are sequences!!
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# strings are sequences!!
for character in "hello":
    print(character)

# we can generate our sequences using range()
# for i in range(stop): # generates a sequence [0, stop)
for i in range(9): #[0, 9) -> [0, 8] 
    print(i, end=" ")
print()

# for i in range(start, stop): # generates a sequence [start, stop)
for i in range(4, 9): #[4, 9) -> [4, 8] 
    print(i, end=" ")
print()

# for i in range(start, stop, step): # generates a sequence [start, stop) go up by step
for i in range(4, 9, 2): #[4, 9) -> [4, 8] going up by 2
    print(i, end=" ")
print()

# task: try printing out the previous numbers in reverse: 8 6 4
# task: Write a for loop to print the first 20 even numbers all on one line 
# separated by a comma and a space (e.g. 2, 4, ..., 38, 40)
for j in range(2, 40, 2):
    print(j, end=", ")
print(j + 2)

# while loop structure
# while condition is true:
#    body of statements to be repeated
#    progress towards your condition being false (otherwise you have infinite loop)
k = 2 # loop control variable
while k <= 38:
    print(k, end=", ")
    # don't forget progress towards k > 38
    k = k + 2 # k += 2
print(k)

# ADVANCED LOOPS
# like if statements you can nest loops
# you can get an early exit from a loop using break keyword
# True False are keywords
# while True:
#     user_input = input("Enter a word (stop to quit): ")
#     if user_input == "stop":
#         break
# print("here")

# RANDOM NUMBERS
# often we need a "random" number to simulate something or to setup the 
# starting state of algorithm
# import the random module
# lets throw a 6-sided die
# if you want the same results, you can seed the generator with a constant
# this is nice for reproducibility
random.seed(0)
die_roll = random.randrange(1, 7) # [1, 7) -> [1, 6]
print("die_roll:", die_roll)

die_roll = random.randint(1, 6) # [1, 6]
print("die_roll:", die_roll)

# FUNCTIONS
# a named sequence of statements
# e.g. round(), print(), input(), etc....
# we are going to write our own
# functions take inputs (arguments when you "call" function, and parameters when
# you define function)
# functions produce outputs (return values AKA results)
# function structure
# def function_name(parameter list):
#    function body (statements that execute when the function is "called")
# calling a function means to execute it
# reasons to use functions: reusability (define once, call multiple times)
# also for organization