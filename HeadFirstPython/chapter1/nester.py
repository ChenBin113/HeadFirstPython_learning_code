"""
这个“nest.py”模块，提供了一个名为print_lol()的函数，
这个函数的作用是打印列表，其中有可能包含嵌套列表。
"""
def print_lol(the_list, indent=False, level=0):
    """
    这个函数取一个位置参数，名为“the_list”，
    这可以是任何Python列表。
    列表内每一个数据项会输出到屏幕上，各数据各占一行。
    indent:第一层列表是否缩进
    level:给不同层列表加上缩进，显示更加清晰。
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent==1:
               for tab_stop in range(level):
                    print("\t", end='') #每一层缩进显示一个Tab制表符
            print(each_item)