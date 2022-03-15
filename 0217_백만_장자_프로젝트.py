for tc in range(int(input())):
    m = int(input())
    b = list(map(int,input().split()))
    r = []

    def revenue(b):
        m = 0
        for i in range(len(b)):
            if b[i] > m:
                m = b[i]
                idx = i

        b_n = b[:idx+1]
        a = b_n[-1]*(len(b_n)-1)-sum(b_n[:-1])
        del b[:idx+1]
        return a

    while b !=[]:
        r.append(revenue(b))

    print(f'#{tc+1}',sum(r))