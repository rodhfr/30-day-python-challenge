from typing import Sequence
import uuid
import random


def random_user_id():
    uid = str(uuid.uuid4())
    uid = uid[:6]
    return uid


# print(random_user_id())


def user_id_gen_by_user():
    chars_n = int(input("Number of characters: "))
    ids_n = int(input("Number of ids: "))
    uid_lst = []

    for _ in range(ids_n):
        uid_lst.append(str(uuid.uuid4()))

    k_numbered_lst = []
    for item in uid_lst:
        k_numbered_lst.append(item[:chars_n])

    return k_numbered_lst


# print(user_id_gen_by_user())


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


# print(rgb_color_gen())


def list_of_hexa_color():
    # c = f"#{random.randint(0, 0xFFFFFF):06x}"
    c = f"#{random.randbytes(3).hex()}"
    return [c]


# print(list_of_hexa_color())


def generate_colors(color_code="rgb", color_lenght=1):
    color_lst = []
    if color_code == "hexa":
        color_fn = list_of_hexa_color
    else:
        color_fn = rgb_color_gen
    for _ in range(int(color_lenght)):
        color_lst.append(color_fn())
    return color_lst


# print(generate_colors(color_code="rgb", color_lenght=8))
# print(generate_colors(color_code="hexa", color_lenght=4))


def shuffle_list(lst):
    # this is interesting python when copy list it
    # this just reference the list it does not copy unless
    # explicitly use the constructor list()
    # or copy the split original[:]
    seq = list(lst)
    out = []

    for _ in lst:
        sel = random.choice(seq)
        out.append(sel)
        seq.remove(sel)

    return out


lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# print(shuffle_list(lst))


def unique_seven_rand():
    seq = []
    last_r_num = -1
    for i in range(7):
        # print("for n:", i)
        r_num = random.randint(0, 9)
        # print("r_num: ", r_num)
        # print("last_r_num ", last_r_num)
        while True:
            if r_num != last_r_num:
                # print("break")
                break
            r_num = random.randint(0, 9)
            # print("while loop")
        seq.append(r_num)
        last_r_num = r_num
    return seq


print(unique_seven_rand())
