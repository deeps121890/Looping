'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
yes
'''
# Function to check if n is a factorial number
def is_factorial(n):
    if n < 1:
        return False
    factorial = 1
    i = 1
    while factorial < n:
        i += 1
        factorial *= i
    return factorial == n

# Input reading
n = int(input())

# Check and print the result
if is_factorial(n):
    print("yes")
else:
    print("no")
