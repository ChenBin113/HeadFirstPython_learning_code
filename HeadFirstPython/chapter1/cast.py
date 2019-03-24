# 演员阵容
from HeadFirstPython.chapter1 import nester

cast = ["Palin",
        ["Cleese", "Idle"],
        ["Jones",
         ['Gilliam', 'Justin'], 'Chapman']]
print('——————————————')
nester.print_lol(cast)
print('——————————————')
nester.print_lol(cast, True)
print('——————————————')
nester.print_lol(cast, True, 2)