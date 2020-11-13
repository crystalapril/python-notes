# python_launcher-regedit

### python_launcher

    python launcher 就是在 windows上可以直接运行python的程序
    python launcher 可帮助我们定位和执行不同版本的 Python 解释器
    python launcher 最开始主要是为了解决 py2.7 和 py3 不兼容的问题，因为现在主要都是用python3 以上了，所以不对这个问题有过多的解释了
    
    python launcher 有 2 个版本
    一个是 python.exe ，又叫 控制台程序
    一个是 pythonw.exe ，这个主要是为 windows 准备，主要是 gui 方面的应用
    
    控制台程序被命名为 py.exe
    而windows程序则命名为 pyw.exe ，并且 pyw.exe 将定位并执行 pythonw.exe
    
    
    之前我们在cmd里面输入命令行
    python file.py
    py file.py
    都是运行python程序的一种方式
    
    其实还有两种方式，可以运行python程序：
    一种是直接 双击 .py 或 .pyw 文件
    一种是点击右键，将要任意文件拖动到要运行的文件上去，我们以 argv_pause.py 为例
    import sys
    print(sys.argv)
    input('press enter to continue')
    
    拖动 md5_sha1.py 到  argv_pause.py 上去
    会看到 ['argv_pause.py','md5_sha1.py']
    这里的 argv获取了 2个文件的地址，第一个 item 是被运行的程序的地址，第二个 item 是被拖动的程序的地址
    注意，如果没有input的话，程序运行结束，会飞快的退出，在肉眼看起来就是闪退
    所以暂时用了笨办法，input进行阻塞，让我们看到程序运行的情况 
 
    那么这个运行方式，有什么实际意义吗
    我们回顾之前写的 md5_sha1.py ，当我们想要运行该程序，计算 md5 ,sha1 是否正确时，需要输入的变量太多了
    python long_address1/md5_sha1.py e:/pycharm-community-2020.2.3.exe AAABF0920C868E3D99F74361C277624CB15148F7  # sha1
    这么一长串输入，其实是有些不方便的
    如果我们能通过改进程序，让需要被计算的文件，直接拖到 py 上，并且 同时能传入参数 md5,sha1 运行时就会方便很多了
    
    
    于是，我们 在 md5_sha1.py 的基础上，新建sha_draw.py 对程序进行3个方面的改动：
    1. 让

    



### regedit
