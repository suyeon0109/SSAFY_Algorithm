def part(la,s,e):
    L,R = s,e
    pivot = (s+e)//2
    while L<R:
        while L<R and la[L]<la[pivot]:
            L += 1
        while L<R and la[R] >= la[pivot]:
            R -= 1
        if L<R:
            if L==pivot:
                pivot = R

        la[L],la[R] = la[R],la[L]
    la[pivot], la[R] = la[R], la[pivot]
    return R # 다음 피봇 인덱스

def quick(la, s, e):
    if s<e :
        p = part(la, s, e)
        quick(la, s, p-1)
        quick(la, p+1, e)
    return la

for tc in range(int(input())):
    n = int(input())
    s, e = 0, n-1
    la = list(map(int, input().split()))
    print(f'#{tc+1}',*quick(la, s, e))