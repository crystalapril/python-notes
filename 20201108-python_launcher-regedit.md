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
    
    之前我们在cmd里面输入命令行 （或者把 file.py 拖到命令行中）
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
    我们回顾之前写的 md5_sha1.py ，当我们想要运行该程序，计算 md5 ,sha1 是否正确时，需要输入的变量太多了，很不方便
    python long_address1/md5_sha1.py e:/pycharm-community-2020.2.3.exe AAABF0920C868E3D99F74361C277624CB15148F7  # sha1
    
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
    input('press enter to continue')
    
    通过 copy 已有的 sha1 码，然后拖动要计算的如 empty.txt 文件，到 sha.py文件，结果发现闪退了
    由于正常运行的文件没有出现闪退的情况，于是我们写一个小的程序验证一下，用 try...except... ,用 sys.exc_info() 捕获错误
    通过简单的 0/0 这样的错误进行试验，发现确实报错会导致闪退。
    
    于是我们对sha.py 进行测试，通过 控制变量法 找出报错的代码，用 sys.exc_info() 捕获错误
    发现错误是因为没有 pyperclip 模块造成的
    于是观察了运行窗口，发现运行的程序是 c:\windows\python.exe，这个原生的 python 没有安装 pyperclip 包的
    我们进入了有安装 pyperclip 的 stuff_venv 试试看
    通过把要运行的.py 文件 copy到 stuff_venv 目录下，拖动要运行的文件 sha.py, 发现成功解决了该问题，没有报错
    那么自然，在原生的 python 里，直接安装 pyperclip 应该也能解决这个问题，我们不再做尝试
    
    上述方法虽然能解决问题，但是不方便，需要把要运行的文件，copy 到 虚拟环境的目录下才行
    因此，我们尝试第三个方法，修改 regedit
      

### regedit

    我们可以通过 windows 的 regedit 来运行上面的 sha.py
    
    regedit 是 windows 里的一个程序，是 registry editor 的缩写，可以用来修改注册表（一种数据库） 
    除了 regedit.exe 以外，windows 里还自带了 reg.exe （是一个命令行程序）也可以用来修改注册表
    （有点类似于 word 文档，microsoft office 和 wps office 都可以修改 word文档）    
    
    用 regegit 来运行 py程序的步骤：
    1. win + R 打开运行命令，输入 regedit 调出 注册表编辑器
    2. 找到 HKEY_CURRENT_USER\Software\Classes
    3. 点开 classes 下面的 * ，发现没有 shell， 点击右键添加 (item)项 shell
    4. 右键点击 shell ，新建 项，名为 pydemo
    5. 点击 pydemo, 新建项 command
    6. 点击 command，双击右侧的 默认，填写数据，假设 notepad
    7. 回到文件夹，右键点击文件，弹出上下文菜单，里面出现了 pydemo，点击，弹出了记事本
    8. 回到 regedit，修改 pydemo的command 默认值为 py C:\idea\argv_pause.py
    9. 回到文件夹，右键点击文件例如 empty.txt，弹出上下文菜单，点击pydemo，发现运行了 argv_pause.py
    10. 修改 pydemo 的默认值为 py C:\idea\argv_pause.py %1
    11. 回到文件夹，右键点击文件 empty.txt，发现 argv 里捕获到了 被点击文件的地址 ['C:\idea\argv_pause.py','C:\idea\empty.txt']
    12. 修改 pydemo 的默认值为 D:\python\stuff_venv\scripts\python.exe C:\idea\clip_test.py %1 ，让虚拟环境里的 python 来作为执行程序
    13. 回到文件夹，右键点击文件 empty.txt，成功运行，虚拟环境里安装的 pyperclip 也 import 成功
    
    14. 我们接着尝试用 pydemo，来打开 white space.txt，出现闪退
    在上一轮修改中，sha.py 已经有了try...except 和 sys.exc_info()，依旧没有抓住错误，猜测在except 语句下，可能再次发生错误
    由于 empty.txt 没有报错，我们猜测报错可能跟 white space.txt 的名字有空格有关系
    通过 控制变量法 ，发现 file = open(addr + '.txt', 'rb') 报错
    原因是通过 regedit 运行py的方式，传入 sys.argv 的时候，把 white space.txt 没有作为一个整体传入
    py argv.py a b，得到的 sys.argv 是 ['argv.py','a','b']
    py argv.py "a b" ，得到的 sys.argv 是 ['argv.py','a b']  # 注意这里命令行的输入必须是 双引号
    
    为了解决这个问题，我们修改 regedit 的 pydemo 的默认值为 D:\python\stuff_venv\scripts\python.exe C:\idea\clip_test.py "%1"        
    点击文件，假设叫 A， 弹出上下文菜单，新增的名字就是 注册表里 \shell 下面的那个比如 pydemo
    然后点击 pydemo 执行的命令就是 command 里的默认值
    如果在这个命令里需要使用最开始的文件 A ，就用 %1 来表示 A （batch的时候也遇到过）
    "%A" 来防止 A中的空格在传递中不被分割
    
    15. 修改完之后，右键点击 white space.txt，运行成功
    
    tips：我们在编程的时候，要尽量避免文件名中有空格，防止中间环节出现问题
          但是在自己编程的时候，同时要考虑到用户可能会使用 有空格的文件名，要提前把这样的问题处理好
          
    继续对程序进行修改，使用input来进行阻塞防止闪退，在程序里面有点难看，而且多余
    同时 try...except...也还是会漏掉错误，于是继续修改 regedit
    16. 把 command 的默认值改为 cmd /c D:\python\stuff_venv\scripts\python.exe C:\idea\clip_test.py "%1" & pause
    17. 右键点击 empty.txt ，点击 pydemo，运行成功，但是由于input，需要多按一次
    18. 删除掉 sha.py 的 input，再试，发现没有闪退，只按一次 enter就能退出程序
    19. 删除掉 sha.py 里面的 try...except，然后试着写错一个地方，再用pydemo 运行，发现像常规的 cmd一样报错
    
          
   
    
    
    
    
    
    
    
    
    
    
    
    
