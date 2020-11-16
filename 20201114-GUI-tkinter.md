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
    
    # 此时我们在标题栏、窗口随便点点，尝试拉大窗口，但是没有反应
    >>>top.bind('<ButtonPress>')
    ''
    >>>top.bind('<ButtonPress>',print)          # top.bind(事件的名称，函数)，当事件发生的时候，就会调用该函数，这里绑定了 print 
    '1398758379497print'
    >>> <ButtonPress event num=1 x=179 y=125>   # 我们点击了标题栏，没有反应
    <ButtonPress event num=1 x=159 y=82>        # 我们点击了窗口3次，调用了 print ，分别出现了右侧的信息，event，坐标系
    <ButtonPress event num=1 x=222 y=256>     
    >>>top.bind('<ButtonPress>')
    'if {"[1398758379497print %# %b %f %h...%Y %D]"=="break"} break\n' 
    # 看不懂，top.bind('<ButtonPress>') 应该与top.title() 类似，返回当前的
    
    >>>top.bind('<ButtonPress>',lambda e: print(e))
    '13987593784508<lambda>'
    >>> <ButtonPress event num=1 x=123 y=123>   
    <ButtonPress event num=1 x=134 y=35>        # 我们点击了窗口，调用了 lambda,lambda 调用了print
    <ButtonPress event num=1 x=254 y=223>     
    >>>top.bind('<ButtonPress>',lambda e: print(e.x, e.y, e.num))  # 用 e.x, e.y, e.num 把3 个fields取出来，构造了一个tuple
    >>> (147,157,1)
    (125,23,1)
    (183,134,1)
    
    
    
    
    
    
