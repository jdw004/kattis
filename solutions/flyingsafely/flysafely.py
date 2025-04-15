x = int(input())

for _ in range(x):
    numCities, numPilots = map(int, input().split())   
    for _ in range(numPilots):
        input()
    print(numCities-1)
