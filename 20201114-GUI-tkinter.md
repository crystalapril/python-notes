# GUI-tkinter

    GUI:  Graphical User Interface 图形用户界面

### Tkinter

    Tkinter 是python 自带的一个 gui 模块，比较古老了
    我们通过Tkinter 来了解一下诸如Tkinter，wxPython, QT 这类 GUI 的一个基本模式
    
    cmd里 py进入交互模式
    >>>import tkinter as tk
    # tk.Tk()创建了顶层的窗口，并赋值给了top，
    >>>top = tk.Tk()            # 此时弹出了白框，标题为 tk
    # top.title() 返回当前标题
    >>>top.title()             
    'tk'
    # top.title(new) 可以设置新标题
    >>>top.title('hello')       # 此时白框的标题，由 tk 变成了 hello
    >>>top.title()
    'hello'
    >>>top.title('world')       # 此时白框的标题，由 tk 变成了 world
    >>>top.title()
    'world'
    
    
    
    
    
    
    
