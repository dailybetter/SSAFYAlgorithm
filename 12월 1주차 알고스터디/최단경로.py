import heapq
n, m = map(int, input().split())
start = int(input())
inf = 1e9
# 연결 정보 리스트
graph = [[] for i in range(n+1)]


distance = [inf] * (n+1)
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in distance:
    print(i)
    
