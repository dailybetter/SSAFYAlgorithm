# import sys
# input = sys.stdin.readline

def go(now, store, goal):
    global ans, visited
    if abs(now[0]-goal[0]) + abs(now[1] - goal[1]) <= 1000:
        ans = 'happy'
        return
    for j in range(len(store)):
        if abs(now[0]-store[j][0]) + abs(now[1]-store[j][1]) <= 1000 and not visited[j+1] :
            visited[j+1] = 1
            go([store[j][0], store[j][1]],store, goal)
t = int(input())
for _ in range(t):
    n = int(input())
    store_li = []
    bear = 20
    home = list(map(int, input().split()))
    for _ in range(n):
        store_li.append(list(map(int, input().split())))
    goal = list(map(int, input().split()))
    for i in range(n):
        store_li[i].append(abs(store_li[i][0] - goal[0]) + abs(store_li[i][1] - goal[1]))
    store_li.sort(key = lambda x: x[2])
    ans = 'sad'
    visited = [0]*(n+1)
    visited[0] = 1
    go(home, store_li, goal)
    print(ans)
    
    