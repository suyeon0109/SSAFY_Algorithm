num = ['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']
hex_bin = {'A':'1010', 'B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

for tc in range(int(input())):
    hexa = input()
    code = ''
    la = []
    for i in range(len(hexa)):
        if hexa[i].isdigit():
            if len(format(int(hexa[i]), 'b')) < 4:
                code += '0'*(4-len(format(int(hexa[i]), 'b'))) + format(int(hexa[i]), 'b')
            else:
                code += format(int(hexa[i]), 'b')
        else:
            code += hex_bin[hexa[i]]
    
    for j in range(-1,-len(code),-1):
        if code[j] == '1':
            break

    for k in range(j,-len(code),-6):

        if code[k-5:k+1] in num:
            la.append(num.index(code[k-5:k+1]))
    la.reverse()

    print(f'#{tc+1}',*la)