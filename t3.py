''' Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60'''

n = int(input())
values = []
for _ in range(n):
    value = int(input())
    values.append(value)
values_tuple = tuple(values)
total_sum = sum(values_tuple)
print(total_sum)
