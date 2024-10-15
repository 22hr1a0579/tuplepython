''' Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6'''


input_values = input().strip().split()
values_tuple = tuple(map(int, input_values))
x = int(input().strip())
count_x = values_tuple.count(x)
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
factorial_value = calculate_factorial(count_x)
print(factorial_value)
