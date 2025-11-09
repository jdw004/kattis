from collections import defaultdict

n = int(input())
odd = 0

freq = defaultdict(int)
for _ in range(n):

    num = int(input())
    freq[num] += 1
    if num % 2 == 1:
        odd += 1

if freq[5] + freq[0] == n:
    print(n)
elif not odd:
    print(n)
else:
    print(1)
