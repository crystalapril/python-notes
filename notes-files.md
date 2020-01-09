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
    - mode 是打开的模式，常用的有只读模式 r，覆盖写模式 w，追加写模式 b，复合模式 +

|  mode   |     功能                            |
|---------|----------------------------------------------------------|
|    r    | 只读模式，也是默认模式，如果文档不存在，则报错FileNotFoundError |
|    w    |                                 |
|    a    |                                 |
|    b    |                                 |
|    +    |                                 |
    
    
    close 关闭文档
    


### read & write 文档的读写


### with function
