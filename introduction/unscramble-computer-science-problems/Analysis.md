## Task_explaination_what_to_type
**Description**: type what the task wants me to do.

**Approach**: type the brief explanation like story-telling of my pseudocode
**Complexity Analysis**:
- **Algorithm**: type to explain the algorithm of my solution function
- **Big O Notation**:$O(n)$. type Big O
- **Justification**: type the reason why I my Big O result become like this (explain in sequence) 


## Task0
**Description**: The task is to get first record of texts and last record of calls

**Approach**: For the first record of texts, I accessed them directly through accessible row index.For the last record of calls, I created function to calculate length of array for that I can get it later in order to access the last row index of calls record. Finally I concatenated each of them with the message for printing out.
**Complexity Analysis**:
- **Algorithm**: The algorithm begins with storing two values, first-record-of-text message and last-record-of-call message . The first-record-of-text message is a string message which on the inside of it is concatenated with the accessible first row index of text and accessible indexes of its columns. last-record-of-call message is done similarly to the previous but on the inside of it is concatenated with the row index calculated from the built function to return the length of array of call and accessible column indexes. Finally the algorithm prints out the stored values, the concatenated messages, 2 times. 
- **Big O Notation**:$O(n)$. where n is length of calls record 
- **Justification**: Storing first_record_of_text value and printing out 2 stored values are O(1). Storing last_record_of_call value called list_len() function 3 times which each time has O(n) so it results in O(3n). The overall would be O(n) not O(3n)






## Task1
**Description**: The task is to find the amount of distinct telephone numbers in the records.

**Approach**:  I created the list for stored up distinct telephone numbers. Then, I iterated through each records which each of them has to be checked for distinct telephone numbers when compared to the added in the created list. Finally, I printed out the message concatenated with the amount of distinct telephone numbers from the created list, the amount of numbers is calculated with the built function.
**Complexity Analysis**:
- **Algorithm**: 
1.Creating a list for stored up the distinct telephone numbers
2.Do looping through texts record and check if the telephone number in texts is duplicate compare to the built list. If it's not duplicate then add it to the list.
3.Do looping again through calls record and check if the telephone number in calls is duplicate compare to the built list. If it's not duplicate then add it to the list.
4.Built function for calculating the amount, length, of list
5.Print out the message concatenated with the length of list which is calculated with the function in 4.
- **Big O Notation**:$O(n^2 + m^2 + m*n)$ where n is size of texts record and m is size of calls record. 
- **Justification**: The first loop is iterate through texts record n times. In worstcase, if every of checked number from texts record is not in different_numbers list, it must iterate through the list from 1 to n times which leads to the result of n times. So the first loop is n multiply with n or n^2. The second loop is similar to the first loop by m is size of calls record. In worstcase, if there's no duplicate number in the differnt_number list which has size equal to n, the checking loop has to check n+m times. Thus, overall of the second loop is m*(n+m). Finally, O(n^2 + m*(n+m)) or O(n^2 + m^2 + n*m) 






## Task2
**Description**: The task is to identify which telephone number spent the longest time and how long it tooks on phone in seconds.

**Approach**: I iterated through calls record, stored the duration in seconds in a value, compared it with the previous duration and if the previous duration is less than the current one, I stored the current one replace with the previous one and save its telephone number. After the iteration completed, it will be printed out in formatted message which has the longest duartion and its telephone number.  
**Complexity Analysis**:
- **Algorithm**:
1. Built up 2 variables, answer and telephone number
2. Looping through calls record
3. Built string_to_integers_seconds function for converting string of call duration into integer type
4. Convert string of call duration into integer with string_to_integers_seconds function and store it in a variable, compare_to_answer.
5. If answer value is less than compare_to_answer value then answer value will be replaced with compare_to_answer value and save its telephone number which belongs to the comapre_to_answer into telephone number variable.
6. Bring the final 2 values, answer and telephone number into formatted message and print it out. 

- **Big O Notation**:$O(n*(k^2))$ where n is number of calls record and k is length of string of call duration 
- **Justification**: For the reason that I give k^2 is that it's come from time complexity efficiency of string_to_integer_seconds function. For worstcase of this function, the loop will iterate 10 times per character ('0' to '9') to find the match character. Thus, the loop iterate k times which k is length of input string then there will be O(10*k) or O(k) , drop 10 because it is constant factor. For the last loop, it iterate through integers_list k times, k is length of integers_list. The next line, it called list_len function k times. Thus the last loop is O(k^2). Overall for this function will be O(k^2). Back to the main function, solution function, the loop iterated through calls record n times and each time it calls string_to_integer_seconds 1 times. Hence, there will be O(n * k^2) for overall of the solution function.  






## Task3
**Description**: There are 2 tasks to be done. First, I have to find all distinct telephone numbers from Bangalore. Second, I have to calculate the percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore.

**Approach**: I create is_from_Bangalore function to check if input telephone number is from Bangalore.I create is_in_bangalore_number_list function to check if the input telephone number is in Bangalore number list. I iterate through calls record and check if either calling number or receiving number is in the Bangalore number list. Then, I count the amount of score if either or neither of calling and receiving number is from Bangalore. After all, I calculate percentage of score if both calling and receiving number are from Bangalore and sort the Bangalore number list. Then, I iterate through the sorted list and print out each of them and print out the percentage score.
**Complexity Analysis**:
- **Algorithm**:
1. Initialize counters and data structure
    1.1 Set Both_not_from_bangalore_total to 0.
    1.2 Set Only_one_from_bangalore_total to 0.
    1.3 Set Both_from_bangalore_total to 0.
    1.4 Create an empty list bangalore_number_list.
2. Process each calls record, check call origin and destination
    - If neither the caller nor the receiver is from Bangalore then Increment Both_not_from_bangalore_total.

    - If only the caller is from Bangalore then increment Only_one_from_bangalore_total.

    - If the caller number is not already in bangalore_number_list then add the caller number to bangalore_number_list.

    - If only the receiver is from Bangalore then increment Only_one_from_bangalore_total.

    - If the receiver number is not already in bangalore_number_list then add the receiver number to bangalore_number_list.

    - If both the caller and receiver are from Bangalore then increment Both_from_bangalore_total.

    - If the caller number is not already in bangalore_number_list then add the caller number to bangalore_number_list.

    - If the receiver number is not already in bangalore_number_list then add the receiver number to bangalore_number_list.
3. Calculate Percentage of Bangalore-to-Bangalore calls
4. Sort and Print Bangalore Numbers
5. Print Percentage Result

- **Big O Notation**:$O(n*k + k*log k)$ where n is size of calls record and k is size of distinct bangalore number list.
- **Justification**: is_from_Bangalore function has O(1). is_in_bangalore_number_list function is iterate through input list k times which k is size of input list so this function has O(k).In worstcase, if both caller and receiver are from Bangalore and they are not in Bangalore number list, it has to call is_in_bangalore_number_list 2 times which O will be O(2k) or O(k) as the input list size for is_in_bangalore_number_list function will grow as k. Combining the loop and the inside of the loop will be n times k,or O(n*k), n is size of calls record. Calculating for percentage amount is O(1). Sorting the list has O(klog k). Looping through the sorted list and print each of them has O(k). The last line is printing out a formatted message which has O(1). So overall of the solution function will be O(nk + klogk + 1 + k + 1), After dropping constant value,we get O(nK + klogk).   






## Task4
**Description**: The task to identify all distinct telephone number which could be telemarketer number. 

**Approach**: I created an empty list for containing possible telemarketer number. Iterate through calls record and check if either caller or receiver is a telemarketer and if it is not already in the created list, add it into the list in case that it passes 2 conditions.
**Complexity Analysis**:
- **Algorithm**:
1. Initialize an Empty List, possible_telemarketer_number_list.
2. Process each call in the call records
    2.1 Check the caller If it is a telemarketer number and it is not already in possible_telemarketer_number_list then add caller to the list.
    2.2 Check the receiver If it is a telemarketer number and it is not already in possible_telemarketer_number_list then add receiver to the list.
3. Sort the possible_telemarketer_number_list.
4. Print the result
    4.1 Print the message: "These numbers could be telemarketers:"
    4.2 For each number in the sorted list, print the number.
- **Big O Notation**:$O(n*k + k*log k)$ where n is size of calls record and k is size of distinct telemarketer numbers.
- **Justification**: The loop iterate through calls record n times which n is size of the record. The loop has O(n). The is_telemarketer_number function is only do slicing string and comparison which leads its O to be O(1). While the loop was iterating through the record and proceed to 2 conditions to be checked if either caller or receiver is telemarketer number and isn't in the distinct list, it added the number into the list. Then, the size of list will be grown as k and the checking process of incoming number if it's already in the list will process k times which leads to O(k). Sorting the distinct number list has O(klogk). Printing out a message has O(1) and Looping through the sorted list and print each of them has O(k). Finally, after combining every lines, it will be O(nk + klogk + 1 + n) which is O(nk + klogk), after dropping constant value.  