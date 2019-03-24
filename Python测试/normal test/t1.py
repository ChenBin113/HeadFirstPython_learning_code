# s = '狗'
# print(s.isalpha())
import random
number = random.randint(1,100)

# 测试用
# print(number)

times = 3
print("本程序将随机生成1-100的整数，您将有三次机会可以猜中数字，每次猜数字之后将有提示")
while times > 0:
    temp = input("请猜程序生成数字是：")
    if temp.isdigit():
        g_num = int(temp)
        if g_num == number:
            print("You win")
            break
        elif g_num > number:
            print("输入数字比生成数大")
        else:
            print("输入数字比生成数小")
        times -= 1
    else:
        print("输入的不是数字")
    print("你还有{0}次机会".format(times))
if times == 0:
    print("You lose")