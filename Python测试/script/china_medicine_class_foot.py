# 自己做观看手机端慕课用
import os
from time import sleep
from random import randint
repeat_times = 60


def tap_screen(x, y):
    os.system("adb shell input tap {} {}".format(x, y))


if __name__ == "__main__":
    for i in range(repeat_times):
        tap_screen(2050, y=220)
        print(i)
        sleep(randint(25, 35))