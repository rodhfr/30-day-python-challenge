import operator
from itertools import islice
from resources.countries import countries
import json

for i in range(11):
    print(i)

for i in range(10, -1, -1):
    print(i)

a = "#"
for i in range(7):
    print(a)
    a = a + "#"

a = "#"
for i in range(8):
    for j in range(8):
        print(a, end=" ")
    print()

rows = 8
cols = 8

for i in range(rows):
    for j in range(cols):
        print("#", end=" ")
    print()

for i in range(10):
    r = i * i
    print(f"{i} * {i} = {r}")

lst = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for item in lst:
    print(item)

for i in range(101):
    if i % 2 != 0:
        print(i, "is odd")
    else:
        print(i, "is even")

w = 0
evens = 0
odds = 0
for i in range(101):
    w = i + w
    if i % 2 != 0:
        odds += i
    else:
        evens += i

print(f"The sum of all numbers is {w}.")
print(f"The sum of all evens is {evens}. And the sum of all odds is {odds}.")


# LEVEL 3
for countrie in countries:
    if "land" in countrie.lower():
        print(countrie)

frt_lst = ["banana", "orange", "mango", "lemon"]
for i in range(3, -1, -1):
    print(frt_lst[i])

with open("resources/countries_data.json", "r", encoding="utf-8") as f:
    countries_data = json.load(f)

print(type(countries_data))
print(countries_data[0]["languages"])

lang_set = set()
lang_lst = []
for item in range(len(countries_data)):
    lang_set.update(countries_data[item]["languages"])
    lang_lst.append(countries_data[item]["languages"])

lst = [item for sublist in lang_lst for item in sublist]

lang_dupes = {}
for lang in lst:
    if lang in lang_dupes:
        lang_dupes[lang] += 1
    else:
        lang_dupes[lang] = 1

# to sort dictionary by value
# print(dict(sorted(lang_dupes.items(), key=lambda x: x[1], reverse=True)))
# or this one to sort dictionary by value
ten_most_speaked_langs = dict(
    sorted(lang_dupes.items(), key=operator.itemgetter(1), reverse=True)
)

k = 10
top_ten = dict(islice(ten_most_speaked_langs.items(), k))
print(top_ten)


most_populated = {}
for item in countries_data:
    item_dct = {item.get("name"): item.get("population")}
    most_populated.update(item_dct)

print(sorted(most_populated.items(), key=operator.itemgetter(1), reverse=True))
