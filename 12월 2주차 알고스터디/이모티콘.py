# 1 2 3 4 5 6 7 8 9 10
# 0 2 3 4 5 5
from collections import deque

n = int(input())
q = deque()
q.append([2,1,2])
min_turn = 0
visited = [0]*1001
visited[0] = 1
visited[1] = 1
while q:
    now, copy, turn = q.popleft()
    visited[now] = 1
    if now == n:
        min_turn = turn
        break
    q.append([now, now, turn+1])
    if not visited[now+copy]:
        q.append([now+copy, copy, turn+1])
    if not visited[now-1]:
        q.append([now-1,copy, turn +1])
print(min_turn)
