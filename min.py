'''Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10'''

n = int(input())
values = []
for _ in range(n):
    value = int(input())
    values.append(value)
values_tuple = tuple(values)
min_value = min(values_tuple)
print(min_value)

