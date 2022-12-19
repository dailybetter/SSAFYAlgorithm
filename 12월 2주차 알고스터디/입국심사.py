n, m = map(int, input().split())
gate_li = []
mini = 21e8
maxi = 0
for _ in range(n):
    t = int(input())
    mini = min(mini, t)
    maxi = max(maxi, t)
    gate_li.append(t)
maxi *= m
ans = 0
while mini <= maxi:
    mid = (mini +maxi) //2
    p = 0
    for i in gate_li:
        p += mid // i
    if p < m:
        mini = mid +1
    elif p >= m:
        ans = mid
        maxi = mid -1
print(ans)

