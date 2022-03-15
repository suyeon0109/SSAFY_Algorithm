def circular(la):
    for p in range(100,1,-1):   # p = 회문 길이

        # 가로
        for i in la:
            for t in range(0,100-p+1):
                if i[t:t+p] == i[t:t+p][::-1]:
                    return p
        
        # 세로
        for a in range(100):
            m = ''
            for j in la:
                m += j[a]
            for t in range(0,100-p+1):
                if m[t:t+p] == m[t:t+p][::-1]:
                    return p


for tc in range(10):
    n = int(input())
    la = [input() for _ in range(100)]
    
    print(f'#{tc+1}',circular(la))