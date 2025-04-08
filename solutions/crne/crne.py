x = int(input())
hCuts = x//2
vCuts = x//2 + x % 2
cuts = (hCuts+1)* (vCuts + 1)
print(cuts)
