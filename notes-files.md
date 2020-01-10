# Files 文档操作

 - Types 文档类型
 - open & close 文档的打开及关闭
 - read & write 文档的读写
 - with function
 
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
       >>> f.readlines() # 不加参数时，读取所有行，跟read（）一样，但是返回的是列表
       ['hello\n', 'april\n', 'enjoy python']
       >>> f.readlines(2) # 加参数时，读取前hint行
       
       
     
     write 写入文件
     写入文件主要有2个方法：
     write([size])
     writelines()
     

### with function


