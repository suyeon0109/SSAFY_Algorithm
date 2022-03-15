for i in range(int(input())):
    la = []
    for j in range(int(input())):
        A, B = map(int,input().split())
        for k in range(A, B+1):
            la.append(k)
    lb = []
    p = int(input())
    for m in range(p):
        lb.append(int(input()))
    
    lc = [0]*p
    for n in range(len(lb)):
        for q in la:
            if lb[n] == q:
                lc[n] += 1
    
    print(f'#{i+1}',*lc)