import math
from collections import defaultdict
import heapq

testCases = int(input())
for i in range(testCases):
    numChannels, numOutposts = map(int, input().split())
    coords = []
    for i in range(numOutposts):
        x, y = map(int, input().split())
        coords.append((x, y))


    def build():
        graph = defaultdict(list)
        n = len(coords)
        for i in range(n):
            xi, yi = coords[i]
            for j in range(i + 1, n):
                xj, yj = coords[j]
                w = math.hypot(xj - xi, yj - yi)
                graph[i].append((j, w))
                graph[j].append((i, w))
        return graph

    graph = build()

    # Prim with parent tracking
    start = 0
    visited = set()
    heap = [(0.0, start, -1)]
    mst_edges = []  # list of chosen edges as weights

    while heap and len(visited) < numOutposts:
        w, u, parent = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if parent != -1:
            mst_edges.append(w)
        for v, ew in graph[u]:
            if v not in visited:
                    heapq.heappush(heap, (ew, v, u))

    mst_edges.sort()
    # Remove the largest (numChannels - 1) edges
    cut = max(0, len(mst_edges) - (numChannels - 1))

    remaining = mst_edges[:cut]
    spacing = 0.0 if not remaining else remaining[-1]
    total_length = sum(remaining)
    print(f"{spacing:.2f}")
