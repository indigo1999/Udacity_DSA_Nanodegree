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

def is_from_Bangalore (input_number) :
    
    #check brackets
    if input_number[0] == "(" and input_number[4] == ")" :
      if input_number[1:4] == "080" :
        #print("True")
        return True

    #print("False")
    return False

#is_from_Bangalore("(080)xxxxxx") 1

def is_in_bangalore_number_list (input_check,bangalore_number_list) :

   if input_check in bangalore_number_list :
      return True

   return False

# k

def solution (calls) :
   
   Both_not_from_bangalore_total = 0
   Only_one_from_bangalore_total = 0
   Both_from_bangalore_total = 0

   bangalore_number_list = [] # k

   for call in calls : # n
      if is_from_Bangalore(call[0]) == False and is_from_Bangalore(call[1]) == False :
         Both_not_from_bangalore_total += 1
      
      elif (is_from_Bangalore(call[0]) == True and is_from_Bangalore(call[1]) == False) :
         Only_one_from_bangalore_total += 1

         if is_in_bangalore_number_list(call[0],bangalore_number_list) == False :
            bangalore_number_list += [call[0]]
         
      elif is_from_Bangalore(call[0]) == False and is_from_Bangalore(call[1]) == True :
         Only_one_from_bangalore_total += 1

         if is_in_bangalore_number_list(call[1],bangalore_number_list) == False :
            bangalore_number_list += [call[1]]
      
      elif is_from_Bangalore(call[0]) == True and is_from_Bangalore(call[1]) == True :
         Both_from_bangalore_total += 1

         if is_in_bangalore_number_list(call[0],bangalore_number_list) == False :
            bangalore_number_list += [call[0]]

         if is_in_bangalore_number_list(call[1],bangalore_number_list) == False :
            bangalore_number_list += [call[1]]
   
   percentage_both_from_bangalore = ( Both_from_bangalore_total / ( Both_not_from_bangalore_total + Only_one_from_bangalore_total ) ) * 100
   bangalore_number_list_sorted = sorted(bangalore_number_list)

   print("The numbers called by people in Bangalore have codes: ")
   for bangalore_number in bangalore_number_list_sorted :
      print(bangalore_number,"\n")

   print(f"{percentage_both_from_bangalore:.2f}" ," percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

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
