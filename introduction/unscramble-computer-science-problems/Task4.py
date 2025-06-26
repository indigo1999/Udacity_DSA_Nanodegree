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
    return input_number[0:3] == "140" 
        
def solution(calls,texts) :

    out_going = []
    non_tele = []

    for call in calls :
        if call[0] not in out_going :
            out_going += [call[0]]
        
        if call[1] not in non_tele :
            non_tele += [call[1]]

    for text in texts :
        if text[0] not in non_tele :
            non_tele += text[0]
        
        if text[1] not in non_tele :
            non_tele += text[1]

    difference = list(set(out_going)-set(non_tele))
    difference = sorted(difference)

    print("These numbers could be telemarketers: ")
    for code in difference :
        print(code)
 
solution(calls=calls,texts=texts)
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

