import tkinter as tk
from tkinter import ttk

class applacation():
    def helpQuit(self):
        print('Quit')
        self.helpRoot.destroy()
        self.root.mainloop()

    def send(self, key=None):
        if self.mainSendText.get() != '':
            self.mainDialog.configure(state=tk.NORMAL)
            self.mainSendText.delete(tk.END, tk.END)
            self.mainDialog.insert(tk.END, '我：' + self.mainSendText.get() + '\n')
            self.mainSendText.delete(0, tk.END)
            self.mainDialog.configure(state=tk.DISABLED)

    def help(self):
        self.helpRoot = tk.Tk()
        self.helpRoot.title('帮助')
        self.helpRoot.geometry('300x120')
        self.helpText = tk.Text(self.helpRoot, width=35, height=5, font=('宋体', 12))
        self.helpText.insert(1.0, "算数题：打出”算术题“，加空格，再写要计算算式\n讲笑话：输入“讲笑话”\n退出：打出“quit”\n打出“节日快乐”会有惊喜")
        self.helpText.configure(state=tk.DISABLED)
        self.helpText.pack()
        self.helpButton = ttk.Button(self.helpRoot, text='知道了', command=self.helpQuit)
        self.helpButton.pack()
        self.helpRoot.mainloop()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tiri —— 您的人工智障问答软件')
        self.root.geometry('600x400')

        # 标题
        tk.Label(self.root, text='Tiri', font=('宋体', 30)).pack()
        tk.Label(self.root, text='您的人工智障问答软件 V1.0.4 I', font=('宋体', 12)).pack()

        # mainFrame
        self.mainFrame = tk.LabelFrame(self.root, text='输入框')

        # mainDialog
        self.mainDialogFrame = tk.Frame(self.mainFrame)
        self.mainDialogFrame.pack()

        self.mainScrollbar = ttk.Scrollbar(self.mainDialogFrame)
        self.mainScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.mainDialog = tk.Text(self.mainDialogFrame, yscrollcommand=self.mainScrollbar.set,
                                  width=58, height=10, font=('宋体', 12))
        self.mainDialog.pack()
        self.mainScrollbar.config(command=self.mainDialog.yview)
        self.mainDialog.configure(state=tk.DISABLED)

        # mainSend
        self.mainSendFrame = tk.Frame(self.mainFrame)
        self.mainSendFrame.pack()

        self.mainSendText = ttk.Entry(self.mainSendFrame, width=49, font=('宋体', 12))
        self.mainSendText.pack(side=tk.LEFT)
        self.mainSendText.bind("<Return>", self.send)

        self.mainSendButton = ttk.Button(self.mainSendFrame, text='发送', command=self.send)
        self.mainSendButton.pack(side=tk.RIGHT)

        # mainFrame pack
        self.mainFrame.pack()

        # 帮助按钮
        self.helpButton = ttk.Button(self.root, text='帮助', command=self.help)
        self.helpButton.pack()

        # mainloop
        self.root.mainloop()


if __name__ == '__main__':
    app = applacation()
