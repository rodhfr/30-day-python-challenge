empty_list = []
more5 = [1,2,3,4,5,6,7]
print("List: ", more5)
print("\nlist len:")
list_size = len(more5)
print(list_size)
middle_list = int(list_size/2)
print("\nfirst middle last:")
print(f"{more5[0]}\n{more5[middle_list]}\n{more5[-1]}")

print("\nlistas com strings")
mixed_data_types = ["rodolfo", 28, "married", "francisco feitosa palitot"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("\nHow many companies:")
print(len(it_companies))
it_companies.append("Softcom")
print("\nadd company:")
print(it_companies)
print("\ninsert company in the middle:")
it_companies.insert(int(len(it_companies)/2), "Petrobras")
print(it_companies)
print("\nit_companies[0] to upper:")
it_companies[0] = it_companies[0].upper()
print(it_companies)

print("\nJoin it_companies with #:")
print("#".join(it_companies))

print("\nCheck if certain company exists within it_companies:")
if "Softcom" in it_companies:
    print("Softcom exists")

print("\nSoft the list using sort():")
it_companies.sort()
print(it_companies)

print("\nreverse the list in descending order using reverse():")
it_companies.reverse()
print(it_companies)

print("\nSlice out the first 3 companies from the list:")
it_companies = it_companies[3:]
print(it_companies)

print("\nSlice out the last 3 companies from the list:")
it_companies = it_companies[:-3]
print(it_companies)

print("\nSlice out the middle IT company or companies from the list:")
mid = int(len(it_companies)/2)
print(it_companies[mid])

print("\n remove the first it company from the list:")
del it_companies[0]
print(it_companies)

print("\nfullstack:")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

print("\nAfter joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.:")
add = ["Python, SQL"]
full_stack[5:5] = add
print(full_stack)

print("\nSort the list and find the min and max age:")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("max_age", max_age)
print("min_age", min_age)

print("\nAdd the min age and the max age again to the list:")
ages.insert(0, min_age)
ages.insert(-1, max_age)
print(ages)

print("\nFind the median age (one middle item or two middle items divided by two):")

len_ages = len(ages)/2 
if len_ages is float:
    median = ((ages[int(len_ages)] + ages[int(len_ages)+1]) / 2)
else:
    median = ages[int(len_ages)]
print(median)

print("\nFind the average age (sum of all items divided by their number ):")
avg = 0 
for i in ages:
    avg += i
avg = avg / len(ages)
print(avg)

print("\nFind the range of the ages (max minus min):")
minvalue = min(ages)
maxvalue = max(ages)
print(maxvalue - minvalue)

print("\nCompare the value of (min - average) and (max - average), use abs() method:")
print(abs(minvalue - avg))
print(abs(maxvalue - avg))

print("\nFind the middle country(ies) in the countries list:")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'joao',
  'Zambia',
  'Zimbabwe',
];

def isListEven(list_input):
    len_list = len(list_input)
    middle_list = len_list / 2
    is_list_float = middle_list % 1 != 0 
    if is_list_float:
        return False, len_list, middle_list
    else:
        return True, len_list, middle_list

is_even, len_list, middle_list = isListEven(countries)
if is_even:
    #print("list is even number")
    #print(middle_list)
    middle_country = [countries[int(middle_list)], countries[int(middle_list)+1]]
else:
    #print("List is odd number")
    #print(middle_list)
    middle_country = countries[int(middle_list)]
print(middle_country)

print("\nDivide the countries list into two equal lists if it is even if not one more country for the first half.:")
is_even, len_list, middle_list = isListEven(countries)
print("Is even:", is_even)
print("Len List:", len_list)
print("Middle index:", middle_list)
if is_even:
    first_half = countries[:int(middle_list)]
    second_half = countries[int(middle_list):]
else:
    first_half = countries[:int(middle_list)+1]
    second_half = countries[int(middle_list):]
print("\nfirst half:", first_half, "")
print("\nsecond half:", second_half, "")

    
print("\nUnpack the first three countries and the rest as scandic countries.:")
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic = countries2
print(first)
print(second)
print(third)
print(scandic)











