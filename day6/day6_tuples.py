print("\nCreate an empty tuple:")
tpl = (1, 2, 3)
print(tpl)

print("\nCreate a tuple containing names of your sisters and your brothers (imaginary siblings are fine)")
sisters = ("isabela", "naninha", "fulana", "ciclana")
brothers = ("fabricio", "fulano", "xerox", "xerolano")
print(sisters)
print(brothers)

print("\nJoin brothers and sisters tuples and assign it to siblings:")
siblings = (sisters + brothers)
print(siblings)

print("\nHow many siblings do you have?:")
sib_len = len(siblings)
print(sib_len)

print("\nModify the siblings tuple and add the name of your father and mother and assign it to family_members:")
parents = ("claudiana", "ivano")
family_members = (parents + siblings)
print(family_members)

print("\nUnpack siblings and parents from family_members:")
mother, father, *siblings = family_members
print(mother)
print(father)
print(siblings)

print("\nCreate fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.:")
fruits = ("amora", "pessego", "tomate", "physalis")
veggies = ("potato", "coentro", "alface")
animal = ("dog", "cat", "cow", "duck")
food_stuff_tp = (fruits + veggies + animal)
print(food_stuff_tp)

print("\nChange the about food_stuff_tp tuple to a food_stuff_lt list:")
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print("\nSlice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.:")
mid_item = len(food_stuff_lt)/2
#print(mid_item)
if mid_item % 1 != 0:
    sliced_middle = (food_stuff_lt[int(mid_item)-1], food_stuff_lt[int(mid_item)])
else:
    sliced_middle = (food_stuff_lt[int(mid_item)-1])
print(sliced_middle)

print("\nSlice out the first three items and the last three items from food_staff_lt list: ")
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

print("\nDelete the food_staff_tp tuple completely: ")
del food_stuff_tp
try:
    my_tuple
except NameError:
    print("Tuple is not defined")
else:
    print("Tuple exists")

print("\nCheck if an item exists in tuple: ")
def isInTP(str_inpt, tpinpt): 
    if str_inpt in tpinpt:
        print(str_inpt, "is preset in tuple.")
    else:
        print(str_inpt, "is not present in tuple.")

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
isInTP("Estonia", nordic_countries)
isInTP("Iceland", nordic_countries)










