for tc in range(int(input())):
    N = int(input())
    la = [list(map(int, input().split())) for _ in range(N)]
    set_p = set({})
    cnt = 1

    lp = [0] * 201
    for i in la:
        for k in range((min(i)+1)//2, (max(i)+1)//2+1):
            lp[k] +=1 
        
    print(f'#{tc+1}',max(lp))