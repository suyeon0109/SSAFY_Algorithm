for tc in range(10):
    N = int(input())
    pswd = list(map(int, input().split()))
    M = int(input())
    order = list(map(str, input().split()))

    i = 0
    while i < len(order):
        k = int(order[i+2])
        while k >= 1:
            pswd.insert(int(order[i+1]),order[i+2+k])
            k -= 1
        i += 3 + int(order[i+2])
    
    print(f'#{tc+1}',*pswd[:10])
