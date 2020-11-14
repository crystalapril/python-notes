# cmd command

### assoc & ftype

    assoc 命令 
    查看文件后缀名为例如 .py 的默认文件类型
    eg. 
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

### echo

    echo 回声
    shell 中的命令，常见于 linux，现在 windows 里也可以在 cmd 里使用
    eg. 
    >>>echo 'hello'
    'hello'
    
    echo %PATH%  返回 windows 系统环境变量的 path
    echo %OS%    返回 windows 的操作系统名称
    
    
    
    
    
    
