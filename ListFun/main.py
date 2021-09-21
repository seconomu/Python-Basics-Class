import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3
list_ints = [100, 1, 10, 20]
# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list

print(list_ints[0])
print(list_ints[-4])

# types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))
# lists are mutable (they can be changed)
list_numbers[0] = "hello"
print(list_numbers)

# use len() to find out how many elements are in a list
print(len(list_numbers))
list_numbers.append("another element")
# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list
print(list_numbers[len(list_numbers) - 1])

# we can declare an empty list!
empty_list = []
print(len(empty_list))

# we can have lists of lists (2D or ND)
nested_list = [[0, 1], [2], [3], [4, 5], []]
print(len(nested_list))
print(len(nested_list[0]))

# looping through list items
candies = ["twix", "reeses", "oreos", "snickers"]
print(candies)

for candy in candies:
    print(candy)

i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

i = 0
for i in range(len(candies)):
    print(i, candies[i])

# common list operators
# list concatenation... adding 2 lists together
print(candies)
candies += ["m&ms", "starburst"]
print(candies)
# list repetition... repeating elements in a list
bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)
# list slicing
print(candies[1:3]) # : is the slice operator. start index is inclusive
# end index is exclusive
# if you ever need a copy of a list, you can simply use the : with no start or end indices
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)

# list methods 
candies.remove("reeses")
print(candies)

# 1D LIST PRACTICE PROBLEM
random_list = []
for x in range(20):
    number = random.randrange(0,11) #randrange is exclusive, so need 11 instead of 10
    random_list.append(number)
    # or random_list.append(randrange(0,11))
print(random_list)

for x in random_list:
    print(x, end=" ")

print()
sorted_list = sorted(random_list)

#sorted_list = random_list.sort()
print(sorted_list)

print("min: ", sorted_list[0], "max: ", sorted_list[-1])
print()
print(random_list)
number = int (input("what is the number? "))
times = 0
for x in random_list:
    if x == number:
        times += 1
print(number, " appears ", times, " times.")


# 1D LIST PRACTICE PROBLEMS
'''
In ListFun, write code that generates 20 random numbers between 1 and 10 inclusive 
and puts them in a 1D list. The program then does the following using the list:
'''
numbers = []
for _ in range(20):
    numbers.append(random.randrange(1, 11))
print("numbers:", numbers)

# -Prints the numbers all one line, each number separated by a space
def pretty_print(numbers):
    for num in numbers:
        print(num, end=" ")
    print()

pretty_print(numbers)

# -Sorts the list using a list method
# numbers.sort() # in place sort (changes the order im memory)
numbers_copy = sorted(numbers)
pretty_print(numbers_copy)

# -Prints the largest and smallest number in the list
# --Hint: can you take advantage of the current ordering of your list?
print("min:", numbers_copy[0], "max:", numbers_copy[-1])
print("min:", min(numbers), "max:", max(numbers))

# -Determines the number of times a user-specified number is in the list
user_num = int(input("Please enter a number in [1, 10] to count: "))
count = 0
for num in numbers:
    if num == user_num:
        count += 1
print("count:", count)

# -Removes all instances of a user-specified number in the list. 
# If the number is not in the list print the message: "Sorry, your number is not here!"
