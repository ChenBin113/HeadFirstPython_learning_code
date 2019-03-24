# 玩玩而已
import os
from time import sleep


def tap_screen(x, y):
    os.system('adb shell input tap {} {}'.format(x, y))


def do_money_work():
    print('#0 start the game')
    tap_screen(1660, 868)
    sleep(30)

    # print('#1 ready, go!!!')
    # tap_screen(1450, 910)
    # sleep(15)

    # print('#2 auto power on!')
    # tap_screen(500, 500)

    for i in range(25):
        tap_screen(1000, 500)
        sleep(1)

    print('#3 do it again...\n')
    tap_screen(1900, 988)
    sleep(3)


if __name__ == '__main__':
    for i in range(80):
        print('round #{}'.format(i + 1))
        do_money_work()
