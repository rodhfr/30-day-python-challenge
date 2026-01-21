# def sum_of_five_nums(a,b,c,d,e):
#     return a+b+c+d+e
#
# lst = [1,2,3,4,5]
# print(sum_of_five_nums(*lst))

import enum


# for index, item in enumerate([20, 30, 40]):
#     print(index, item)

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]


# enumerate
for index, x in enumerate(countries):
    if x == "Finland":
        print(f"The country {x} has been found at index {index}")


# zip
# associate items by index
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato", "tomato"]
fruits_and_vegs = []
for (
    f,
    v,
) in zip(fruits, vegetables):
    fruits_and_vegs.append({"fruit": f, "veg": v})

print(fruits_and_vegs)
