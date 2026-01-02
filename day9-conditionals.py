## LEVEL 1
"""
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
"""

# age = input("Enter your age: ")
# if int(age) >= 18:
#    print("You are old enough to drive.")
# else:
#    r = 18 - int(age)
#    print(f"Wait {r} year(s) to drive.")

"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to 
print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom 
text if my_age = your_age.
"""

# your_age = int(input("Enter your age: "))
# my_age = 28
#
# if your_age > my_age:
#    print(f"You are {your_age - my_age} year(s) older than me.")
# elif your_age < my_age:
#    print(f"You are {my_age - your_age} year(s) newer than me")
# else:
#    print("You have the same age as me.")


""" 
Get two numbers from the user using input prompt. If a is greater than b return a 
is greater than b, if a is less b return a is smaller than b, else a is equal to b.
"""

# n1 = input("Write me a number: ")
# n2 = input("Ok. \nNow other number: ")
# if n1 > n2:
#     print(n1, "is greater than", n2)
# elif n1 < n2:
#     print(n2, "is greater than", n1)
# else:
#     print(n1, "is equal to", n2)


## LEVEL 2
"""
Write a code which gives grade to students according to theirs scores
"""

# score = [10, 55, 65, 75, 85]
# for s in score:
#     if s >= 80 and s <= 100:
#         s = "A"
#     elif s >= 70 and s <= 89:
#         s = "B"
#     elif s >= 60 and s <= 69:
#         s = "C"
#     elif s >= 50 and s <= 59:
#         s = "D"
#     else:
#         s = "F"
#     print(s)

"""
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, 
October or November, the season is Autumn. December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer
"""

# seasons = {
#     "autumn": ["September", "October", "November"],
#     "winter": ["December", "January", "February"],
#     "spring": ["March", "April", "May"],
#     "summer": ["June", "July", "August"],
# }
# usr_ssn = input("Which month are you on: ")
# for season, months in seasons.items():
#     for mes in months:
#         if usr_ssn.lower() == mes.lower():
#             print(season)


# fruits = ["banana", "orange", "mango", "lemon"]
"""
If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
If the fruit exists print('That fruit already exist in the list')
"""
# usr_fruit = str(input("Write a fruit: "))
# if usr_fruit not in fruits:
#     fruits.append(usr_fruit)
#     print("\nFruit Added to list:")
# else:
#     print(f"{usr_fruit} is already present.")
# print(fruits)

## LEVEL 3
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

"""
Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
"""

#
# def middle_list(inpt_lst):
#     mid = len(inpt_lst)
#     print(mid)
#     if mid % 2 == 1:
#         mid = mid // 2
#         print(inpt_lst[mid])
#         return [inpt_lst[mid]]
#     else:
#         mid1 = mid // 2 - 1
#         mid2 = mid // 2
#         print([inpt_lst[mid1], inpt_lst[mid2]])
#         return [inpt_lst[mid1], inpt_lst[mid2]]
#
#
# prs_s = person.get("skills")
# if prs_s:
#     mid_prs_s = middle_list(prs_s)
#
"""
Check if the person dictionary has skills key, if so check if the person has 'Python' 
skill and print out the result.
"""
#
# if prs_s:
#     if "Python" in prs_s:
#         print(prs_s)
#         print(True)

"""
* If a person skills has only JavaScript and React, print('He is a front end developer'), 
if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person 
skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
- for more accurate results more conditions can be nested!

"""

# prs_s = person.get("skills")
# if prs_s:
#     if "JavaScript" in prs_s and "React" in prs_s:
#         print("He is frontend dev")
#     elif "Node" in prs_s and "Python" in prs_s and "MongoDB" in prs_s:
#         print("He is Backend dev")
#     elif "React" in prs_s and "Node" in prs_s and "MongoDB" in prs_s:
#         print("He is fullstack dev")
#     else:
#         print("unknown title")
#
# skills = set(person.get("skills", []))
# if {"JavaScript", "React"} <= skills:
#     print("He is frontend dev")
# elif {"Node", "Python", "MongoDB"} <= skills:
#     print("He is Backend dev")
# elif {"React", "Node", "MongoDB"} <= skills:
#     print("He is fullstack dev")
# else:
#     print("unknown title")

skills = set(person.get("skills", []))
roles = {
    "He is fullstack dev": {"React", "Node", "MongoDB"},
    "He is frontend dev": {"JavaScript", "React"},
    "He is Backend dev": {"Node", "Python", "MongoDB"},
}
for title, required_skills in roles.items():
    if required_skills <= skills:
        print(title)
        break
else:
    print("unknown title")


"""

* If the person is married and if he lives in Finland, print the information in the 
following format:

"""
marital_sts = person.get("is_marred")
country_lived = person.get("country")

if marital_sts:
    if country_lived == "Finland":
        print("Asabeneh Yetayeh lives in Finland. He is married.")
