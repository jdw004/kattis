from collections import defaultdict
n = int(input())
need = 1
freq = defaultdict(int)
for _ in range(n):
    num = int(input())

    freq[num] += 1


for key, val in freq.items():

    if key % 2 == 0:
        pix = 1 + key // 2 + val // 2
    else:
        pix = (key+1)//2 + (val+1) // 2

    need = max(need, pix)

print(need)
