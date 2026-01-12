import json
from os import SPLICE_F_NONBLOCK


def add_two_numbers(a, b):
    return a + b


def area_of_circle(r):
    return 3.14 * r * r


def add_all_nums(*a):
    total = 0
    for num in a:
        if isinstance(num, int):
            total += num
        else:
            print(num, "is not int")
    return total


# print(add_all_nums(1, 2, 3, 4, 5, "rato", 5))


def convert_celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


# print(convert_celsius_to_fahrenheit(30))


def check_season(m):
    winter = [("December", 12), ("January", 1), ("February", 2), ("winter")]
    spring = [("March", 3), ("April", 4), ("May", 5), ("spring")]
    summer = [("June", 6), ("July", 7), ("August", 8), ("summer")]
    autumn = [("September", 9), ("October", 10), ("November", 11), ("autumn")]
    obj_month = 0
    all_seasons = [winter, spring, summer, autumn]
    for season in all_seasons:
        for item in season:
            s_string, s_number, *s_rest = item
            if s_number == m:
                obj_month = s_number
                print(s_string)
                print(obj_month)
                return season[3]
            if isinstance(m, str):
                if s_string.lower() == m.lower():
                    obj_month = s_number
                    print(s_string)
                    print(obj_month)
                    return season[3]


# print(check_season("december"))


def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


# print(calculate_slope(1, 2, 3, 4))


def solve_quadratic_eqn(a, b, c):
    x1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    return x1, x2


# print(solve_quadratic_eqn(1, 5, 6))


def parse_quad_eq(st):
    ls = []
    if isinstance(st, str):
        for i in range(len(st) - 1):
            if list(st)[i + 1] == "x":
                print(st[i])
                if st[i] == "":
                    ls.append("1")
                else:
                    ls.append(st[i])
        print(st[-1])
        ls.append(st[-1])

        a = int(ls[0])
        b = int(ls[1])
        c = int(ls[2])
        return solve_quadratic_eqn(a, b, c)


# print(parse_quad_eq("1x^2+5x+6"))


def print_list(lst):
    for i in range(len(lst)):
        print(lst[i])


lst = [1, 2, 3]
# print(print_list(lst))


def reverse_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i])

    return "end"


lst = [1, 2, 3]
# print(reverse_list(lst))


def capitalize_list_items(lst):
    new_lst = []
    for item in lst:
        item = item[0].upper() + item[1:]
        new_lst.append(item)
    return new_lst


food_stuff = ["potato", "tomato", "mango", "milk"]
# print(capitalize_list_items(food_stuff))


def add_item(lst, add):
    lst.append(add)
    return lst


add = "chicken"
# print(add_item(food_stuff, add))
add_item(food_stuff, add)


def remove_item(lst, rem):
    print(lst)
    lst.remove(rem)
    return lst


rem = "chicken"
# print(remove_item(food_stuff, rem))


def sum_of_numbers(num):
    sum = 0
    for i in range(1, num + 1, 1):
        sum += i
    return sum


# print(sum_of_numbers(5))
# print(sum_of_numbers(10))
# print(sum_of_numbers(100))


def sum_of_even(num):
    sum = 0
    ls = []
    for i in range(1, num + 1, 1):
        if i % 2 == 0:
            sum += i
            ls.append(i)
    return sum, ls


# print(sum_of_even(100))


def sum_of_odd(num):
    sum = 0
    ls = []
    for i in range(1, num + 1, 1):
        if i % 2 != 0:
            sum += i
            ls.append(i)
    return sum, ls


# print(sum_of_odd(100))


def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
        print(i)
    return fact


# print(factorial(5))


def is_empty(p):
    return not p


# print("Is empty?", is_empty(""))


def sum_lst(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum


def median_lst(lst):
    middle_lst = int(len(lst) / 2)
    elements = []
    if len(lst) % 2 == 0:
        elements.extend((lst[middle_lst - 1], lst[middle_lst]))
        median = mean_lst(elements)
    else:
        median = lst[middle_lst]
    return median


def mean_lst(lst):
    return sum_lst(lst) / len(lst)


# Mode implementation without count
# def mode_lst(lst):
#     freq = {}
#     not_lst = []
#     for i in range(len(lst)):
#         if lst[i] in not_lst:
#             pass
#         else:
#             not_lst.append(lst[i])
#
#         if lst[i] in freq:
#             freq[lst[i]] += 1
#         else:
#             freq[lst[i]] = 1
#
#     moda = None
#     maior = 0
#     for chave, valor in freq.items():
#         if valor > maior:
#             maior = valor
#             moda = chave
#
#     return moda


# Mode implementation with count
def mode_lst(lst):
    moda = None
    maior = 0

    for x in lst:
        c = lst.count(x)
        if c > maior:
            maior = c
            moda = x
    return moda


def range_lsts(lst):
    max_v = max(lst)
    min_v = min(lst)
    return [max_v, min_v]


def var_lsts(lst):
    mean = mean_lst(lst)
    deviance = []
    for i in range(len(lst)):
        deviance.append((lst[i] - mean) ** 2)
    variance = mean_lst(deviance)
    return variance


def std_lsts(lst):
    return var_lsts(lst) ** 0.5


def calculate_lsts(lst):
    mean = mean_lst(lst)
    median = median_lst(lst)
    mode = mode_lst(lst)
    range_v = range_lsts(lst)
    variance = var_lsts(lst)
    std_v = std_lsts(lst)

    result = [mean, median, mode, range_v, variance, std_v]
    return result


lst = [8, 6, 6, 4, 7, 8, 8, 6, 6]
# print(calculate_lsts(lst))


def is_prime(n):
    if n % 1 == 0 and n % n == 0:
        print(n, "is a prime number.")
        return True


# print(is_prime(1))


# def is_unique(lst):
#     res = []
#     unique = []
#     for item in lst:
#         if item not in unique:
#             unique.append(item)
#     return unique


def is_unique(lst):
    unique_lst = set(lst)
    return unique_lst == lst


# print(is_unique(lst))


def is_same_data_type(lst):
    for x in range(len(lst) - 1):
        if type(lst[x]) is not type(lst[x + 1]):
            return False
    return True


lst = [1, 1, 1, 4]
# print(is_same_data_type(lst))


def is_variable_valid(v):
    try:
        v
        print("variable is defined")
    except NameError:
        print("Variable not defined")


# print(is_variable_valid(a))


with open("resources/countries_data.json", "r", encoding="utf-8") as f:
    countries_data = json.load(f)


def most_spoked_langs(dic, k=float("inf")):
    spoked_langs = []
    for countri_dic in dic:
        spoked_langs.extend(countri_dic.get("languages"))

    freq = {}
    for x in spoked_langs:
        freq[x] = spoked_langs.count(x)

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_freq)

    top_k_langs = {}
    i = 0
    for key, value in dict(sorted_freq).items():
        if i == k:
            break
        top_k_langs[key] = value
        i += 1

    return top_k_langs


# print(most_spoked_langs(countries_data, 20))


def most_populated_countries(dic, k=float("inf")):
    data = dic
    populated_countries_dct = {}
    for x in data:
        x = dict(x)
        popl = x.get("population")
        namectr = x.get("name")
        populated_countries_dct[namectr] = popl

    sorted_countries_popl = sorted(
        populated_countries_dct.items(), key=lambda x: x[1], reverse=True
    )

    top_k_populated_countries = {}
    i = 0
    for key, value in dict(sorted_countries_popl).items():
        if i == k:
            break
        top_k_populated_countries[key] = value
        i += 1

    return top_k_populated_countries


print(most_populated_countries(countries_data, 10))
