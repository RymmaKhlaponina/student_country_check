import re
""" The program receives as input a pair consisting of a key (student number) and values (e.g. Name, age, country).
The dictionary is formed, then the dictionary is passed to the function to check the country of origin, in case the 
country - Ukraine, the student's data (except for the key) are added to the list student_ukr"""

def input_dict():
    """ The function is required to enter the dictionary (keys + values) from the console"""
    students = dict()
    while (True):
        print('Enter key (empty enter - exit) ')
        key = input()
        if key == '':
            break
        print('Enter value ')
        value = input().split()
        students[key] = value
    return students


def check_country(student_s):
    """ The function is necessary to check the student's country. The check is performed as follows: the key-value pairs
    are enumerated by the key in the student_s library, then, since the values are a !list! (since the values are more
    than one) the re.fullmatch function is used to check if the third element in the list matches the pattern.
    (Assuming that the first value is a name, the second value is anything else and only the third value is a country
    and all the values are entered according to this rule)
    If the country matches, the WHOLE list (i.e. the value that refers to the current key) is added to the LIST.
    students_ukr"""
    students_ukr = []
    for key in student_s:
        if re.fullmatch(r'[u,U]\w\w', student_s[key][2]) is not None:
            students_ukr.append(student_s[key])
    print ('Students from Ukraine ' + str(students_ukr) + '\n')


students = input_dict()
print(students)
check_country(students)
