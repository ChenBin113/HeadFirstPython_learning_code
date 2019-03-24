def hano(n, a, b, c):
    '''
    这是函数文档：
    a,b,c是汉诺塔的塔，n个盘子借助b塔将a塔的盘子转移到c塔
    '''
    if n == 1:
        print(a, '->', c)
        return None
    if n == 2:
        print(a,'->', b)
        print(a,'->', c)
        print(b,'->', c)
        return None
    if n >= 3:
        # n-1个盘子，借助c塔从a塔到b塔
        hano(n-1, a, c, b)
        print(a, '->', c)
        hano(n-1, b, a, c)
print('请输入汉诺塔上的盘子数：')
# n = int(input())
n = 3
a = 'A'
b = 'B'
c = 'C'
hano(n, a, b, c)