# Learn segment

st = set()

st = {"item1", "item2"}

print("\nadd:")
st.add("item3")
print(st)

print("\nupdate:")
st.update(["item4", "item5", "item6"])
print(st)

print("\nremove:")
st.remove("item2")
print(st)

removed_item = st.pop()
print(st)
print(removed_item)

print("\nclear:")
st.clear()
print(st)

print("\nunion:")
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item5", "item6", "item7", "item8"}
st3 = st1.union(st2)
print(st3)

print("\nupdate:")
st4 = set()
set4 = st4.update(st3)
print(st4)

print("\nintersection:")
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item3", "item2"}
st1.intersection(st2)
print(st1)

print("\nsubset and superset:")
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
print(st1.issubset(st2))
print(st1.issuperset(st2))

print("\ndifference:")
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
# elementos que estao tanto em st1 quanto em st2 mas nao em ambos
print(st2.difference(st1))
print(st1.difference(st2))

print("\nsymmetric difference:")
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
# elementos que estao em apenas um dos conjuntos
# (st1 - st2) U (st2 - st1)
print(st2.symmetric_difference(st1))

print("\ndisjoint sets: ")
st1 = {"item1", "item2", "item3", "item4"}
st2 = {"item2", "item3"}
print(st1)
print(st2)
# isso e para ver se tem disjuncao se tem algum item que nao esta presente
# retorna um valor booleano
print(st2.isdisjoint(st1))
