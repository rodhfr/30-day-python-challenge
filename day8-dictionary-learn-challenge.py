# print("\nCreate an empty dictionary called dog: ")
# dog = {"pastor", "shitzu", "lhasa", "pintscher"}

person = {
    "first_name": "liandra",
    "last_name": "lima",
    "age": "28",
    "country": "br",
    "marital_status": "married",
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "francisco da rocha", "zipcode": "58036448"},
}

print(len(person))

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(dct["key2"])
print(dct["key4"])

print(
    "\nGet method avoid raising error if key does not exist. get method returns None NoneType object data type if key not exist: "
)
print(person.get("city"))

print("\nAdd new items to dictionary: ")
dct["key5"] = "value5"
print(dct)

print("\nModifyiong items in dict: ")
dct["key1"] = "value-one"
print(dct)

print("\nCheck keys in dict: ")
print("key2" in dct)
print("key7" in dct)

print("\nRemoving key and value pairs from dict: ")
# pop(key) removes item with the key
# popitem() removes the last item
# del removes an item with specified key name

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct.pop("key1")
print(dct)
dct.popitem()
print(dct)
del dct["key2"]
print(dct)

print("\nChanging dict to list of items: ")
print()

print(dct.items())
print(dct.clear())
del dct
dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
dct_copy = dct.copy()
print(dct)
keys = dct.keys()
print(keys)

print("\nCreate an empty dictionary called dog")
dog = {}

print("\nAdd name, color, breed, legs, age to the dog dictionary")
dog["name"] = "rufus"
dog["color"] = "black"
dog["breed"] = "pastor"
dog.update({"legs": "long"})
extra = {"age": "6"}
dog.update(extra)
print(dog)

print(
    "\nCreate a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys"
)
student = {"first_name": "Rodrigo"}
a1 = {"last_name": "Silva"}
a2 = {"gender": "M"}
a3 = {"age": "28"}
a4 = {"marital_status": "married"}
add_student = [a1, a2, a3, a4]
for i in add_student:
    student.update(i)
student["skills"] = ["JavaScript", "Python", "PowerBI"]
student["country"] = "Recife"
student["address"] = "R. eduardo vieira da silva"
print(student)

print("\nGet the length of the student dictionary")
s_len = len(student)
print(s_len)

print("\nGet the value of skills and check the data type, it should be a list")
skill_lst = student.get("skills")
print(skill_lst)
print(type(skill_lst))

print("\nModify the skills values by adding one or two skills")
student["skills"].append("React")
print(student)

print("\nGet the dictionary keys as a list")
print(list(student.items()))

print("\nGet the dictionary values as a list")
print(list(student.values()))

print("\nChange the dictionary to a list of tuples using items() method")
print(student.items())

print("\nDelete one of the items in the dictionary")
print(student)
student.pop("last_name")
print(student)

print("\nDelete one of the dictionaries")
del student
print("")
