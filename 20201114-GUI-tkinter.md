# GUI-tkinter

    GUI:  Graphical User Interface 图形用户界面

### Tkinter

    Tkinter 是python 自带的一个 gui 模块，比较古老了
    我们通过Tkinter 来了解一下诸如Tkinter，wxPython, QT 这类 GUI 的一个基本模式
    
    1.tk.Tk(), title(), bind(), <ButtonPress>
    
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
    
    # top.bind('<ButtonPress>',lambda e: print(e)) 就是在 <ButtonPress> 发生的时候，会调用后面的 lambda函数
    >>>top.bind('<ButtonPress>',lambda e: print(e))  
    '13987593784508<lambda>'
    >>> <ButtonPress event num=1 x=123 y=123>   #  <ButtonPress> 就是点击
    <ButtonPress event num=1 x=134 y=35>        # 我们点击了窗口，调用了 lambda,lambda 调用了print
    <ButtonPress event num=1 x=254 y=223>      
    >>>top.bind('<ButtonPress>',lambda e: print(e.x, e.y, e.num))  # 用 e.x, e.y, e.num 把3 个fields取出来，构造了一个tuple
    >>> (147,157,1)  
    (125,23,1)
    (183,134,1)    
    >>>top.bind('<ButtonPress>',lambda e: top.title('tk %d %d %d' % (1,2,3))) # title 名称修改成了 'tk 1 2 3'
    >>>top.bind('<ButtonPress>',lambda e: top.title('tk %d %d %d' % (e.x, e.y, e.num))) # title 名称随着点击窗口而变化 'tk 123 34 1'
    
    
    2. mainloop
    
    eg.
    tk1.py
    import tkinter as tk
    top = tk.Tk()    
    def on_ButtonPress(e):
      new_title = 'tk %d %d %d' % (e.num, e.x, e.y)
      top.title(new_title)
    top.bind('<ButtonPress>', on_ButtonPress)    
    我们在 cmd 里 py tk1.py ，发现闪退，我们猜测是不是因为程序运行结束了，就关闭程序，同时也关闭了 tk 窗口
    
    我们进入py交互模式，验证一下想法
    >>>import tkinter as tk
    >>>top = tk.Tk()    # 弹出窗口
    >>>import sys
    >>>sys.exit()       # python 退出，同时 tk 窗口也关闭了
    
    想要观察 tk1.py 的运行，可以用 input 设置阻塞
    但是 input 的缺点很明显，首先会弹出 py的运行窗口黑色框框，其次要 enter 才会消失，多此一举
    
    tkinter 提供了mainloop() 来解决这个问题，既不会弹出黑框，又不需要按 enter
    mainloop() 是一个会阻塞的函数，阻塞到窗口的关闭按钮被点击为止
    
    我们在py 交互式里 ，观察一下
    >>>import tkinter as tk
    >>>top = tk.Tk()    # 弹出窗口
    >>>top.mainloop()   # 这句输入完后，交互式的提示符 caret >>> 一直没有出现
    >>>                 # 关闭 tk 窗口，>>> 提示符出现了
    # 也即，top.mainloop() 运行后，一直没有执行完，所以提示符>>> 没有出现，一直到 tk 窗口关闭
      关闭后，top.mainloop()  执行完了，提示符 >>> 出现了
      
    tk1.py  # 修改后，增加 mainloop
    import tkinter as tk
    top = tk.Tk()    
    def on_ButtonPress(e):
      new_title = 'tk %d %d %d' % (e.num, e.x, e.y)
      top.title(new_title)
    top.bind('<ButtonPress>', on_ButtonPress)    
    top.mainloop()    
    
    
    3. pyw 
    
    我们在 cmd 里执行
    >assoc .pyw
    .pyw=Python.NoConFile
    >ftype Python.NoConFile
    Python.NoConFile="C:\WINDOWS\pyw.exe"  "%L" %*
    pyw 是 python no console file 的意思
    >pyw tk1.py    # 程序顺利运行，弹框成功，同时cmd的 提示符也出现了
    
    我们把 tk1.py 的后缀改成 tk1.pyw ，然后直接双击
    发现程序直接运行，且没有黑框了
    
    py 就是python， w 就是 windows
    py.exe 启动的时候，有个标记位，告诉windows ，启动的时候开个黑框
    pyw.exe 没有这个标记，启动的时候，就没有黑框
    
    
    4. 
    eg.         # 用 tkinter 创建一个时钟 
    clock.py
    import tkinter as tk
    import datetime
    top = tk.Tk()
    time = datetime.datetime.now   # 这里之所以拆分 time 和 strftime 是因为，一旦now()被调用了，就是一个数字，不再能时时更新
    def button(e):
        top.title(time().strftime('%Y-%m-%d %H:%M:%S'))    # 要把 time 作为函数传入button，点击的时候再调用
    top = tk.Tk()
    top.title(time().strftime('%Y-%m-%d %H:%M:%S'))   # 启动的时候，直接在 title 里显示时间
    top.bind('<ButtonPress>',button)
    top.mainloop()
    # top.title() 传递给 title的 参数，不管是整数还是说时间，会默默被转成 str
      >>>top.title(10)       
      >>>top.title()
      '10'
    
    这个并没有实现时钟的功能，需要点一下，才能更新时间，没有时钟是酱紫的，所以我们做了改进，让clock自动更新时间       
    
    clock.py   # 修改后，自动更新时间
    import tkinter as tk
    import datetime
    top = tk.Tk()
    def update_time():
        output['text'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        top.after(1000, update_time）
    output = tk.Label(top)
    output.pack()
    top.after(1000, update_time)
    top.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
