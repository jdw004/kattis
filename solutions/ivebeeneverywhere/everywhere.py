n = int(input())

for _ in range(n):
    numCities = int(input())
    mySet = set()
    for _ in range(numCities):
        x = input()
        mySet.add(x)
    print(len(mySet))
