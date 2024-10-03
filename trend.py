'''
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
If the given number is a trendy number, then print "Trendy Number". Otherwise, print "Not a Trendy Number".
Refer the sample output for formatting.
Sample Input:
791
Sample Output:
Trendy Number
'''
# Function to check if the number is a trendy number
def is_trendy_number(n):
    # Convert the number to string to check its length
    str_n = str(n)
    
    # Check if the number has exactly 3 digits
    if len(str_n) == 3:
        # Get the middle digit
        middle_digit = int(str_n[1])
        # Check if the middle digit is divisible by 3
        if middle_digit % 3 == 0:
            return "Trendy Number"
    
    return "Not a Trendy Number"

# Input reading
n = int(input())

# Check and print the result
result = is_trendy_number(n)
print(result)
