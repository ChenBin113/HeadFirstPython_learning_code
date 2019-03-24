# 演员阵容
# from HeadFirstPython.chapter1 import nester
from HeadFirstPython.chapter2 import nester

cast = ["Palin",
        ["Cleese", "Idle"],
        ["Jones",
         ['Gilliam', 'Justin'], 'Chapman']]
print('第一次测试')
nester.print_lol(cast)
print('第二次测试')
nester.print_lol(cast, True)
print('第三次测试')
nester.print_lol(cast, True, 2)