numbers = [(i, i * i) for i in range(11)]
# print(numbers)

positive_even_nums = [x for x in range(21) if x % 2 == 0 and x > 0]
# print(positive_even_nums)

## Make more easy to flatten lists
lst_of_lsts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_lst = list()
for item in lst_of_lsts:
    for item in item:
        flat_lst.append(item)
# print(flat_lst)

lst_of_lsts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_lst = [x for x in lst_of_lsts for x in x]
# print(lst_of_lsts)
# print(flat_lst)

## Lambda function can take any number of arguments, but can only have one expr
## ession. Need when want to write anonymous function inside another function
add_two_nums = lambda a, b: a + b  # noqa: E731
# print(add_two_nums(2, 3))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
f_nums = [x for x in numbers if x > 0]
# print(f_nums)

lst_of_lsts = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_lst = [x for x in lst_of_lsts for x in x for x in x]
# print(flatten_lst)

a = [i for i in range(11)]

lst_comprehn = [(x, 1, x**2, x**3, x**4, x**5) for x in range(11)]

strl = ""
for x in lst_comprehn:
    strl += str(x) + "\n"
strl = "[" + strl
strl = strl[:-1] + "]"
# print(strl)

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

flatten_countries_lst = [{"country": x} for x in countries for x in x for x in x]

# for x in flatten_countries_lst:
# print(x)

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]

names_flatten = [x for x in names for x in x for x in x]
names_comb_lst = [
    names_flatten[i] + " " + names_flatten[i + 1] for i in range(len(names_flatten) - 1)
]
print(names_comb_lst)
# for x in names_flatten:
#     print(x)

m = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)  # noqa
print(m(11, 3, 5, 2))
