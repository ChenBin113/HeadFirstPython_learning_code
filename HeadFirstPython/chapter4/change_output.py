import os
os.chdir(r'F:\1【Python】编码项目\HeadFirstPython\chapter4')

from HeadFirstPython.chapter1.nester import print_lol
import pickle

man = []
other = []

try:
    data = open('sketch4.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            # strip从字符串中去除不想要的空白符
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The file is missing!')

print(man)
print(other)


for i in list(man):
    print(i)
print('-------以上是男主的台词-------')
for i in list(other):
    print(i)
print('-------以上是其他人的台词-------')

# 版本1：需要用finally关闭文件
# try:
#     man_file = open("man_data.txt", "w")
#     other_file = open("other_data.txt", "w")
#     print(man, file=man_file)
#     print(other, file=other_file)
# except IOError:
#     print('File error')
# finally:
#     man_file.close()
#     other_file.close()

# 版本2：用with打开文件不需要使用finally关闭文件
# try:
#     with open('man_data.txt', 'w') as man_file:
#         man.append("这一个是测试用的")
#         print_lol(man, location=man_file)
#     with open('other_data.txt', 'w') as other_file:
#         print_lol(other, location=other_file)
# except IOError as err:
#     print('File error: ' + str(err))

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as per:
    print('Pickling error: ' + str(per))

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as per:
    print('Pickling error:' + str(per))

print("————为了证明以下代码是重新写的————")
print_lol(new_man)