total_digits, different_digits = map(int, input().split())
if (different_digits > total_digits or
    different_digits == 1 and total_digits > 1):
    print("Impossible")
else:
    general_pattern = '9876543210'
    pattern = general_pattern[:different_digits]
    quotient = total_digits//different_digits
    remainder = total_digits % different_digits
    result = pattern*quotient + pattern[:remainder]
    print(result)
