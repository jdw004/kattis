k, n = map(int, input().split())
import itertools

def get_digit_permutations():
    perms = [''.join(p) for p in itertools.permutations(codes[0], k)]
    return perms

codes = []

def checkWord(word, perm):
    pointer = 0

    for i in range(len(word)):
        if pointer == len(perm):
            break

        if word[i] == perm[pointer]:
            pointer += 1

    return len(perm) == pointer

for _ in range(n):
    entry = input()
    codes.append(entry)

prev = [0] * len(codes)

# build pos
perms = get_digit_permutations()
    
answers = []
answerSet = set()
#try pos for each word
for i in range(len(perms)):

    for word in codes:
        result = checkWord(word, perms[i])

        if not result:
            break
    else:
        if perms[i] in answerSet:
            continue
        answerSet.add(perms[i])
        answers.append(perms[i])

answers.sort()
print(len(answers))
for a in answers:
    print(a)

