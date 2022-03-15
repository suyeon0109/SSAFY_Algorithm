for tc in range(int(input())):
    N, M = map(int, input().split())

    la = [input() for _ in range(N)]

    for i in la:
        for p in range(N-M+1):
            if i[p:p+M] == i[p:p+M][::-1]:
                print(f'#{tc+1}',i[p:p+M])
                break

    for j in range(N):
        m = ''
        for k in la:
            m += k[j]
        for p in range(N-M+1):
            if m[p:p+M] == m[p:p+M][::-1]:
                print(f'#{tc+1}',m[p:p+M])
                break