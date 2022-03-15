# for tc in range(int(input())):
#     a,b = map(str, input().split())

#     print(f'#{tc+1}',len(a.replace(b,'!')))

for tc in range(int(input())):
    a,b = map(str, input().split())

    cnt = 0
    k = 0
    i = 0
    while i <= len(a) :
        if a[i+k:i+k+len(b)] == b:
            cnt += len(b)-1
            k += len(b)-1
        i += 1

    print(f'#{tc+1}', len(a)-cnt)