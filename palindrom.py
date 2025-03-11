word = list(input().strip())


def can_be_palindrom(word):
    mistakes = []

    for symbol in range(len(word)//2):
        if word[symbol] != word[-symbol-1]:
            mistakes.append(symbol)

    if len(mistakes) >= 3:
        return "NO"
    if not mistakes:
        return "YES"
    if len(mistakes) == 1 and len(word) % 2 == 0:
        return "NO"
    if len(mistakes) == 2:
        word[mistakes[0]], word[mistakes[1]] = word[mistakes[1]], word[mistakes[0]]
        return "YES" if word == word[::-1] else "NO"
    if len(mistakes) == 1 and len(word) % 2 == 1:
        word[mistakes[0]], word[len(word)//2+1] = word[mistakes[len(word)//2+1]], word[mistakes[0]]
        return "YES" if word == word[::-1] else "NO"


print(can_be_palindrom(word))

