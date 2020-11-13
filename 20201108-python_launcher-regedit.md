# python_launcher-regedit

### python launcher

    python launcher 就是在 windows上可以直接运行python的程序
    python launcher 可帮助我们定位和执行不同版本的 Python 解释器
    python launcher 最开始主要是为了解决手动指定到底是运行 py2.7 还是 py3 的问题
    简单来说就是，手动的方式是 py2 a.py  或者 py3 a.py
    而在 a.py 里面加上 #！python2 或者 #！python3 ，然后直接用 py a.py，就可以用指定的 python 版本来运行，这就是 python launcher 的主要工作
    
    python launcher 有 2 个版本
    一个是 python.exe ，又叫 控制台程序
    一个是 pythonw.exe ，这个主要是为 windows 准备，主要是 gui 方面的应用
    
    控制台程序被命名为 py.exe，其实 py.exe 运行之后，会启动 python.exe ，就实际上还是 python.exe 来干活
    而windows程序则命名为 pyw.exe ，并且 pyw.exe 将定位并执行 pythonw.exe    
 
 
### methods of run python program
    
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
    这里的 argv获取了 2个文件的地址，第一个是被运行的 .py 文件的地址，第二个是被拖动的文件的地址，可能是 .py, .txt 都可以
    注意，如果没有input的话，程序运行结束，会飞快的退出，在肉眼看起来就是闪退
    所以暂时用了笨办法，input进行阻塞，让我们看到程序运行的情况 
 
    那么这个运行方式，有什么实际意义吗
    我们回顾之前写的 md5_sha1.py ，当我们想要运行该程序，计算 md5 ,sha1 是否正确时，需要输入的变量太多了
    python long_address1/md5_sha1.py e:/pycharm-community-2020.2.3.exe AAABF0920C868E3D99F74361C277624CB15148F7  # sha1
    这么一长串输入，其实是有些不方便的
    如果我们能通过改进程序，让需要被计算的文件，直接拖到 py 上，并且 同时能传入参数 md5,sha1 运行时就会方便很多了    
    
    于是，我们 在 md5_sha1.py 的基础上，新建 sha.py 对程序进行3个方面的改动：
    1. 通过 pyperclip 来获取要被校验的 md5 / sha1 码
    2. 在 sha1.py 对 file的 md5 / sha1 进行计算，并与 pypeyclip 获得的进行比对，print 比对的结果
    3. open() 在处理大文件的时候，可能会有问题，解决掉 open() 与大文件兼容的问题
    
    我们首先对前两个问题进行了处理
    sha.py 如下：
    import sys,pyperclip,hashlib
    # get sha code from outside
    whole = pyperclip.paste()
    whole_split = whole.split(' ')
    sha_paste = whole_split[1].strip().lower()
    # calculate sha code of file
    addr = sys.argv[1]
    file = open(addr + '.txt', 'rb')
    data = file.read()
    sha = hashlib.sha1(data)
    sha_calcu = sha.hexdigest().lower()
    # compare
    addr_split = addr.split('\\')
    print(addr_split[-1]+' sha1'+ ':'+ sha_calcu)
    print(sha_calcu)
    print(True) if sha_paste == sha_calcu else print(False)  
    

### regedit
