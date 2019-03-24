import os  # 实际上可以不用前两行
os.chdir(r'F:\1【Python】编码项目\HeadFirstPython\chapter3')

data = open('sketch3.txt')
for each_line in data:
    try:
        # find方法如果没有找到会返回-1
        # 原数据有(pause)等，因此增加这个逻辑判断
        if not each_line.find(':') == -1:
            # 通过指定分隔符对字符串进行切片，
            # 如果参数 num 有指定值，
            # 则分隔 num+1 个子字符串
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
    except:
        print('*'*10)
data.close()
