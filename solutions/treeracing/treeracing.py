from heapq import *
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**7)

n, m, k = map(int, input().split())
graph = defaultdict(list)
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

racers = {}
# racers mapped to their speed
# location -> (racer i, speed)
for i in range(1, m+1):
    location, s = map(int, input().split())
    racers[location] = (i, s)

root = int(input())

numCp = int(input())
special = set()
for _ in range(numCp):
    special.add(int(input()))

ans = [-1] * (m + 1)

def dfs(node, parent):
    heap = []

    if node in racers:
        rid, spd = racers[node]
        heappush(heap, (0, -spd, rid))

    for nbr in graph[node]:
        if nbr == parent:
            continue
        child = dfs(nbr, node)

        # shift arrivals
        for i in range(len(child)):
            arr, negSpd, rid = child[i]
            child[i] = (arr - (-negSpd), negSpd, rid)

        # merge small to large using list extend + heapify
        if len(child) > len(heap):
            heap, child = child, heap
        heap.extend(child)
        heapify(heap)

    if node in special and len(heap) > k:
        heap[:] = nlargest(k, heap)
        heapify(heap)

    if node == root:
        for negArr, _, rid in heap:
            ans[rid] = -negArr

    return heap



dfs(root, 0)
for i in range(1, len(ans)):
    print(ans[i])