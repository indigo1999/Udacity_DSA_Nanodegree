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
**Description**:  The task is to count the total number of distinct phone numbers present in both datasets (calls and texts), including both caller and receiver numbers.

**Approach**: I created a list, different_number list, for containing distinct phone numbers from both records, calls and texts. I built a function, list_len function for calculating length of different number list. I iterated through each records and each iteration I checked if the caller/sender and receiver of the each iteration is already in the different_number list. If it wasn't already in the list, just added it in the list.After all, I printed out a message formated with result from list_len function. 
**Complexity Analysis**:
- **Algorithm**: 
1. Initialize an empty list called different_numbers

2. For each text in texts:

    - If text/sender is not in different_numbers, append text[0] to different_numbers

    - If text/receiver is not in different_numbers, append text[1] to different_numbers

3. For each call in calls:

    - If call/caller is not in different_numbers, append call[0] to different_numbers

    - If call/receiver is not in different_numbers, append call[1] to different_numbers

4. Create list_len function for calculating length of different_number list  

5. Print the message and call list_len function to get its result into the message.

- **Big O Notation**: $O( (t+c)^2 )$ where t is amount of texts record and c is amount of calls record.
- **Justification**:  In the worst case, all phone numbers are distinct, sender and receiver, we will process up to 2t + 2c phone numbers in total. the different_numbers list will grow to size not bigger than 2t+2c. Inside the first loop,there are 2 "not in" operations per iteration which performs linear search over the list - that's O(k) where k is the current length of different_numbers. Assume each phone number is unique then the total cost of all the not in checks is O (1 + 2 + 3 + ... + (2t+2c)) = O ((2t+2c)^2) . The second loop is similar to the previous one, O((2t+2c)^2). Finally, overall O is O((2t+2c)^2) which is O((t + c)^2). 

## Task2
**Description**: 

**Approach**: 
**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**:
- **Justification**:

## Task3
**Description**: 

**Approach**: 
**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**:
- **Justification**:

## Task4
**Description**: 

**Approach**: 
**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**:
- **Justification**: