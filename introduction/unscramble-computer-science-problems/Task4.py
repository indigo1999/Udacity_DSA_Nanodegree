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
      
def solution(calls,texts) :

    out_going = [] # max_len ==> og
    non_tele = [] # max_len ==> nt

    for call in calls : # O(c)
        if call[0] not in out_going : # O(og) ==> og ~= c ==> O(c)
            out_going += [call[0]] # O(1)
        
        if call[1] not in non_tele : # O(nt) ==> nt ~= c ==> O(c)
            non_tele += [call[1]] # O(1)

    for text in texts : # O(t)
        if text[0] not in non_tele : # worstcase, both [0] & [1] not in [] 
            #==> c , c + 1 , c + 2 , c + 3 , ... , c + t-1 ==> c(t-1) + t(t-1)/2 ==> t^2 + ct - c
            non_tele += [text[0]] # O(1)
        
        if text[1] not in non_tele : # c + 1 , c + 2 , c + 3, ... , c + t ==> ct + (1+t)t/2 ==> t^2 + ct
            non_tele += [text[1]] # O(1)

    difference = list(set(out_going)-set(non_tele))
    difference = sorted(difference) # O(klogk) ==> k is len(difference)

    print("These numbers could be telemarketers: ") # O(1)
    for code in difference : # O(k)
        print(code)
    
    #O(c [c + c] + t [t^2 +ct - c + t^2 + ct] + klogk + 1 + k) ==> O(2c^2 + 2t^3 + 2ct^2 - c + klogk + k + 1) ==> O(c^2 + t^2(t + c) + klogk) ==> O(c^2 + t^2 + klogk)

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

