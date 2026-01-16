from functools import reduce
import json

# -*- coding: utf-8 -*-

names = ["Asabneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""day14_higher_order_functions.ipynb

Collab Version:
    https://colab.research.google.com/drive/1NtPIkshcBrwgqCP4Cp2CIdlxoWJBTqgT

# Python Higher Order Functions
"""


"""## **Q1L1) Explain the difference between map, filter, and reduce:**

- map takes a function and applies to every element of an iterable object
"""

regular_list = [1, 2, 3, 4, 5]
sum_one = map(lambda x: x + 1, regular_list)
print(list(sum_one))

"""- filter takes a function and uses boolean condition to filter out elements from
iterable object.
"""

lst = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(even_numbers)

"""- reduce exists to reduce an entire collection to a single value aplying repeatdly the function it accepts.

"""

lst = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, lst)
print(product)

"""---

## **Q2L2) Explain the difference between higher order function, closure and decorator:**

### higher order function is when:

- a function takes another function as an argument
- a functions returns a function as a result
"""


def uppercase(text):
    return text.upper()


def greet(some_fn):
    return some_fn("Hello")


print(greet(uppercase))

"""### A closure function is when:
- A closure is function that has a inner function which you return
- A closure's inner function uses variables from the external fn
"""


def multiplyer_creator(n):
    def multiply(x):
        return x * n

    return multiply


double = multiplyer_creator(2)
triple = multiplyer_creator(3)

print(double(10))
print(triple(10))

"""closure function is useful whenever is needed to maintain state between functions without needing a class"""


def countate():
    total = 0

    def increment():
        nonlocal total
        total += 1
        return total

    return increment


c = countate()
print(c())  # 1
print(c())  # 2
print(c())  # 3

"""### A decorator is a function that:

1. Receives another function that is below @decorator
2. Creates a new function that wrappes the older function inside
3. Returns this new behavior enhanced function
"""


def changecase(func):
    def wrapper():
        return func().upper()

    return wrapper


@changecase
def greet():
    return "hello"


print(greet())

"""---

## **Q3L3) Define a call function before map, filter or reduce, see examples:**
"""


def ite_manipulation(type_op):
    if type_op == "map":

        def map_fn(fn, iterable):
            return list(map(fn, iterable))

        return map_fn
    elif type_op == "filter":

        def filter_fn(fn, iterable):
            return list(filter(fn, iterable))

        return filter_fn
    elif type_op == "reduce":

        def reduce_fn(fn, iterable):
            return reduce(fn, iterable)

        return reduce


# def ite_manipulation(type_op):
#    ops = {
#        "map": lambda fn, iterable: list(map(fn, iterable)),
#        "filter": lambda fn, iterable: list(filter(fn, iterable)),
#        "reduce": lambda fn, iterable: reduce(fn, iterable)
#    }
#    return ops[type_op]

lst = [1, 2, 3, 4, 5]
map_fn = ite_manipulation("map")
print(map_fn(lambda x: x * 2, lst))

filter_fn = ite_manipulation("filter")
print(filter_fn(lambda x: x % 2 == 0, lst))

reduce_fn = ite_manipulation("reduce")
print(reduce_fn(lambda x, y: x + y, lst))

"""## **Q4L1) Use for loop to print each country in the countries list.**
## **Q5L1)Use for to print each name in the names list.**
## **Q6L1) Use for to print each number in the numbers list.**



"""

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in countries:
    print(x)
for x in names:
    print(x)
for x in numbers:
    print(x)

"""## **Q1L2)Use map to create a new list by changing each country to uppercase in the countries list**

"""

upper_countries = list(map(lambda x: x.upper(), countries))
print(upper_countries)

"""## **Q2L2)Use map to create a new list by changing each number to its square in the numbers list**"""

squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)

"""## **Q3L2)Use map to change each name to uppercase in the names list** *italicized text*"""

upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)

"""## **Q4L2)Use filter to filter out countries containing 'land'.**"""

countries_without_land = list(filter(lambda x: "land" not in x, countries))
print(countries_without_land)

"""### **Q5L2)Use filter to filter out countries having exactly six characters.**"""

filter_out_six_chars_countries = list(filter(lambda x: len(x) != 6, countries))
print(filter_out_six_chars_countries)

"""## **Q6L2)Use filter to filter out countries containing six letters and more in the country list.**"""

filter_out_six_or_more_chars_countries = list(filter(lambda x: len(x) < 6, countries))
print(filter_out_six_or_more_chars_countries)

"""## **Q7L2)Use filter to filter out countries starting with an 'E'**"""

filter_out_starting_with_e_countries = list(filter(lambda x: x[0] != "E", countries))
print(filter_out_starting_with_e_countries)

"""## **Q8L2)Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))**"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_reduce_mapped = int(
    reduce(lambda x, y: x + y, map(lambda x: x * 2, filter(lambda x: x != 1, numbers)))
)
print(filtered_reduce_mapped)

"""## **Q9L2)Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.**"""


def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))


countries_str = get_string_lists(countries)
print(countries_str)

"""## **Q10L2)Use reduce to sum all the numbers in the numbers list.**"""

reduced_numbers = reduce(lambda x, y: x + y, numbers)
print(reduced_numbers)

"""## **Q11L2)Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries**"""

reduced_countries = reduce(lambda x, y: x + " " + y, countries)
print(reduced_countries, "are north European countries")

"""## **Q12L2)Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).**"""

countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

filtering_arr = ["land", "ia", "island", "stan"]
for filterr in filtering_arr:
    countries_with_filterr = list(filter(lambda x: filterr in x, countries))
    print(f'\ncountries with "{filterr.upper()}": {countries_with_filterr}')

"""## **Q13L2)Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.**"""

# With list and set comprehension
lst_index = [x[0] for x in countries]
index_dct = {x: lst_index.count(x) for x in lst_index}


def returns_index_dict(lst):
    lst_index = list(map(lambda x: x[0], lst))
    index_dct = dict(sorted(map(lambda x: (x, lst_index.count(x)), set(lst_index))))
    return index_dct


print(returns_index_dict(countries))

"""## **Q14L2)Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.**"""


def get_first_ten_countries(lst):
    return lst[:10]


print(get_first_ten_countries(countries))

"""## **Q15L2)Declare a get_last_ten_countries function that returns the last ten countries in the countries list.**"""


def get_last_ten(lst):
    return lst[-10:]


print(get_last_ten(countries))


with open("countries_data.json", "r") as f:
    data = json.load(f)

countries_dict = {x["name"]: x for x in data}

name_data_sorted = sorted(data, key=lambda country: country["name"], reverse=True)
countrie_namai = [x.get("name") for x in name_data_sorted]
print(countrie_namai)

capital_data_sorted = sorted(data, key=lambda country: country["capital"])

countrie_capital = [
    x.get("capital") for x in capital_data_sorted if x.get("capital") is not None
]
print(countrie_capital)


with open("countries_data.json", "r") as f:
    d = json.load(f)

print("\nQ3l3 Counties population sorted by size\n")
big_dict = {}
for x in d:
    # print(x, "\n")
    current_dict = {x["name"]: x["population"]}
    # print(current_dict)
    big_dict.update(current_dict)

print(sorted(big_dict.items(), key=lambda x: x[1], reverse=True))
