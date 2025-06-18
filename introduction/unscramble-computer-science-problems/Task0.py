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
    first_record_of_text = "First record of texts, " + texts[0][0] + " texts " + texts[0][1] + " at time " + texts[0][2]
    last_record_of_call = "Last record of calls, " + calls[list_len(calls)-1][0] + " calls " + calls[list_len(calls)-1][1] + " at time " + calls[list_len(calls)-1][2] + ", lasting " + calls[list_len(calls)-1][3] + " seconds"
    print(first_record_of_text)
    print(last_record_of_call)
    
def list_len(lists) :
    count = 0
    for list_count in lists :
        count += 1
    
    return count

solution(texts,calls)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
    



    