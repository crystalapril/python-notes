# Files 文档操作

 - Types 文档类型
 - open & close 文档的打开及关闭
 - read & write 文档的读写
 - with statement
 - other method: seek,flush 
 - file-like object:stdin,stdout,stderr
 - 后记
 
```
之前所学到的python的各种对数据和文本的处理，都是在程序中定义，或者用input函数实时输入的
当需要输入的量太大的时候，或者需要引用外部数据的时候，input函数就不太够用
这时就需要用到文档处理，把外部文档导入进来

同时，当我们在程序运行之后，希望能够把运算结果进行保存，而不是每次都重新run一遍程序以获取结果
也需要将运算的结果存储在文档里，就是数据存储和导出的过程

因此我们有必要了解如何通过python，来实现文档的存取和读写
```
 
### Types 文档类型
    
    文档大致上分为文本文档和二进制文档
    
    二进制文档：（这个不太懂，55555，以后遇到再说，暂时先记住结论：
                所有的文档本质上都是用二进制的方式存储的，文本文档和二进制文档都是文件的展示方式，
                二进制文档展现出来的大致长这样：b'\xd6\xd0\xb9\xfa\xca\xc7\xb8\xf6\xce\xb0\xb4'
                后面不再说二进制）
    
    文本文档：txt，py这些都属于文本文档   
    
    
### open & close 文档的打开及关闭

    open 打开文档
    
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    open函数有一堆参数，用的最多的就是file，mode
    - file就是文件的路径（地址），如果是打开程序运行本文件夹的文件，直接输入名字就好  open('somefile.txt')
      如果不在本文件夹，建议把文件的路径写清楚 open(r'd:\april\somefile.txt')      
    - mode 是打开的模式，常用的有：只读模式 r ，覆盖写模式 w， 追加写模式 a ，二进制模式 b，复合模式 +

    注意：
    file文档打开后，得到的是一个file对象（file object）
    file object 包含一些属性，例如：closed ，mode， name 等，同时还具备一些方法（read,write等，将在下一节描述）
    
    e.g. 
    >>> sm = open('testfile.txt','r+')
    >>> sm.name
    'testfile.txt'
    >>> sm.mode
    'r+'
    >>> sm.closed
    False
    
    

|  mode   |     功能                            |
|---------|----------------------------------------------------------|
|    r    | 只读模式，也是默认模式，也就是说，open('somefile.txt','r') 和 open('somefile.txt') 的效果是一样的，如果文档不存在，则报错FileNotFoundError |
|    w    | 覆盖写模式，当文件存在时，open('somefile.txt','w')会覆盖掉之前的内容；当文件不存在时，创建新的文件 |
|    a    | 追加写模式，当文件存在时，open('somefile.txt','a')会在文件内容的最后接着写；当文件不存在时，创建新的文件 |
|    b    | 二进制模式，open('somefile.txt','b')以二进制的形式处理文件内容                                |
|    +    | 复合模式，跟rwab等放在一起用，如open('somefile.txt','r+')，在原功能基础上，同时增加读写功能       |
    
    
    close 关闭文档
    
    当文件读取写入完之后，建议关闭文档。
    不关闭也可以，程序退出时会自动关闭，但是用open函数打开后，文件一直处于被占用状态，消耗内存，还有文件被不小心的操作给改动的风险。
    并且，一直不关闭，电脑突然崩溃了，也可能导致之前写入的内容没有被真正存储下来，类似word没有及时保存吧
    所以，处理完文件，file.close()是个好习惯！
    
    当然，后面还有个with函数可以也帮你解决这个问题   


### read & write 文档的读写

     文件打开后，我们可以正式的进入读写的步骤    
         
     read 读取文件
     以 f = open('somefile.txt') 为例
     读取文件主要有3个方法：
     
     - read([size])  
       >>> f.read()  # read() 不加参数时，读取全部文本
       'hello\napril\nenjoy python'
       >>> f.read(3) # 加参数时，读取前size长度，此处是3个
       'hel'
       >>> f.read(2) # 连续使用read，会在上次读取内容的后面，接着读取size长度
       'lo'
     
     - readline([size])
       >>> f.readline() # 按行提取，如果不加参数，一次提取文本中的一行
       'hello\n'
       >>> f.readline(3) # 加参数时，读取前size长度，同样，如果是连续使用，将会在上次读取内容的后面开始读
       'apr'
     
     - readlines([hint])
       >>> f.readlines() # 不加参数时，读取所有行，跟read()一样取了所有内容，但是返回的是列表，并把每行作为一个列表元素
       ['hello\n', 'april\n', 'enjoy python']
       >>> f.readlines(2) # 加参数时，读取前hint行
       ！！！
       这里测试的有些失败，期待出现的结果是['hello\n','april\n']，但是run出来却是['hello\n'] 
       原因找了半天也没找到，这里先mark一下吧，以后找到原因了再来更新，5555555     
                  
       
     总结一下read的三种方法：
     - read() & readlines() 都是一次性读取全部，区别是一个返回str，另一返回list，并自动按行拆分成一个个元素
       因为是一次性读取，也很占内存，一旦内容过多，程序可能就崩溃了
     - readline() 是逐行提取，每次提取时释放出内存，所以内容大的时候用readline（）比较安全       
             
     
     write 写入文件
     以 f = open('textfile.txt','w') 为例
     写入文件主要有2个方法：
     - write(s)
     >>> f.write('hello,april\nworld\nenjoy python')  # write方法是向file写入一个字符串         
     
     - writelines(squence)
     >>> f.writelines(['hello\r\n','april\r\n','enjoy python'])
     # writelines 方法是写入一个序列，可以是list，也可以是tuple，或任何可以迭代的文本
     
     注意了，写文件并没有writeline方法，因为write就能满足写一行的需要
     
     
     
     for循环：
     
       f 和 f.readlines()等都是可迭代的
       
       readlines 方法经常跟for循环放在一起使用：
       >>> for line in f.readlines():  # 一次提取，分行处理
           ... print(line)
       就可以逐行的处理文本
       当然 read() 也可以跟for循环一起用，但是迭代的就是每个字符，而不是每行，所以基本上很少用
       
       此外呢，file也可以直接用for循环来处理：
       >>> for line in f:
           ... print(line)
       与上面的区别是，这里是逐行提取，所以这种办法更省内存
       
     既然f 和 f.readlines()等都是可迭代的，能用for循环，自然也就可以用while循环：
     

### with expression

    前面提到了 每次处理完文件之后，都建议用close()，把文件关闭
    为了避免在运行出现error导致无法关闭的情况，有时候写作：
    try:
        dosomething(file)
    finally:
        file.close()
        
    事实上，python有专门的 with 语句涵盖了上面的功能(try...except...finally:close)   
        
    >>> with open('testfile.txt') as f:
        ... dosomething(f)        
            
    运行结束之后，f被自动关闭，无需自己再写close（）
    
    看到这里，有的小伙伴有些疑惑，一眼看过去，没看出来with里面包含了close的功能啊
    而且，如果do something 这个过程，出现error怎么办，文档还能正常关闭吗
    或者with这步就出现错误了呢
    
    事实上，with语句可以启动一个叫做上下文管理器（context manager）的对象，context manager包含了两个方法：__enter__,__exit__
    object.__enter__(self)
    顾名思义，帮助进入到文档中，而 open('testfile.txt') 的返回值将会被 as 语句赋值给后面的 f
    object.__exit__(self, exc_type, exc_value, traceback)
    而exit方法，包含了close的功能，以及处理和记录exception的功能（exit后面的三个参数就是exception的信息）
    - 如果没有出现错误，正常退出，后面3个参数的值是（None,None,None） 
    - 如果出现了异常，并且exit的返回值是False，那么异常会被重新抛出(reraise)
    - 如果出现了异常，并且exit的返回值是True，那么异常会被压制（suppress），程序继续往下执行
    - 如果这组语句因为（除了异常以外的）其他任何原因退出，exit的返回值都会被忽略，程序继续往下执行   
    
    目前来说，我们暂时不需要掌握的这么详细，大致知道with里面包含了对异常的处理，以及不管遇到啥情况，都能close文档就行了 
    
    我们来test一下：
    e.g. 1.1:    
    >>> with open('a.txt') as f:
        ... print(f.read())
    >>> print('a')    
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: 'a.txt'
    a
    
    第一个例子是with语句出现错误，并没有'a.txt'这么个文件，但是其后的 print('a')还是运行成功了
    也即尽管with语句运行错误，其内部还是对该异常进行了处理，以使程序能够继续进行下一步的运行。
    
    e.g. 1.2:
    >>> with open('testfile.txt') as g:
        ... print(1/0)
    >>> print('b')
    >>> print(g.closed)
    Traceback (most recent call last):
      File "<input>", line 2, in <module>
    ZeroDivisionError: division by zero    
    b    
    True 
       
    第二个例子是下面的表达式（suite）中出现了错误，该错误同样被处理
    同时'testfile.txt'还成功的被关闭（g.closed=True）   
    
    
    具体详情可见：
    https://docs.python.org/3/reference/compound_stmts.html
    8.5 with statement
      
    
### other method: seek, flush

    seek    
    fileObject.seek(offset[, whence]) 改变文件指针的位置       
    - whence，当 whence 没有指定时，默认为文件的开头
      0 ：文件开头  1： 文件当前位置  2：文件末尾
    - offset，是相对于whence的偏移量   
    
    e.g. 2.1:
    >>> sm = open('testfile.txt','r+')
    >>> sm.read()
    'hello\napril\nenjoy python\neveryday'
    >>> sm.seek(5)   # 指针从文件的开头，向右偏移 5 个位置
    5
    >>> sm.write('test')
    4
    >>> sm.flush()   # 刷新缓存
    >>> sm.seek(0,0)  # 指针回到文件的开头
    0
    >>> sm.read()
    'hellotestril\nenjoy python\neveryday'
    >>> sm.close()
    
    
    flush
    fileObject.flush() 用来刷新缓存（也即修改的内容）
    
    很多情况下，当我们在文档操作中进行某些修改时，修改的内容被放到了缓存区
    直到文档关闭的时候，这些内容才被写进了文档
    
    如果我们想查看修改的内容，我们可以close（）文档，然后再open，read
    但是这样太麻烦。。。
    
    flush（）方法可以立刻刷新缓存，把缓存save进文档，同时清空缓存区
    这样我们就无需关闭文档来检查更新了
    
    
### File-like object:stdin,stdout,stderr

    stdin,stdout,stderr 是sys 模块中定义的三种流
    表示的是源于标准 UNIX 概念中的标准输入流，标准输出流，标准错误流
    
    因为没有接触过 UNIX，我们这里先顾名思义吧（5555555）
    重点看 标准，以及 输入，输出，错误，这几个词
    大致能猜到这个是跟 输入和输出相关的
    事实上，确实如此
    
    以 stdout 为例：
    print('hello,april') 大致等同于 sys.stdout.write(('hello,april')+'\n')
    但是 stdout 比 print 更好用，比如我们不想换行时可以只写 stdout.write('hello,april')
    
    眼尖的朋友，可能已经发现了 stdout 居然也可以用 write 方法
    没错，stdin ,stdout,stderr 事实上返回的是类文件对象（file-like object）    
    类对象可以用的方法，例如read ，readline， write这些，file-like object都可以用
    需要注意的是，sys.stdin.readline()会获取标准输入的全部内容，包括'\n'，这点有别与 input
    
    这三个流先有个大致印象，以后遇到了再琢磨   
    
    
### 后记

    file处理工具还有很多，这里只是罗列几种最常用的，其他的以后用的多的时候再补上
    
    本次笔记遗留了3个问题待处理：
    1.二进制文档
    2.readlines一次读取多行出bug的问题
    3.这里面没有涉及到file 不同处理方法之间效率差异的原理
    等找到答案了再来更新
        
    
    上面是比较浅显的认知，存在着不足，待不断修正更新
    
   
    
    
    


