import re


paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love"

dict_frequency = dict()
for word in paragraph.split():
    matches = re.findall(word, paragraph, re.I)
    dict_frequency[word] = len(matches)


sorted_dict = sorted(dict_frequency.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)

print("\n")

# with regex
words = re.findall(r"\b\w+\b", paragraph.lower())
print(words)

print("\n")

txt = """
 points = ['-12', '-4', '-3', '-1', '0', '4', '8']
 sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
 distance = 8 -(-12)
"""

txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

match = re.findall(r"-?\d+", txt, re.I)
print(match)


def is_valid_variable(name):
    pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
    return bool(re.match(pattern, name))


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))  # True


def most_frequent_words(cleaned_text):
    words = re.findall(r"\w+", cleaned_text.lower())

    freq_list = [(word, words.count(word)) for word in set(words)]
    sorted_list = sorted(freq_list, key=lambda x: x[1], reverse=True)
    return sorted_list


def clean_text(sentence):
    excluded_chars = r"[%@&$;#]"
    match = re.sub(excluded_chars, "", sentence)
    return match


sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
cleaned_text = clean_text(sentence)

print("\n")
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text))  # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
