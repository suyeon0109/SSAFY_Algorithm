hex_bin = {'0': '0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010', 'B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
for i in range(int(input())):
    m = input()
    word = ''
    for j in range(len(m)):
        word += hex_bin[m[j]]
    la = []
    num = int(word[0])
    for k in range(1,len(word)):
        num = num * 2 + int(word[k])
        if k%7 == 6:
            la.append(num)
            num = 0
    else:
        la.append(num)
    print(f'#{i+1}',*la)