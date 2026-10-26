x = int(input())
freqs = {}
for _ in range(x):
    list = map(int, input().split())
    list = sorted(list)
    key = "".join(map(str, list))

    if key in freqs:
        freqs[key] += 1
    else:        
        freqs[key] = 1
maxVal, maxKey = 0, 0
for key, val in freqs.items():
    if val > maxVal:
        maxVal = val
        maxKey = key
ans = 0
for key, val in freqs.items():
    if val == maxVal:
        ans += val
    
print(ans)