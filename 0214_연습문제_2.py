from itertools import combinations

def subset_0(la):
    for k in range(1,len(la)+1):
        for i in set(combinations(la, k)):
            if sum(i) == 0:
                return 1
    return 0

for j in range(int(input())):
    la = list(map(int, input().split()))
    print(f'#{j+1}',subset_0(la))
