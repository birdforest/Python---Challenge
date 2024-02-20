- # Python---Challenge
- PyBank &amp; PyPoll

- PyBank Challenge:

- The total number of months included in the dataset: Methodology used is to iterate the loop by row to sum up the number of months. Using similar concept as Challenge 2 (counter = counter + 1).
The net total amount of "Porfit/Losses" over the entire period: Methodology used is similar to that of calculating the total of months. Instead of adding "1" for every iteration, the net total amount considers the actual values.
The changes in "Profit/Losses" over the entire period, and then the average of those changes: Methodology used is summing up all monthly changes and divided by the number of monthly changes. I came up with the logic but used Stack Overflow to find the decimal function. The question asked on Stack Overflow is "Limiting floats to two decimal points".
The greatest increase in profits (date and amount) over the entire period: Metholodgy used is to calculate the change from month-to-month and update the list with larger change and its respective month. Stack Overflow mentions that the "else" statement is not necessary if it makes sense to the code. The question asked on Stack Overflow is "Is an else statement always needed".
The greatest decrease in profits (date and amount) over the entire period: Methodology used is the same as calculating the greatest increase in profits.

PyPoll Challenge

The total number of votes cast: Methodology used is to iterate the loop by row to sum up the number of votes. Using similar concept as Challenge 2 (counter = counter + 1).
A complete list of candidates who received votes: Methodology used is to iterate the loop to add unique candidate names to the set. I chose set over list in this scenario because duplicate elements are not preferred. Also, add function does nothing if the element is already present in the set. The source for choosing set function is based on https://docs.python.org/ and add function is based on W3Schools.
The total number of votes each candidate won: Methodology used is to go through the candidate with their corresponding votes in the dictionary created prior.
The winner of the election based on popular vote: Methodology used is to use the max function to determine the candidate with the maximum votes in the 'candidate_votes' dictionary and assigns it to the variable ' winner'. The source for applying max function is Stack Overflow. The question asked on Stack Overflow is "Getting key with maximum value in dictionary?".
