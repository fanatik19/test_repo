n = int(input())
k = 0
number = (k*(k+1))/2

def calculate_the_size(k):
    return (k * (k + 1) * (k + 5)) / 6 - 1

while True:
    previous_k = k
    k += 1
    size = calculate_the_size(k)
    if size > n:
        print(previous_k)
        break