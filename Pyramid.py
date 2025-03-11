t = int(input())
list_of_examples = []
for i in range(t):
    n, m = map(int, input().split())
    list_of_examples.append([n, m])


def define_number(n, m):
    number = 0
    while True:
        number += n*m
        n -= 1
        m -= 1
        if n == 0 or m == 0:
            break
    return number


for list in list_of_examples:
    print(define_number(list[0], list[1]))





