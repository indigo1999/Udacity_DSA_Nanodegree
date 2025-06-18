"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def solution(calls) :
    answer = 0
    telephone_number = 0
    for call in calls :
        compare_to_answer = string_to_integer_seconds(call[3])
        if answer < compare_to_answer :
            answer = compare_to_answer
            telephone_number = call[0]

    print(telephone_number," spent the longest time,",answer," seconds, on the phone during September 2016.")


# string_to_integer function 
def string_to_integer_seconds(s):

    string_to_number_dict = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9
    }

    integers_list = []

    for _s_ in s : 
        for string_key in string_to_number_dict: 
            if _s_ == string_key:
                integers_list += [string_to_number_dict[string_key]]

    answer = 0
    index = 0
    for number in integers_list: # n
        answer += number * 10 ** ((list_len(integers_list) - 1) - index)
        index += 1

    return answer


def list_len(lists) :
    count = 0
    for list_count in lists :
        count += 1
    
    return count

solution(calls=calls)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

