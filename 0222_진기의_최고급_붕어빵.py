for tc in range(int(input())):
    N, M, K = map(int, input().split())
    la = list(map(int, input().split()))

    bung = 0 # 팔린 붕어빵 개수

    la.sort()

    for t in range(len(la)):
        if la[t]//M * K - bung > 0: # 붕어빵 남아있으면
            bung += 1
            pass
        else:
            print(f'#{tc+1}','Impossible')
            break
    
    if bung == len(la): # 붕어빵 개수가 사람수랑 같으면
        print(f'#{tc+1}','Possible')