#  File system & Process

### File system 文件系统

    文件系统提供在存储介质（磁盘，固态硬盘等）上组织数据的一种方式方法
    
    简单来说，一个块硬盘，跟bytes 有点类似，是一个字节一个字节的
    如果直接指定硬盘，第1000-3000个字节存放 hello.txt，第3000-6000字节存放 world.py 就有点乱
    文件系统就是在硬盘这种储存上构造一种层次化的组织
    包括文件、文件名、内容，以及修改日期，是否只读等等
    也包含目录，目录里可能包含更多的文件、子目录，也有修改日期、是否只读这些
    这样才能使用 C:\\Windows\py.exe 这样的东西来表示一个文件
    硬盘是不知道文件名、文件属性这些的 
    硬盘的语言就是，“在第1000个字节开始记录这500个字节”
    
    文件系统就是这么一个东西
    用户告诉文件系统：“列出C:\ 这个目录下有哪些文件”
    文件系统将这个语言（文件、目录。。。）翻译成硬盘知道的语言
    它思考了一下，然后告诉硬盘
    “第500字节开始给我800字节”
    “第2000字节开始给我200字节”
    “第2200字节开始给我300字节”
    问了硬盘，然后自己计算了一下，然后回答用户 “C:\ 这个目录下有这些文件”
    文件系统有点类似于图书管理员，硬盘就是图书馆书架    
    
    程序（program）就是file system 上个一个文件（file）
    比如 argv.py  这个是文件名
    import sys
    print(sys.argv)
    是文件的内容
    argv.py 这个文件还有一些元数据，例如 修改日期，是否只读 
    右键点一个文件，点属性，就能看到 创建日期，修改日期，最后访问日期，是否只读，是否隐藏 这些
    它们不是文件的内容，把文件丢到 pycharm 里，pycharm 也不会显示修改日期这些
    但是它们又确实是文件的一部分
    你修改了文件，那么文件的修改日期就会变化
    把文件设置成 只读，pycharm 就不让你保存了
    
    目录也有名字、内容，其他的元数据
    目录内容里，也有子文件，子目录
    目录也包含创建日期，修改日期，最后访问日期，是否只读，是否隐藏 这些 
    目录里增加删除了文件，目录的修改日期就会变
    把目录的只读勾上，目录就不能增加删除文件了
    
    让用户可以以文件目录的形式来记录数据，就是由文件系统完成的
    平时习以为常的文件目录的功能，都是靠着文件系统的默默付出
    
### process & pid

    进程 process
    我们每开一个程序，就启动一个进程 process
    一个程序可以启动多次产生多个 process，或者一次都不启动，就没有对应的 process
    pid，是 process id 的缩写，也即进程id
    
    我们启动一个程序，这个结果是产生了一个新的进程，又叫子进程 child process
    那么，这个动作，是由谁启动，谁执行的呢      
    
    我们通过修改 environ.py，来观察进程的特点
    import os
    for k in os.environ:
      if k.startswith('TEST'):
        print((k, os.environ[k]))
    input('press enter to exit')
    
    在老的 cmd 里 
    >>>set TEST_ENV=hello
    >>>echo %TEST_ENV%
    hello
    >>>py environ.py
    ('TEST_ENV','hello')
    
    我们打开任务管理器，win + R： taskmgr
    点击名称，按名称排序，看到2个cmd.exe，一个pid=15216， 另一个pid=13276
    一个py.exe,pid=12088
    
    我们在新的 cmd 里执行
    >>>wmic process where "(processid=12088)" get processid,parentprocessid,executablepath
    ExecutablePath      ParentProcessId    ProcessId
    C:\WINDOWS\py.exe   15216              12088
    也即，py.exe 的id是12088，爸爸的id是 15216
    
    关掉新的 cmd，现在进程里只剩一个 cmd.exe，pid 是 15216
    再打开一个新的 cmd, 进程里出现了新的 cmd.exe,pid = 13340,在新的cmd里执行：
    >>>wmic process where "(processid=15216)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\WINDOWS\system32\cmd.exe   7256               15216    
    
    >>>wmic process where "(processid=7256)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\WINDOWS\Explorer.EXE       7208               7256     
    可以看到 explorer.exe 是爷爷，启动了 cmd.exe (爸爸)，cmd.exe 启动了 py.exe (孙子)
    
    关掉旧的 cmd 里启动的py.exe
    双击 environ.py,在任务管理器里找 py.exe 的pid，发现是 13992    
    >>>wmic process where "(processid=13992)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\WINDOWS\Explorer.EXE       7256               13992     
   
    
    我们进入py 的交互模式
    >>>import os
    >>>os.getpid()
    8236
    >>>os.getppid()   # parent process id
    10564
    
    打开任务管理器 win+R: taskmgr
    点击表头，按名称排序，win7系统需要自己添加 pid 列
    看到 pid 8236 对应的python.exe, ppid 10564 对应的是 py.exe
    (注意，python.exe 的父进程是 py.exe，py.exe是通过python.exe 来干活的，自己不干活 )
    
    再打开一个cmd
    >>>wmic process where "(processid=8236)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\...\python38\python.exe    10564              8236   
    >>>wmic process where "(processid=10564)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\WINDOWS\py.exe             6184               10564   
    >>>wmic process where "(processid=6184)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\WINDOWS\system32\cmd.exe   3396               6184   
    >>>wmic process where "(processid=3396)" get processid,parentprocessid,executablepath
    ExecutablePath                ParentProcessId    ProcessId
    C:\WINDOWS\Explorer.EXE       3360               3396  
   
      
    由此得知：
    双击启动： explorer.exe ----> py.exe
    cmd 启动： explorer.exe ----> cmd.exe ---->py.exe
    交互式：   explorer.exe ----> cmd.exe ---->py.exe ----> python.exe
    

    
    
