# Run Program & Command Line & Default Argument

### 1 Run Program
  - python foo.py
  - python -m foo
  
        python foo.py 和 python -m foo 
        
        是加载py文件的两种方式：
        python foo.py  叫做直接运行
        python -m foo  相当于import,叫做当做模块来启动
               -m mod : run library module as a script (terminates option list)
        
        不同的加载py文件的方式，主要是影响sys.path这个属性：
        python foo.py 直接运行是把run.py文件，所在的目录放到了sys.path属性中
        python -m foo 模块启动是把你输入命令的目录（也就是当前路径），放到了sys.path属性中
  
  
### 2 Run Program vs Import Module
  - import foo
  - '__name__'
  
        __name__是python的一个内置类属性:
        如果当前模块是主模块（也就是调用其他模块的模块），那么此模块名字就是__main__
        如果此模块是被import的，则此模块名字为文件名字（不加后面的.py）
       
        因为：
        对于__name__来说，python -m foo 和 python foo.bar 是一类，import foo 是另一类
        对于__name__来说，python -m foo 和 python foo.py 都是作为程序（主模块）运行，import foo 是作为模块导入
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/name_a.png)


### 3 Command Line Argument
  - sys.argv
  - python foo.py ...
  - python -m foo ...

### 4 Default Argument
  - python -m http.server PORT
  - python -m http.server # 8000
  
### 4.1 http.server程序        

    python -m http.server看起来不像是在运行一个python程序，但事实上，http.server是一个python程序
    我们进入python交互模式：
    >>> import http.server
    >>> http.server

    可以看到出现了一个路径(path)，把前后的单引号也一起复制然后
    >>> print('C:\\Users\\april\\AppData\\Local\\Programs\\Python\\Python37\\lib\\http\\server.py')
    'C:\Users\april\AppData\Local\Programs\Python\Python37\lib\http\server.py'
    （\\ 变成1个\了）

    >>> python C:\Users\april\AppData\Local\Programs\Python\Python37\lib\http\server.py
    得到的执行结果和
    >>> python -m http.server
    执行的效果是一样的，因此，python -m http.server也是在运行一个python程序
        
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/http.server.png)

### 4.2 启动 http.server
    
    >>> python -m http.server
    Serving HTTP on 0.0.0.0 port 8000(http://0.0.0.0:8000/)...

    会在当前目录启动一个文件下载服务器，默认打开8000端口。    

    如果当前目录下有index.html文件，默认显示该文件的内容；如果没有，默认显示当前目录下的文件列表。
    这时，可以在浏览器中输入 http://127.0.0.1:8000 查看
    注意：    
    - windows在查看的时候，需要关闭防火墙，否则可能报错  
    - 为什么此处输入127.0.0.1，因为127.0.0.1是本机地址
    - 当前目录,例如：如果在C盘文件夹下启动，则显示C盘文件里的目录，如果是D盘文件夹里启动，则显示D盘文件里的目录
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.8000.png)
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.8000-1.png)

### 4.3 http.server的端口(port)的用处    

    >>> python -m http.server 8000
    Serving HTTP on 0.0.0.0 port 8000(http://0.0.0.0:8000/)...
    这里的 8000 就是端口，也即port，port默认为8000（不输入的情况下），也可以自己定义如8080，9000，如
    
    >>> python -m http.server 8080
    Serving HTTP on 0.0.0.0 port 8080(http://0.0.0.0:8080/)...
    前往http://127.0.0.1:8080 查看:
    得到跟上面8000端口显示同样的文件目录
   
    >>> python -m http.server 9000
    Serving HTTP on 0.0.0.0 port 9000(http://0.0.0.0:9000/)...
    前往http://127.0.0.1:9000 查看:
    得到跟上面8000端口显示同样的文件目录

    因此，无论port是8000，8080，9000，在同一个目录下启动的，显示的文件目录也是一致的
    注意：这里浏览器地址隐藏了 http  

    那么端口的作用是什么呢？   
    我们在电脑的 cmd 里运行 ipconfig
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/ipconfig.png)      
    
    WLAN下面的 IPv4 地址：192.168.0.110
    >>> python -m http.server
    让手机跟电脑连上同一个wifi,然后用手机里的浏览器去访问，http://192.168.0.110:8000
    显示出了D盘文件夹下的目录

    对于手机和电脑来说，192.168.0.110都是电脑的地址，这个地址不是固定的，一般用ipconfig先查询一下
    继续在电脑端执行
    >>> python -m http.server 9000
    然后在手机浏览器里访问，http://192.168.0.110:9000
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/iphone.c.jpg) 

    现在运行了两个http.server
    其中一个是列出D盘的内容，另一个是列出C:\User\april 的内容
    
    那么对于访问的人来说，需要一个东西来区别
    是打算访问 D: ，还是打算访问 C:\User\april呢
    端口号，8000 9000 就是区分
    cmd里显示，手机的地址是192.168.0.101
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/iphone-address.png) 

    也即，地址是用来区分不同机器的
    在这里，192.168.0.110是电脑，192.168.0.101是手机
    
    但是电脑里可能会运行不止一个http.server
    因此就要有另一个东西来区分某一个机器里的不同的http.server，这个东西就叫做端口号
    
    大多数时候，端口号都是用来区分“不同类型”的服务的
    只是因为现在举例只运行了 http.server 这一个程序
    
    类似mysql，mysql其实也是可以在一个机器上运行，然后在另一个机器上去访问的
    假设一个机器，它有一个地址，但是这个机器上可以同时运行mysql和http.server
    
    地址只能区分机器
    区分不同的“服务”需要另一个东西,这个就是端口号    
    
    mysql也可以像刚刚http.server那样执行多个
    就需要端口号来区分， 是想访问哪一个服务:某个http.server，还是某个mysql，或其他
    
### 4.4 端口的规则

    一般来说0-1023以下的端口号为管理员使用，1024以上的“随意”分配
    
    用管理员模式启动cmd，进入到了C:\WINDOWS\system32 这个目录下
    切换到D盘的根目录下，然后
    >>> python -m http.server 80
    Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/)...
    
    在电脑访问：  http://127.0.0.1:80
    在手机里访问：http://192.168.0.110:80
    执行出现了D盘的目录，并且地址栏隐藏了 80
    
    再在电脑里访问 ： http://127.0.0.1
    在手机里访问：  http://192.168.0.110   （不带80）
    出现了同样的，D盘的文件目录
    
    也即，对于python -m http.server如果没有写端口号，http.server默认就用 8000
    
    对于http这种协议（protocol）来说，它的默认端口是80
    http://127.0.0.1:80 = http://127.0.0.1  ，http://192.168.0.110 = http://192.168.0.110
    
    现在出现了两个默认端口号，一个是http协议的80，一个是http.server的8000
    也有其他类似 http.server的程序，就不一定是用8000作为默认端口了，一般也不会用80
    
    为什么一般程序不会用80这个端口号呢？
    
    在类unix的系统（几乎除了windows以外的所有系统）中，比如linux，0-1023之间的端口必须要有管理员权限才能使用
    
    因此，为了兼顾系统规定，大部分程序不会使用1023以下的号码作为端口号    
    比如在linux中，python -m http.server 80 就会报错（permission denied）
    另外有一些比较“聪明”的程序，会根据使用者是不是管理员来分配端口号：
    是管理员给分配1024以下的端口号，不是管理员也没有提供端口号就选择1024以上的
    
    以ubuntu为例：
    安装ubuntu：
    1、在开始菜单的右边输入栏搜索power
    2、选择windows powershell
    3、输入 Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    4、重启，在放大镜的输入栏里搜索 store
    5、找到 ubuntu 18.04，点击获取
    6、安装成功了，自定义username，password
    
    检测端口规则：
    >>> python3 -m http.server
    打开浏览器 127.0.0.1 ，可以访问
    
    >>> sudo python3 -m http.server 80
    打开浏览器 127.0.0.1 ，也可以访问
    （sudo就是将这条命令以管理员权限执行）
    
    以busybox这个程序（是一个不给端口号就可以使用80的程序）为例来测试：
    >>> busybox httpd -f
    permission denied
    （没有用sudo，因此不是以管理员权限来执行，被拒绝访问）
    >>> sudo busybox httpd -f
    没有报错
    （浏览器访问127.0.0.1，出现404，因为busybox只有下载的功能，没有列出目录的功能。但是因为加了sudo没有被拒绝访问）
    
    

### 5 Different Meaning
  - python -m http.server PORT
  - python -m venv ENV_DIR
  
        不同的程序可以对命令行参数有不同的理解
        
        对于python来说命令行参数就只是一个字符串的数组而已    
        
        对于python -m http.server 8000命令来说，是http.server它把'8000'这个字符串解释为数字了，并用作端口号
        
        例如：
        >>> python -m pip --version
        pip 19.1.1 from C:\Users\april\AppData\Local\Programs\Python\Python37\lib\site-packages...
        
        >>> python -m venv --version
        venv: error: the following arguments are required: ENV_DIR              
        (错误：需要ENV_DIR这个参数)
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/venv1.png) 
        
        >>> python -m venv A
        >>> python -m venv B   

        这时观察D盘，发现生成了A文件夹和B文件夹

    我们发现：
    - venv 这个程序，把传递给它的参数，当作目录名字来用了
    - http.server和venv对命令行的理解是不一样的
    - http.server 的参数是控制它的端口号，但这是因为这个命令行参数是被http.server来使用和理解的
    - 其他程序并不一定也是理解为端口号，参数在命令行中的意义，是每个程序自己定义的
   



        
        
        
        
        
        
        
