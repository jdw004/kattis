day = -1

n = int(input())
days = list(map(int, input().split()))
days.sort(reverse=True)

for i in range(len(days)):
    curr = i + days[i] + 1
    day = max(day, curr)
print(day+1)
