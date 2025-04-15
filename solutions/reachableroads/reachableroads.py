def find(x):
    if roads[x] == x:
        return x
    roads[x] = find(roads[x])
    return roads[x]

def union(x, y):
    roads[find(x)] = find(y)

cities = int(input())
for _ in range(cities):
    numRoads = int(input())
    numPairs = int(input())

    roads = [i for i in range(numRoads)]

    for _ in range(numPairs):
        x, y = map(int, input().split())
        union(x, y)

    currAns = set()
    for i in range(numRoads):
        currAns.add(find(i))

    print(len(currAns)-1)
