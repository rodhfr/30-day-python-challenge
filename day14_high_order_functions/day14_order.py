import json


with open("countries_data.json", "r") as f:
    d = json.load(f)

big_dict = {}
for x in d:
    # print(x, "\n")
    current_dict = {x["name"]: x["population"]}
    # print(current_dict)
    big_dict.update(current_dict)

# big_dict_sorted = dict(sorted(big_dict.items(), key=lambda x: x[1]))
print(sorted(big_dict.items(), key=lambda x: x[1], reverse=True))
