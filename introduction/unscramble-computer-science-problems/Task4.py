"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def is_telemarketer_number (input_number) :
    
    if input_number[0:3] == "140" :
        return True

    return False

def solution(calls) :

    possible_telemarketer_number_list = []
    for call in calls :
        if is_telemarketer_number(call[0]) and ((call[0] in possible_telemarketer_number_list) == False)  :
            possible_telemarketer_number_list += [call[0]]

        if is_telemarketer_number(call[1]) and ((call[1] in possible_telemarketer_number_list) == False) :
            possible_telemarketer_number_list += [call[1]]

    possible_telemarketer_number_list_sorted = sorted(possible_telemarketer_number_list)

    print("These numbers could be telemarketers: ","\n")
    for possible_telemarketer_number in possible_telemarketer_number_list_sorted :
        print(possible_telemarketer_number,"\n")
 
solution(calls=calls)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

