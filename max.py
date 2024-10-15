'''

5) Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30'''

n = int(input())
values = []
for _ in range(n):
    value = int(input())
    values.append(value)
values_tuple = tuple(values)
max_value = max(values_tuple)
print(max_value)

