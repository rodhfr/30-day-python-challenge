import re


def return_match(substring, string):
    match = re.search(str(substring), string, re.I)
    if match is not None:
        span = match.span()
        print(span)
        start, end = span
        substring = txt[start:end]
        return substring
    else:
        print("Not found")
        return 1


def return_search(substring, string):
    match = re.search(str(substring), string, re.I)
    print(match)
    if match is not None:
        span = match.span()
        print(span)
        start, end = span
        print(start, end)
        substring = txt[start:end]
        return substring


txt = "I love to learn python"
substring = "I love"

print(return_match(substring, txt))

txt = "python is the best language to learn first."
substring = "learn"

print(return_match(substring, txt))

txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# It return a list
matches = re.findall("language", txt, re.I)
print(matches)  # ['language', 'language']

# re.sub is to substitte

# re.split is to split the string conform the substring
print(re.split("\n", txt))
