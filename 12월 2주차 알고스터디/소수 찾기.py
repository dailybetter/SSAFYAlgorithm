from itertools import permutations
def ss_check(t):
    k = 0
    for i in range(2,t):
        if t%i == 0:
            k += 1
    if k ==0 and t > 1:
        return True
ans = 0
a = '011'
b = list(map(int, a))
ans_list = []
for i in range(1, 4):
    a = list(permutations(b,i))
    for j in range(len(a)):
        a[j] = list(a[j])
        l = len(a[j])
        num = 0
        for v in range(l):
            num += a[j][v]*(10**v)
        if num not in ans_list and ss_check(num):
            ans_list.append(num)
print(print(ans_list))

            
