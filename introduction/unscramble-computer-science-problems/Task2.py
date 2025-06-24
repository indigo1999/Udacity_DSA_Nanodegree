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
    phone_dict = {}

    for call in calls :
        phone_dict[call[0]] = dict_get_by_key(phone_dict,call[0],0) + string_to_integer_seconds(call[3])
        phone_dict[call[1]] = dict_get_by_key(phone_dict,call[1],0) + string_to_integer_seconds(call[3])
    
    
    max_time_spent = 0
    max_time_phone_number = ""

    for phone in phone_dict :
        if phone_dict[phone] > max_time_spent :
            max_time_spent = phone_dict[phone]
            max_time_phone_number = phone
    

    print(f"{max_time_phone_number} spent the longest time, {max_time_spent} seconds, on the phone during September 2016.")

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


def dict_get_by_key (dict_,key , default_value) :

    if key in dict_ :
        return dict_[key]
    else :
        return default_value 


solution(calls=calls)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

