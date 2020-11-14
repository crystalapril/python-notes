# explorer-pid-environment

### explorer.exe

    explorer.exe 又叫 File Explorer，又叫文件夹管理
    一般来说，桌面上的内容，打开文件的窗口，窗口的内容都归 explorer.exe 来管
    
    我们打开任务管理器验证一下，win+R: taskmgr 
    点击表头，按名称排序，找到了explorer.exe ，发现 pid（process id） 号为 6024
    点击结束任务，电脑蓝屏（win10垃圾，win xp的话会再开一个 explorer.exe）
    再次调用 taskmgr，发现各程序依旧在运行
    也就是，explorer.exe 负责绘制屏幕，包括壁纸以及桌面图标等
    explorer.exe 关掉之后，桌面的屏幕就没有了，但是电脑其实还在运行
    
### pid

    process id 进程id
    
### environment

    windows environment
    主要是指定 windows 系统运行中的一些参数
    主要分为用户的环境变量，系统的环境变量两大类，其中分别包含：
    用户环境变量：path, temp, test, tmp 等 
    系统环境变量：path, os, pathext, username, windir 等等
    以上都属于环境变量的范围，不仅仅是 path
    windows path 由一系列的路径构成
    系统运行一个程序而没有告诉它程序所在的完整路径时，系统除了在当前目录下面寻找此程序外，还可以到path中指定的路径去找
    这也是为什么，我们在安装python 的时候，需要把python.exe 的路径添加到环境变量里，否则可能无法直接通过 cmd 运行
    
    一般来说，系统搜索环境变量的顺序是，从左到右，从上到下
    如果有安装一个程序的不同版本，左边的，上面的会被优先搜到，被默认执行
    
    修改用户的环境变量，可以直接通过搜索栏进入
    修改系统的环境变量，需要管理员权限，得通过计算机属性来进入
    
    安装 python launcher 的时候，发现 py.exe 的路径在用户和系统的环境变量path里都没有找到
    py.exe 一般安装在 C:\WINDOWS 下面，而 C:\WINDOWS 有时候被显示为 %SYSTEMROOT% , 因此在cmd 里启动 py 能直接运行
    
    
    environment regedit
    
    除了上述在计算机属性里进入环境变量的界面，修改参数以外
    还可以通过 regedit 来修改
    win + R : regedit 
    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment
    进入上面地址的 environment ，与系统环境变量对比，发现变量和值均一一对应
    同时，修改增删 regedit 的参数和值，系统环境变量界面也相应的有了变化，反之亦然
    
    HKEY_CURRENT_USER\Environment
    进入上面地址的 environment，与用户环境变量对比，发现变量和值均一一对应
    同上面一样，修改 regedit 的参数和值，用户环境变量也相应的变动，反之亦然
    
    
    
    
    
    
    
    
    

