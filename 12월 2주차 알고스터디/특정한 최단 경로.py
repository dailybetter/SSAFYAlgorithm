import heapq
n,e = map(int, input().split())
nodes = [i for i in range(n+1)]
inf = 1e8
graph = [[] for _ in range(n+1)] 
for _ in range(e):
    y,x,cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))
v1,v2 = map(int, input().split())

def dijkstra(start):
    dist = [inf]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for i in graph[now]:
            cost = d + i[1]

            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dist
start_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

v1_path = start_dist[v1] + v1_dist[v2] + v2_dist[n]
v2_path = start_dist[v2] + v2_dist[v1] + v1_dist[n]

ans = min(v1_path, v2_path)
print(ans if ans< inf else -1)