for tc in range(int(input())):
    a, b = map(str, input().split())
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    srt = list(map(str, input().split()))
    new = []

    for i in num:
        for j in srt:
            if i == j:
                new.append(i)
    print(f'#{tc+1}')
    print(*new)
    