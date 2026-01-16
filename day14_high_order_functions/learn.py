from functools import reduce
from operator import add

# def f(lst):
#     return sum(lst)
#
#
# # function as a parameter
# def higher_order_fn(f, lst):
#     return f(lst)
#
#
# lst = [1, 2, 3]
# print(higher_order_fn(f, lst))
#
#
# def square(x):
#     return x**2
#
#
# def cube(x):
#     return x**3
#
#
# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -(x)
#
#
# def higher_order_function(type: str):
#     if type == "square":
#         return square
#     elif type == "cube":
#         return cube
#     elif type == "absolute":
#         return absolute
#     else:
#         raise ValueError("unknown function type")


# result = higher_order_function("square")

# if result is not None:
# print(result(3))

# result = higher_order_function("absolute")
# if result is not None:
# print(result(-3))

#
# def greeting():
#     return "Welcome to python"
#
#
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# g = uppercase_decorator(greeting)
#
# if g is not None:
#     print(g())
#


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# def split_string_decorator(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string
#
#     return wrapper
#
#
# @split_string_decorator
# @uppercase_decorator
# def greeting():
#     return "Welcome to Python"
#
#
# print(greeting())
#
#
# # Decorator that accepts parameters
# def decorator_with_parameters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#
#     return wrapper_accepting_parameters
#
#
# @decorator_with_parameters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love to teach.".format(first_name, last_name))
#
#
# print_full_name("Rodolfo", "Franca", "Brasil")
#

numbers = [1, 2, 3, 4, 5]


# def square(x):
#     return x**2
#
#
# numbers_squared = map(square, numbers)
# print(list(numbers_squared))

numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

names = ["nina", "rodrigo", "rafael", "geremias"]


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# LAMBDA

names_upper_cased = map(lambda x: x.upper(), names)
print(list(names_upper_cased))

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

numbers = [1, 2, 3, 4, 5]

numbers_str = ["1", "2", "3", "4", "5"]


def add_two_numbers(x, y):
    return int(x) + int(y)


total = reduce(lambda x, y: int(x) + int(y), map(int, numbers_str))
print(total)
