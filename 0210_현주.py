for i in range(int(input())):
    N,Q = map(int,input().split())
    la = [0]*N
    for j in range(Q):
        L,R = map(int,input().split())
        for k in range(L-1,R):
            la[k]=j+1
    
    print(f'#{i+1}',*la)