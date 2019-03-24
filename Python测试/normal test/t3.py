# for i in range(100,999):
#     a = i//100%10
#     b = i//10%10
#     c = i%10
#     if a**3 + b**3 + c**3 == i:
#         print(i)
#     else:
#         pass

for i in range(100,999):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if a**3 + b**3 + c**3 == i:
        print(i)
    else:
        pass