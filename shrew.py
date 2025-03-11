from math import floor, ceil


n = int(input())
min = 0
max = ceil(n / 2)

while n != 0:
    n = ceil(n/2)-1
    min += 1
print(min, max)
