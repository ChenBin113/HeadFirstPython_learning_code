# 之前的代码
try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as er:
    print('File error' + str(er))
finally:
    if 'data' in locals():
        data.close()

# 版本1：
try:
    data = open('its.txt', 'w')
    print('It', file=data)
except IOError as err:
    print('File error: ' + str(err))
finally:
    if 'data' in locals():
        data.close()

# 版本2：上下文管理协议（conetext management protocol）
try:
    with open('its.txt', 'w') as data:
        print("It", file=data)
except IOError as err:
    print('File error: ' + str(err))

# 练习1
try:
    with open('man_data.txt', 'w') as man_file:
        print(man_file, file=man_file)
    with open('other_data.txt', 'w') as other_file:
        print(other_file, file=other_file)
except IOError as err:
    print('File error: ' + str(err))

# 练习2
# try:
#     with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
#         print(man, file=man_file)
#         print(other, file=other_file)
# except IOError as err:
#     print('File error: ' + str(err))
