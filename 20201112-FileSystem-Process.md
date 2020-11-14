#  File system & Process

### File system

    
### process & pid

    进程 process
    我们每开一个程序，就启动一个进程 process
    pid，是 process id 的缩写，也即进程id
    
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
    
    由此得知：
    双击启动： explorer.exe ----> py.exe
    cmd 启动： explorer.exe ----> cmd.exe ---->py.exe
