# 유니온파인드..?
n,m = map(int, input().split())
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
parent = [i for i in range(n)]
count = 0
cycle = False
for _ in range(m):
    count += 1
    y,x= map(int, input().split())
    if find(parent, y) == find(parent, x):
        print(count)
        cycle = True
        break
    else:
        union(parent, y,x)
if not cycle:
    print(0)
