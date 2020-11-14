# explorer-pid-environment-registry

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
    
### registry

    上面我们提到了regedit，是 registry editor 的缩写
    现在我们说说 registry 注册表
    
    registry 是windows里 hierarchical 的数据库
    类似文件系统，分层的，最顶层有几个，然后可以展开，可以有目录，也可以有文件 的一个数据库
    windows 提供了一套函数（C语言的）去操作这个数据库，增删改查
    https://docs.python.org/3/library/winreg.html
    python 有个模块，可以使用 windows 提供的这套函数
    
    而之前我们见过的 regedit 也是一个windows 自带的程序，可以对 registry 进行增删改查的工具
    regedit 不是注册表本身，主要不要混淆，是一个程序
    registry 注册表，是一个数据库
    
    windows 自带的 reg.exe 是个命令行程序，也可以修改 registry，但是没有 regedit.exe 直观
    （类似于 software office 和 wps office 程序都可以运行 .word 文档一样）
    
    而我们常用的修改环境变量的工具，其实也是一个操纵注册表的程序，对，是程序！
    但是 regedit 是通用的
    修改环境变量的程序是带有目的，只对注册表中环境变量的部分做出特别的处理
    通过这个程序修改环境变量，和通过 regedit 修改环境变量是操作的同一个数据库 registry 里的同一个部分
    所以才会有上面的，一边修改了，另一边就看见了
    
    我们通过 cmd 读取环境变量里的数据时，例如：
    echo %PATH%
    echo %OS%
    echo %TMP%
    cmd 在启动的时候，会去读取注册表里的 
    HKEY_CURRENT_USER\Environment
    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment
    然后根据他们的内容，计算出环境变量，然后让这个cmd 进程的环境变量设置为这个
    这个工作，也可能是 explorer.exe 做的
    环境变量严格来说，是进程的属性
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

