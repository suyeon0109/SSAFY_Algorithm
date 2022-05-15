for tc in range(int(input())):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    service_max = 0

    house = 0
    for i in city:
        house += i.count(1)
    
    cost_max = M * house

    K = 1
    cost = 0
    while cost <= cost_max:
        cost = K**2 + (K-1)**2
        if cost > cost_max:
            break
        for p in range(N):
            for q in range(N):
                service = 0
                for i in range(-K+1,K):
                    for j in range(-(K-abs(i)-1),K-abs(i)):
                        if 0 <= p+i <= N-1 and 0 <= q+j <= N-1 and city[p+i][q+j] == 1:
                            service += 1
                
                if service * M >= cost and service > service_max:
                    service_max = service
        
        K += 1
    
    print(f'#{tc+1}', service_max)