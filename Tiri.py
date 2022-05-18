import tkinter as tk


class applacation():
    def send(self, key=None):
        if key is None:
            if self.mainSendEntry.get() != '':
                self.mainDialog.configure(state=tk.NORMAL)
                self.mainDialog.insert(tk.END, '我：' + self.mainSendEntry.get() + '\n')
                self.mainSendEntry.delete(0, 'end')
                self.mainDialog.configure(state=tk.DISABLED)
                return
        if key.char == '·':
            if self.mainSendEntry.get() != '':
                self.mainDialog.configure(state=tk.NORMAL)
                self.mainDialog.insert(tk.END, '我：' + self.mainSendEntry.get() + '\n')
                self.mainSendEntry.delete(-1, tk.END)
                self.mainDialog.configure(state=tk.DISABLED)

    def help(self):
        self.helpRoot = tk.Tk()
        self.helpRoot.title('帮助')
        tk.Label(self.helpRoot,
                 text="算数题：打出”算术题“，加空格，再写要计算算式，符号与数字要用空格。幂用mi代替，这样写：6 mi 2。\n讲笑话：输入“讲笑话”\n退出：打出“quit”\n打出“节日快乐”会有惊喜").pack()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tiri —— 您的人工智障问答软件')
        self.root.geometry('600x400')

        # 标题
        tk.Label(self.root, text='Tiri', font=('宋体', 30)).pack()
        tk.Label(self.root, text='您的人工智障问答软件 V1.0.10040', font=('宋体', 12)).pack()

        # mainFrame
        self.mainFrame = tk.LabelFrame(self.root, text='输入框')

        # mainDialog
        self.mainDialogFrame = tk.Frame(self.mainFrame)
        self.mainDialogFrame.pack()

        self.mainScrollbar = tk.Scrollbar(self.mainDialogFrame)
        self.mainScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.mainDialog = tk.Text(self.mainDialogFrame, yscrollcommand=self.mainScrollbar.set,
                                  width=58, height=10, font=('宋体', 12))
        self.mainDialog.pack()
        self.mainScrollbar.config(command=self.mainDialog.yview)
        self.mainDialog.configure(state=tk.DISABLED)

        # mainSend
        self.mainSendFrame = tk.Frame(self.mainFrame)
        self.mainSendFrame.pack()

        self.mainSendEntry = tk.Entry(self.mainSendFrame, width=49, font=('宋体', 12))
        self.mainSendEntry.pack(side=tk.LEFT)
        self.mainSendEntry.bind("<Key>", self.send)

        self.mainSendButton = tk.Button(self.mainSendFrame, text='发送', width=10, font=('宋体', 12), command=self.send)
        self.mainSendButton.pack(side=tk.RIGHT)

        # mainFrame pack
        self.mainFrame.pack()

        # 帮助按钮
        self.helpButton = tk.Button(self.root, text='帮助', width=10, font=('宋体', 12), command=self.help)
        self.helpButton.pack()

        # mainloop
        self.root.mainloop()


if __name__ == '__main__':
    app = applacation()
