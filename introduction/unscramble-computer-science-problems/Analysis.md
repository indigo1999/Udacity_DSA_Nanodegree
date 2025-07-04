
## Task0
**Description**: The task is to get first record of texts and last record of calls

**Approach**: For the first record of texts, I accessed them directly through accessible row index.For the last record of calls, I created function to calculate length of array for that I can get it later in order to access the last row index of calls record. Finally I concatenated each of them with the message for printing out.

**Complexity Analysis**:
- **Algorithm**: The algorithm begins with storing two values, first-record-of-text message and last-record-of-call message . The first-record-of-text message is a string message which on the inside of it is concatenated with the accessible first row index of text and accessible indexes of its columns. last-record-of-call message is done similarly to the previous but on the inside of it is concatenated with the row index calculated from the built function to return the length of array of call and accessible column indexes. Finally the algorithm prints out the stored values, the concatenated messages, 2 times. 
- **Big O Notation**:$O(n)$. where n is length of calls record 
- **Justification**: Storing first_record_of_text value and printing out 2 stored values are O(1). Storing last_record_of_call value called list_len() function 3 times which each time has O(n) so it results in O(3n). The overall would be O(n) not O(3n)


## Task1
**Description**:  The task is to count the total number of distinct phone numbers present in both datasets (calls and texts), including both caller and receiver numbers.

**Approach**: I created a list, different_number list, for containing distinct phone numbers from both records, calls and texts. I built a function, list_len function for calculating length of different number list. I iterated through each records and each iteration I checked if the caller/sender and receiver of the each iteration is already in the different_number list. If it wasn't already in the list, just added it in the list.After all, I printed out a message formated with result from list_len function. 

**Complexity Analysis**:
- **Algorithm**: 
1. Initialize an empty list called different_numbers

2. For each text in texts:

    - If sender is not in different_numbers, append sender to different_numbers

    - If receiver is not in different_numbers, append receiver to different_numbers

3. For each call in calls:

    - If caller is not in different_numbers, append caller to different_numbers

    - If receiver is not in different_numbers, append receiver to different_numbers

4. Create list_len function for calculating length of different_number list  

5. Print the message and call list_len function to get its result into the message.

- **Big O Notation**: $O( (t+c)^2 )$ where t is amount of texts record and c is amount of calls record.
- **Justification**:  In the worst case, all phone numbers are distinct, sender and receiver, we will process up to 2t + 2c phone numbers in total. the different_numbers list will grow to size not bigger than 2t+2c. Inside the first loop,there are 2 "not in" operations per iteration which performs linear search over the list - that's O(k) where k is the current length of different_numbers. Assume each phone number is unique then the total cost of all the not in checks is O (1 + 2 + 3 + ... + (2t+2c)) = O ((2t+2c)^2) . The second loop is similar to the previous one, O((2t+2c)^2). Finally, overall O is O((2t+2c)^2) which is O((t + c)^2). 



## Task2
**Description**: The task to find which telephone number spent the highest time on phone and how long does the number take.

**Approach**: Before get into coding the main function, solution function, I created 3 functions as my helper functions which are list_len, string_to_integer_seconds and dict_get_by_key functions. The list_len is a function for calculating length input list. The string_to_integer_seconds function is a function for convert string into integer type. The dict_get_by_key is a function for get a value from the input dictionary by given key. Here comes the solution function, I created a dictionary named "phone_dict". I iterated through calls record, calling dict_get_by_key function to get its value and to ensure the key existence. After get the value, I increment it with the time unit integer after converting type with string_to_integer_seconds. I did these processes with both caller and receiver number.

After I get the completed phone_dict dictionary, I make 2 variables, max_time_spent and max_time_phone_number. I iterated through phone_dict. If in-checking value is more than previous max_time_spent value, it will replace the previous value with in-checking value and replace the max_time_phone_number with in-checking key. 

Finally, I printed out the message formatted with max_time_spent and max_time_phone_number variables.

**Complexity Analysis**:
- **Algorithm**: 
1. Initialize a dictionary phone_dict to keep track of the total call duration (in seconds) for each phone number.

2. Iterate over each call in the list calls:

    - For the caller (call[0]) and the receiver (call[1]), do the following:

        - Convert the call duration string (call[3], e.g. "120") into an integer number of seconds using the helper function string_to_integer_seconds.

        - Add this duration to both the caller's and receiver's total in phone_dict.

3. Find the phone number with the maximum total time:

    - Initialize max_time_spent and max_time_phone_number.

    - Loop through the keys in phone_dict and update these variables when a higher total duration is found.

4. Print the result using print().
- **Big O Notation**:$O(nk)$ where n is the length of calls record and k is average length of the duration string.
- **Justification**: The dict_get_by_key function is a function for searching key existence and return its value which dictionary key lookup is O(1) average case. The string_to_integer_seconds is a function to convert string into integer.In this function with considering the worst case, the outer loop has to process through input string k times.The inner loop has to process through string_to_number_dict dictionary 10 times, so it will be O(10k) which is O(k) after drop the constant value. The next loop for this function, it iterated through integer_list k times and each time it called list_len function which its Big O is O(k), k is length of input list. For this function, we get O(k + kk) or O(k^2). Back to main function, Iterating through calls record n times and each time it called dict_get_by_key 2 times and string_to_integer_seconds 2 times which overall O for this loop is O(n(k^2+k^2)), O(n(k^2)). The last loop, In worst case every call involves two unique numbers. the phone_dict will consist of 2n phone numbers and the last loop has to iterate through this dictionary 2n times, O(2n), O(n). The rest of all, each of them is O(1). Finally, overall O is O(n(k^2)+n), O(n(k^2)).

## Task3
**Description**: There are 2 tasks to do, finding all area codes from telephone number which was called by people in Bangalore and calculating the percentage of calls
were made to a number also starting with (080) which was called from the number also started with (080). 

**Approach**: I built 6 helper functions, is_from_Bangalore, is_fixed_line_number, is_mobile_number, is_telemarketer_number, find_index_of_input and list_len. In main function, I made a list, area_code, and declared 2 variables which are numerator and denominator. I iterated through calls record. If the caller is from Bangalore then denominator value will be incremented.After this checking, if the receiver is the fixed line number and its area code is not already existed in the area_code list then add its area code into the list. If the receiver is just a mobile number and its area code is not already existed in the area_code list then add its area code into the list. If the receiver is a telemarketer number which its area code is 140 and its area code is not already existed in the area_code list then add its area code into the list.If the receiver is also from Bangalore then denominator value will be incremented. I sort the area_code list and dividing numerator with denominator, multiply it with 100 and round it up 2 decimal places.After all, I printed out the message and printed all of the area code list and printed out the formatted message.

**Complexity Analysis**:
- **Algorithm**: 
1. Initialize variables
    - area_code: An empty list to store unique area codes or prefixes.
    - numerator: Counter for how many calls from Bangalore are to Bangalore.
    - denominator: Counter for how many calls are from Bangalore.
2. Loop over all call records
    - For each call:
        Check if the caller is from Bangalore ("(080)"). If yes, increment the denominator by 1.
        Based on the type of the receiver's number, extract the area code or prefix:
            - Fixed line: Use find_index_of_input(")", call[1]) to locate the end of area code, and extract substring like "(XYZ)".
            - Mobile number: Extract the first 4 digits.
            - Telemarketer: Code is "140".
        Add the code to area_code only if not already present.If the receiver is also from Bangalore, increment numerator.
3. Sort the collected area codes/prefixes
4. Calculate percentage
5. Output the results
    - Print all collected area codes or prefixes (sorted).
    - Print the calculated percentage of Bangalore-to-Bangalore fixed line calls (to two decimal places).

- **Big O Notation**:$O(n^2+nlogn)$ where n is size of calls record.
- **Justification**: Before all, There are 4 helper functions which each of them has O(1), is_from_Bangalore, is_fixed_line_number, is_mobile_number and is_telemarketer_number function. The list_len function has O(m) because inside of this function is just an iteration though an input which its length could be defined as m.The other helper function is find_index_of_input. This function iterates through an input m times where m is length of input which can be calculated with The list_len. The loop inside this function has to circulate m times in worst case, each time it's call list_len which cost O(m). So it will be O(m^2) for this function. Due to fixed and small length of input or phonenumber, then it can be more like O(1^2) or O(1). In main function, Looping through calls record cost O(n) as n denoted to length of calls record. Inside this loop, there are 4 checking condition which applied the mentioned first 4 helper functions which each of them cost O(1). Slicing index cost O(1). Checking if new area code is already in the area_code list is O(k) as area_code grown length grown as k and another reason why it's costed O(k) is because it's linear search. Sorting area_code with a buit-in function cost O(klogk).Looping through the sorted area_code list cost O(k). Finally after combine all O, it will be O(n [(1+1+k) + (1+k) + (1+k) + 1] + klogk + 1 + k + 1 ) or O(3nk+k+5n+2+klogk). In worstcase, k ~= n, Hence, it will be O(3n^2+6n+nlogn+2) or O(n^2+nlogn).

## Task4
**Description**: The task is to identify all possible number that could be telemarketer number.

**Approach**: I created 2 lists,out_going and non_tele. I iterated through calls and texts record. In loop of calls record, I added each caller into out_going list and each receiver into non_tele list. In loop of texts record I added each sender and receiver into non_tele list. I converted the 2 lists into set, make subtraction and convert the result into a list then sorted this list. Finally, I printed out the message and iterated through the sorted list to print each number out.


**Complexity Analysis**:
- **Algorithm**: 
1. Initialize Lists:
    - out_going: to store numbers that make calls.
    - non_tele: to store numbers that receive calls, send texts, or receive texts.
2. Process Call Records:
    - For each call:
        - If the caller (call[0]) is not already in out_going, add it.
        - If the receiver (call[1]) is not already in non_tele, add it.
3. Process Text Records:
    - For each text:
        - If the sender (text[0]) is not already in non_tele, add it (note: this line has a bug, explained below).
        - If the receiver (text[1]) is not already in non_tele, add it.
4. Identify Telemarketers:
        - Use set difference: set(out_going) - set(non_tele) to get numbers that only make calls and never appear elsewhere.
        - Convert the result to a sorted list.
5. Output:
        - Print the sorted list of suspected telemarketer numbers.
- **Big O Notation**:$O(c^2 + t^2 + klogk)$ where c is size of calls record, t is size of texts record and k is size of list of possible telemarketer numbers.
- **Justification**: Iteration through calls record has O(c) which c is size of the record. In worst case, if both caller and receiver are not already in out_going and non_tele list so each of 2 linear searching will cost O(2c).The first loop will overally cost O(c(2c)) or O(2c^2). Iteration through texts record has O(t) which t is size of texts record. In worst case,both text sender and text receiver are not already in non_tele list. The text sender linear checking will cost O(c) at first round of the loop and the text receiver linear checking will cost O(c + 1) because the text sender already appended in the list. In the 2nd round,The text sender linear checking will cost O(c + 1) at first round of the loop and the text receiver linear checking will cost O(c + 2) because the text sender already appended in the list. In the 3rd round, The text sender linear checking will cost O(c + 2) at first round of the loop and the text receiver linear checking will cost O(c + 3) because the text sender already appended in the list. So overall of the linear checking for text sender will be O( c + c + 1 + c + 2 + c + 3 + ... + c + t-1) or O(t^2 + ct - c) shortly. The the linear checking for text receiver will cost O(c + 1 + c + 2 + c + 3+ ... + c + t) or O(t^2 + ct) shortly.The difference between the out_going and non_tele lists is calculated using set operations. This operation has a time complexity of O(k), where k is the length of the resulting difference. Sorting this difference takes O(k log k).Printing the results has a time complexity of O(k), where k is the number of potential telemarketer numbers. Combining all O, it will be O(2c^2 + 2t^3 + 2ct^2 - c + klogk + k + 1) or O(2c^2 + t^2(2t+2c)+klogk+k+1-c) or O(c^2+t^2+klogk).