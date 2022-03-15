def rsp(a,b):
    if la[a] == la[b]:
        return b
    elif la[a] - la[b] == 1:
        return b
    elif la[b] - la[a] == 1:
        return a
    elif la[a] - la[b] == 2:
        return a
    elif la[b] - la[a] == 2:
        return b
    
for tc in range(int(input())):
    n = int(input())
    la = list(map(int, input().split()))
    p = [i for i in range(len(la))]
    while len(p) > 1:
        print(p)
        for j in range(0,len(p[:]),2):
            p.remove(rsp(j,j+1))
    print(p)
    