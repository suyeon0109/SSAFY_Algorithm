def rsp(s,e):
    if s == e:
        return s

    a = rsp(s,(s+e)//2)
    b = rsp((s+e)//2+1,e)

    if la[a] == la[b]:
        return a
    else:
        if (la[a]+la[b])%2 == 0:
            if la[a] < la[b]:
                return a
            else:
                return b
        else:
            if la[a] > la[b]:
                return a
            else:
                return b

for tc in range(int(input())):
    n = int(input())
    la = [0] + list(map(int, input().split()))
    ans = rsp(1,n)
    print(f'#{tc+1}',ans)