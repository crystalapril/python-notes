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

    windows

