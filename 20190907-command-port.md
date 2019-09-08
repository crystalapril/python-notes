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

        会在当前目录启动一个文件下载服务器，默认打开8000端口。

        如果当前目录下有index.html文件，默认显示该文件的内容；如果没有，默认显示当前目录下的文件列表。
        
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/c.8000.png)
![image](https://github.com/crystalapril/python-notes-april/master/image/c.8000-1.png)
        
    
    

### 5.Different Meaning
  - python -m http.server PORT
  - python -m venv ENV_DIR
