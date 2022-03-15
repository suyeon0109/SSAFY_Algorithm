for tc in range(int(input())):
    la = [0]*26
    for i in input():
        la[ord(i) - 65] += 1

    for i in range(len(la)):
        if la[i] != 0 and la[i] != 2:
            print(f'#{tc+1}','No')
            break
    if i == len(la)-1:
        print(f'#{tc+1}','Yes')
