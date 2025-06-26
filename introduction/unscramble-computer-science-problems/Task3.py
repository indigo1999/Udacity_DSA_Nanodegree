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

def is_from_Bangalore (input_number) : #O(1)
    return input_number[0:5] == "(080)"

def is_fixed_line_number (input_number) : #O(1)
    return input_number[0:2] == "(0" 

def is_mobile_number (input_number) : # O(1)
    return input_number[0] in ('7','8','9')

def is_telemarketer_number (input_number) : # O(1)
    return input_number[0:3] == "140"
      
def find_index_of_input (find_input,list_input) : # O(m^2)
    index = 0
    return_index = 0
    while (index <= list_len(list_input)) : # O(m) / 1 time ==> O(m^2)
        if find_input == list_input[index] :
            return_index = index
            break
        index += 1

    return return_index


def list_len (lists) : #O(m)
    count = 0
    for list_count in lists :
        count += 1
    
    return count

def solution (calls) :
   
   area_code = [] # growth as k 

   numerator = 0
   denominator = 0

   for call in calls : # O(n)
      if is_from_Bangalore(call[0]) : # O(1) | n[ m^2 + k ]
          denominator += 1

          if is_fixed_line_number(call[1]) : # O(1)
              
              index_end = find_index_of_input(")",call[1]) # O(m^2)
              new_area_code = call[1][0:index_end+1]

              if new_area_code not in area_code: # O(k)
                  area_code += [new_area_code]


          if is_mobile_number(call[1]) : # O(1)
              
               new_area_code = call[1][0:4]

               if new_area_code not in area_code: # O(k)
                  area_code += [new_area_code]

          if is_telemarketer_number(call[1]) : # O(1)
               
               if "140" not in area_code: # O(k)
                  area_code += ["140"]    

          if is_from_Bangalore(call[1]) : # O(1)
               numerator += 1

   sorted_area_code = sorted(area_code) # O(k log k)
   result = numerator/denominator*100

   print("The numbers called by people in Bangalore have codes:")
   for code_ in sorted_area_code : # O(k)
       print(code_)

   print(f"{result:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

# O(nm^2 + nk + klogk + k) ==> O(nm^2 + klogk)

solution(calls=calls)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
