def pascal(n):
    pascal = [[1],[1,1]]
    if n>2:
        for k in range(1,n-1):
            pascal.append([1]+[pascal[k][i]+pascal[k][i+1] for i in range(k)] + [1])
        return pascal
    elif n == 2:
        return pascal
    else:
        return pascal[:1]

for tc in range(int(input())):
    print(f'#{tc+1}')
    for j in pascal(int(input())):
        print(*j)