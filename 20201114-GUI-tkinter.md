# GUI-tkinter

    GUI:  Graphical User Interface 图形用户界面

### Tkinter

    Tkinter （Tk interface）是python 自带的一个 gui 模块，比较古老了
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
    
    
    4. tkinter 在 命令行运行 和 交互式运行的区别
    
    我们以模拟时钟的 gui 为例
    eg.         # 用 tkinter 创建一个时钟 
    clock1.py
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
    那么如何让 时钟自动更新，并且一直不停，我们想到了while True，并且用sleep函数来每秒停顿一下
    
    clock2.py
    import tkinter as tk
    import datetime
    top = tk.Tk()
    print('before')
    while True:
        top.title(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))    
        time.sleep(1)
    print('after')
    top.mainloop()
    运行之后，发现黑框里有‘before’出现，但是时钟没有白框，也就是 tk 的窗口
    
    我们进入py 交互式逐行查看究竟
    >>>import tkinter as tk
    >>>import datetime
    >>>top = tk.Tk()    # 弹出白框
    >>>top.title(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   # title修改为时间
    >>>top.title(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   # 时间更新
    
    由此看出，交互式与 py clock2.py，运行的情况大不相同
    
    clock_consumer.py
    import tkinter as tk
    from datetime import datetime
    top = tk.Tk()
    n = 0
    while True:
      input(str(n))
      n += 1
      top.title(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
      
    我们在 cmd里 
    >py  clock_consumer.py
    一开始，弹出窗口，title是 tk，窗口有反应（可以拖动大小）
    在 cmd里敲回车，窗口的标题变成了当前时间，窗口依然有反应（可以拖动大小）
    继续敲回车，依然会更新时间，窗口依然有反应
    
    我们再进入交互式
    >>>import tkinter as tk
    >>>import time
    >>>top = tk.Tk()   # 弹出白框
    >>>time.sleep(5)   # 停顿了5秒
    
    >>>import tkinter as tk
    >>>import time
    >>>top = tk.Tk();time.sleep(5)   
    # 预期：白框框出现，然后等待5秒，提示符出现
    # 结果：白框没有立刻出现，等待5秒后，提示符重新出现的同时，白框框才出现
    
    >>>import tkinter as tk
    >>>import time
    >>>top = tk.Tk();print('before');time.sleep(5);print('after')
    # 白框没有立刻出现，'before'先出现，等待5秒后，'after'出现后，白框出现了
    
    >>>import tkinter as tk
    >>>import time
    >>>top = tk.Tk();top.update();print('before');time.sleep(5);print('after')   # 注意，新增了 update()
    # 白框立刻出现，随后'before'，等待5秒，'after'
    
    事实上，python给 tkinter 开了后门
    在交互模式里，py 把命令执行完之后，等待下一条输入之前，它会悄悄的执行 top.update() 或类似的机制
    >>>top = tk.Tk() 
    >>>                     # 交互模式执行完了，它就悄悄的update，所以马上就看到白框了
    
    >>>top.title('world');print('before');sleep(5);print('after')
    # 会先出来 'before'，然后停顿5秒，然后 'after', 然后 title 变成 'world'
    >>>top.title('hello');top.update();sleep(3)
    # title 立刻变成 'hello',然后停顿3秒，出现下一个提示符
    
    因此，clock2.py里因为没有进入交互式，也没有 update 这样的机制，就卡住了
    >>>sleep(10)  # 拉动tk 窗口但是没有反应
    
    clock1.py里，我们做了一个点击之后就更新时间的程序
    python的代码里面，处理了点击这个事件
    但是，无论是拖动窗口，还是调整窗口大小，clock1.py里面，没有写相应的处理这些的代码
    那么，总有一个地方需要处理这样的事件，类似处理鼠标拖动窗口大小
    如果python 在 sleep，就没有机会去调用那些代码
    update 就是去调用那些代码
    例如，我们在交互式里
    >>>top.bind('<Button-1>',print)   # 点击窗口，交互式里会输出
    >>>top.sleep(5)      # 点击窗口，就没反应了
    
    那么，根据我们观察和测试的情况，我们对 clock进行改进
    clock3.py
    import tkinter as tk
    import datetime
    top = tk.Tk()
    print('before')
    while True:
        top.update()
        top.title(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))    
        time.sleep(1)
    print('after')
    top.mainloop()
    
    改完之后运行，能自动更新时间了，窗口也可以拖动了，但是有点慢    
    我们接着对 clock 进行改进，引入 after
        
    
    5. after()
    
    clock4.py   # after
    import tkinter as tk
    import datetime
    top = tk.Tk()
    def update_time():
        top.title(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  
        top.after(1000, update_time）
    top.after(1000, update_time)
    top.mainloop()
    
    top.after(ms,f) 就是在 ms 毫秒后执行函数 f
    但是，after不会让窗口卡住
    运行后，时间自动更新了，窗口也不卡，可以自由拖动
    
    
    6. Label
    
    进入 python 交互模式
    >>>import tkinter as tk
    >>>top = tk.Tk()    #弹出白框
    >>>output = tk.Label(top)   
    >>>output.pack()     # 白框变小了
    >>>output['text'] = 'hello'     # 白框的窗口处正中间出现了 'hello'
    >>>output['text'] = 'world'     # 'hello' 的正下方出现了 'world'
    
    也就是说，创建一个 Label ，然后pack， 然后设置它的 text ，就可以控制窗口显示的内容了
    那么，我们把 clock改一改，让时间显示在窗口，而不是标题栏
    
    clock5.py   # Label, pack, text
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
    
    运行成功，终于变成一个在窗口出自动更新的时钟了
    
    我们再观察一下 Label ,pack 的顺序
    >>>import tkinter as tk
    >>>top = tk.Tk()     # 弹出白框
    >>>a=tk.Label(top)
    >>>a['text']='hello'
    >>>a.pack()          # 窗口出现了 'hello'
    >>>b=tk.Label(top)
    >>>b['text']='world'
    >>>b.pack()          # 'hello'的正下方出现了 'world'
    >>>c=tk.Label(top)
    >>>c['text']= 'python'   
    >>>c.pack()          # 'world' 的正下方出现了 'python'
    
    开一个新的python 交互式，调换 pack的顺序
    >>>import tkinter as tk
    >>>top = tk.Tk()     # 弹出白框
    >>>a=tk.Label(top)
    >>>a['text']='hello'
    >>>b=tk.Label(top)
    >>>b['text']='world'
    >>>c=tk.Label(top)
    >>>c['text']= 'python'   
    >>>c.pack()          # 窗口出现了 'python'
    >>>a.pack()          # 'python'的正下方出现了 'hello'
    >>>b.pack()          # 'hello'的正下方出现了 'world'
    所以只有 pack() 调用的时候，窗口才会发生变化
    
    开一个新的python 交互式, 加入 sleep
    >>>import tkinter as tk
    >>>from time import sleep
    >>>top = tk.Tk()     # 弹出白框
    >>>a=tk.Label(top)
    >>>a['text']='hello'
    >>>b=tk.Label(top)
    >>>b['text']='world'
    >>>c=tk.Label(top)
    >>>c['text']= 'python'   
    >>>c.pack()          
    >>>a.pack()          
    >>>b.pack()          
    >>>print('before')
    >>>sleep(5)
    >>>print('after')
    先出现 'before', sleep 5s, 'after',然后 'python','hello','world'
    
    开一个新的python 交互式, 加入 update
    >>>import tkinter as tk
    >>>from time import sleep
    >>>top = tk.Tk()     # 弹出白框
    >>>a=tk.Label(top)
    >>>a['text']='hello'
    >>>b=tk.Label(top)
    >>>b['text']='world'
    >>>c=tk.Label(top)
    >>>c['text']= 'python'   
    >>>c.pack()          
    >>>a.pack()          
    >>>b.pack()     
    >>>top.update()
    >>>print('before')
    >>>sleep(5)
    >>>print('after')
    先出现 'python','hello','world' 然后'before', sleep 5s, 'after'
    
    开一个新的python 交互式,调换顺序
    >>>import tkinter as tk
    >>>from time import sleep
    >>>top = tk.Tk()     # 弹出白框
    >>>a=tk.Label(top)
    >>>a['text']='hello'
    >>>b=tk.Label(top)
    >>>b['text']='world'
    >>>c=tk.Label(top)
    >>>c['text']= 'python'         
    >>>a.pack()          
    >>>b.pack()    
    >>>top.update()
    >>>print('before')
    >>>sleep(5)
    >>>print('after')
    >>>c.pack()  
    先出现 'hello','world' 然后'before', sleep 5s, 'after'，'python'
    
    
    7. tk.LEFT  tk.TOP  tk.RIGHT
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
