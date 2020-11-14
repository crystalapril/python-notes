# cmd command

### assoc & ftype

    assoc 命令 
    查看文件后缀名为例如 .py 的默认文件类型
    eg.1  
    >>>assoc .py
    .py=Python.File   # 将.py文件 归为一组，相关联成 名称Python.File 的一类
    
    >>>assoc .txt
    .txt=txtfile
    
    
    ftype 命令
    查看文件类型为例如 Python.File  的默认执行程序
    >>>ftype Python.File
    Python.File="C:\WINDOWS\py.exe" "%L" %*
    # %* ---命令执行传入的参数
    
    >>>ftype txtfile
    txtfile=%SystemRoot%\system32\NOTEPAD.EXE %1
    # %1 ---被命令打开的文件名

    
    
    
