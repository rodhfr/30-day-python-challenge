# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("\nFind the length of the set it_companies: ")
print(len(it_companies))

print("\nAdd 'Twitter' to it_companies: ")
it_companies.add("Twitter")
print(it_companies)

print("\nInsert multiple IT companies at once to the set it_companies: ")
additional_companies = {"Meta", "Alibaba", "AT&T", "Dell", "Sony"}
it_companies.update(additional_companies)
it_companies.union(additional_companies)
print(it_companies)

print("\nRemove one of the companies from the set it_companies: ")
it_companies.remove("Twitter")
print(it_companies)

print("\nWhat is the difference between remove and discard: ")
print('it_companies.discard("SomeLocalCompany")')
print(it_companies)
print('it_companies.remove("SomeLocalCompany")')
print("KeyError")
print("The difference is that remove gaves keyerror if the element is not in the set.")

print("\nJoin A and B: ")
X = A
X.update(B)
print(X)

print("\nFind A intersection B: ")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A:", A)
print("B:", B)
A.intersection(B)
print(A)

print("\nIs A subset of B: ")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A:", A)
print("B:", B)
print(A.issubset(B))

print("\nAre A and B disjoint sets: ")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A:", A)
print("B:", B)
print(A.isdisjoint(B))

print("\nJoin A with B and B with A: ")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A:", A)
print("B:", B)
A.update(B)
B.update(A)
print(A)
print(B)


print("\nWhat is the symmetric difference between A and B: ")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A:", A)
print("B:", B)
print(A.symmetric_difference(B))

print("\nDelete the sets completely: ")
A.clear()
B.clear()
print("A:", A)
print("B:", B)

print(
    "\nConvert the ages to a set and compare the length of the list and the set, which one is bigger?: "
)
age = [22, 19, 24, 25, 26, 24, 25, 24]
stage = set(age)
print("List:", len(age))
print("Set:", len(stage))
print(stage)
print(
    "the difference resides in the fact that sets only perceives unitary values and list not"
)


print(
    "\nExplain the difference between the following data types: string, list, tuple and set: "
)
print(
    "string is just a bunch of characters in a list, list is a datatype that holds in order characters or values and is mutable, tuple is a list that is not mutable, set holds values not in order but with value importance."
)

print(
    "\nI am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.: "
)
strphrase = "I am a teacher and I love to inspire and teach people."
lstphrase = strphrase.split(" ")
setphrase = set(lstphrase)
print(setphrase)
print("Unique words:", len(setphrase))
