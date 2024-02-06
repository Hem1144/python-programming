#! first method
# def square(num):
#     return num * num


# print(square(2))

#! second method using lambda
# square = lambda num: num * num
# print(square(3))

#! using lambda
# addTwo = lambda num: num + 2

# print(addTwo(12))

# sum = lambda a, b: a + b
# print(sum(4, 2))


# def funcBuilder(x):
#     return lambda num: num + x  # * it takes 7 as num paramater and 10 as x parameter


# addTen = funcBuilder(10)
# addTwenty = funcBuilder(20)

# print(addTen(7))
# print(addTwenty(7))

#! Higher order function map()
# to_square = lambda num: num * num

# numbers = [3, 7, 12, 18, 20, 34]

# square_nums = map(to_square, numbers)
# print(list(square_nums))

#! using filter built-in-function to check odd numbers
# demo = lambda num: num % 2 != 0
# numbers = [3, 7, 12, 18, 20, 34]
# odd_nums = filter(demo, numbers)
# print(list(odd_nums))

#! reduce function
from functools import reduce

# for_reduce = lambda accum, curr: accum + curr
# numbers = [1, 2, 3, 4, 5, 1]
# total = reduce(for_reduce, numbers, 10)
# print(sum(numbers, 10))

#! character count using reduce function

names = ["Hemlal", "Akash", "Suneel", "Sushil", "Prabesh"]
char_count = lambda accum, elem: accum + len(elem)
total_chars = reduce(char_count, names, 0)
print("Total characters in the names are : ", total_chars)
