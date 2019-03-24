# 非常差的代码
number = 1
while number:
    if number % 2 == 1:
        if number % 3 == 2:
            if number % 5 == 4:
                if number % 6 == 5:
                    if number % 7 == 0:
                        print(number)
                        break
                    else:
                        number += 1
                else:
                    number += 1

            else:
                number += 1

        else:
            number += 1



    else:
        number += 1


print("*"*50)
x = 0
while x < 1000:
    if (x % 2 == 1) \
            and (x % 3 == 2) \
            and (x % 5 == 4) \
            and (x % 6 == 5) \
            and (x % 7 == 0):
        print(x)
        x += 1
        # break
    else:
        x += 1

print("循环结束")