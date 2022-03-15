for m in range(int(input())):

    count = [0]*10
    n = input()
    for i in range(len(n)):
        count[int(n[i])] += 1

    for j in range(len(count)):
        if count[j] >= 3:
            count[j] -= 3

    for k in range(0,8):
        if count[k] == count[k+1] == count[k+2] == 1:
            count[k] -= 1
            count[k+1] -= 1
            count[k+2] -= 1

    if count == [0]*10:
        print(f'#{m+1}',1)
    else:
        print(f'#{m+1}',0)

