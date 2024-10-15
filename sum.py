''' Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60'''

input_values = input().strip().split()
values_tuple = tuple(map(int, input_values))
total_sum = 0
for value in values_tuple:
    total_sum += value
print(total_sum)
