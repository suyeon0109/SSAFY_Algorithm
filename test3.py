la = {1:[1,2,3], 5:[6,7,8]}
print(la)
if 5 in la:
    print('yes')
else:
    print('no')
la[6] = [9]
la[5].append(9)
print(la)
print(max(la))