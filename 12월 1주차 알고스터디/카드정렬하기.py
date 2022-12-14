n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort()
answer = 0
while True:
    if len(li) <= 2:
        answer += sum(li)
        break
    cli = []
    for i in range(1,len(li)//2 +1):
        cli.append(li[i*2-1]+li[i*2])
        answer += (li[i*2-1]+li[i*2])
    if len(li)%2 == 1:
        cli.append(li[-1])
    li = cli
print(answer)

