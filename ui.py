import tkinter as tk
import windnd
from tkinter.messagebox import showinfo
import os

from remark import add_comment

def on_window_configure(event):
    if event.widget == window:
        # 窗口大小发生变化时执行的操作
        frame_width = event.width / 2  # 设置frame宽度为窗口宽度的一半
        frame_height = event.height / 2  # 设置frame高度为窗口高度的一半
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=frame_width, height=frame_height)

def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    entry1.delete(0, tk.END)
    entry1.insert(tk.END, msg)

def on_button_click():
    input_text1 = entry1.get()  # 获取第一个输入框的文本内容
    input_text2 = entry2.get()  # 获取第二个输入框的文本内容
    msg = ""
    msg = add_comment(input_text1, input_text2)
    warning_label.config(text=msg)

# 创建主窗口
window = tk.Tk()
window.title("Remark")
# window.iconbitmap("icon.ico")

# 设置窗口的初始大小
window_width = 300
window_height = 180
window.geometry(f"{window_width}x{window_height}")

# 创建一个容器框架，用于将组件居中
frame = tk.Frame(window)

# 绑定窗口的"<Configure>"事件，当窗口大小发生变化时调用on_window_configure函数
window.bind("<Configure>", on_window_configure)

# 使用pack()方法将组件放置于窗口中心
frame.pack(expand=True)

# 创建第一个输入框
entry1 = tk.Entry(frame)
entry1.insert(tk.END, "将文件夹拖放到此处")
entry1.pack(expand=True, fill=tk.X)

# 创建第二个输入框
entry2 = tk.Entry(frame)
entry2.pack(expand=True, fill=tk.X)

# 创建确定按钮
button = tk.Button(frame, text="确定", command=on_button_click)
button.pack()

# 创建警告提示标签
warning_label = tk.Label(frame, text="", fg="red")
warning_label.pack()

# 绑定拖放事件
windnd.hook_dropfiles(window , func=dragged_files)

# 进入主循环
window.mainloop()
