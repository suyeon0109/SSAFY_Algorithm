for i in range(int(input())):
    a,b = map(int, input().split())
    la = list(map(int, input().split()))
    max = 0
    min = 0

    for j in range(len(la)-b+1):
        sum = 0
        for k in range(b):
            sum += la[j+k]
        print(sum)
        if min == 0:
            min = sum
        if sum < min:
            min = sum
        if sum > max:
            max = sum
        print(min, max)

    print(f'#{i+1}', max-min)