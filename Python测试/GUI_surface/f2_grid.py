# [https://blog.csdn.net/qq_40925239/article/details/88618199]
import tkinter as tk
import tkinter.messagebox as mbox


# 定义MainUI类表示应用/窗口，继承Frame类
class MainUI(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        # 创建控件
        self.create_widgets()

    # 创建控件
    def create_widgets(self):
        # 创建一个标签，输出要显示的内容
        self.first_label = tk.Label(self, text="人生苦短，我用Python")
        # 设定使用grid布局
        self.first_label.grid()
        # 创建一个按钮，用来出发answer方法
        self.click_button = tk.Button(self, text="不知道要按下还是退出", command=self.answer)
        # 设定使用grid布局
        self.click_button.grid()


    def answer(self):
        # 我们通过messagebox来显示一个提示框
        mbox.showinfo("都是广告", "你不信就进来看看")


# 创建一个MainUI对象
app = MainUI()
# 设置窗口标题
app.master.title('Python')
# 设置窗体大小
app.master.geometry('400x400+100+100')
# 主循环开始
app.mainloop()

