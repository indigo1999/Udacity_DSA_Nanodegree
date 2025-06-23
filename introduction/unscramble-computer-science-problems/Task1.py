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

def solution (texts,calls) :
    different_numbers = [] # 2t + 2c
    for text in texts : # t
        if text[0] not in different_numbers :
            different_numbers += [text[0]]

        if text[1] not in different_numbers :
            different_numbers += [text[1]]

    for call in calls : # c
        if call[0] not in different_numbers :
            different_numbers += [call[0]]

        if call[1] not in different_numbers :
            different_numbers += [call[1]]
    
    print("There are ",list_len(different_numbers), " different telephone numbers in the records.")



def list_len(lists) :
    count = 0
    for list_count in lists :
        count += 1
    
    return count

solution(texts=texts,calls=calls) 

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
