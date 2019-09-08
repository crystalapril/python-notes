# Run Program & Command Line & Default Argument

### 1.Run Program
  - python foo.py
  - python -m foo
  
  
### 2.Run Program vs Import Module
  - import foo
  - __name__

### 3.Command Line Argument
  - sys.argv
  - python foo.py ...
  - python -m foo ...

### 4.Default Argument
  - python -m http.server PORT
  - python -m http.server # 8000
  
        4.1 python -m http.server
        
        4.1.1 http.server程序
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


    4.1.2 启动 http.server
    >>> python -m http.server
    Serving HTTP on 0.0.0.0 port 8000(http://0.0.0.0:8000/)...

    会在当前目录启动一个文件下载服务器，默认打开8000端口。
    (当前目录,例如：如果在C盘文件夹下启动，则显示C盘文件里的目录，如果是D盘文件夹里启动，则显示D盘文件里的目录)

    如果当前目录下有index.html文件，默认显示该文件的内容；如果没有，默认显示当前目录下的文件列表。
    这时，可以在浏览器中输入 http://127.0.0.1:8000 查看
    注意：windows在查看的时候，需要关闭防火墙，否则可能报错  
         为什么此处输入127.0.0.1，因为127.0.0.1是本机地址
        
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.8000.png)
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.8000-1.png)
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/d.8000-3.png)
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/d.8000-2.png)

    4.1.3 http.server的端口(port)的用处
    >>> python -m http.server 8000
    Serving HTTP on 0.0.0.0 port 8000(http://0.0.0.0:8000/)...
    这里的 8000 就是端口，也即port，port默认为8000（不输入的情况下），也可以自己定义如8080，9000，如
    >>> python -m http.server 8080
    Serving HTTP on 0.0.0.0 port 8080(http://0.0.0.0:8080/)...
    >>> python -m http.server 9000
    Serving HTTP on 0.0.0.0 port 9000(http://0.0.0.0:9000/)...
    但无论port是8000，8080，9000，在同一个目录下启动的，显示的文件目录也是一致的
    
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.8080-2.png)
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.9000-1.png)  

    那么端口的作用是什么呢？
    
        
    
    

### 5.Different Meaning
  - python -m http.server PORT
  - python -m venv ENV_DIR
