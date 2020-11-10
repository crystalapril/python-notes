# python_launcher-regedit

### python_launcher

    python launcher 就是在 windows上可以直接运行python的程序
    python launcher 可帮助我们选择，和执行不同版本的Python解释器（比如是选择执行py3.7，还是py3.9）
    
    之前我们在cmd里面输入命令行
    python file.py
    py file.py
    都是运行python程序的一种方式
    
    其实还有另一种方式，可以运行python程序：
    点击右键，将要任意文件拖动到要运行的文件上去，我们以 argv_pause.py 为例
    import sys
    print(sys.argv)
    input('press enter to continue')
    
    拖动 md5_sha1.py 到  argv_pause.py 上去
    会看到 ['argv_pause.py','argv_pause.py']
    注意，如果没有input的话，程序运行结束，会飞快的退出，在肉眼看起来就是闪退
    所以暂时用了笨办法，input进行阻塞，让我们看到程序运行的情况


### regedit
