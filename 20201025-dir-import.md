# dir & import

### dir
    
    dir()，返回一个列表
    不带参数的时候，列表的item 是当前范围内的属性、方法；
    带参数时，list 里面的 item 该参数的属性、方法等
    
    eg.1
    >>> dir()
    ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'hashlib', 'sys']    
    
    
    dir(sys)
    ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__',     '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding',     
    ......此处省略......    
    'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
    
    我们可以看到 dir() 返回的 list 里面，有很多 双下划线'__'打头的方法，属性等，单下划线'_'打头的，以及普通函数、方法
    通常来说，我们自己创立的 module 里的的函数，通常是普通表示的，非'__', '_'
    


### import

    import 的几种方法已经比较熟悉了
    
    这里插一句特殊的
    
    如果要通过命令行来选择需要 import的 module 怎么办，可以直接 import sys.argv[1] 吗
    答案是否定的
    
    import module
    后面的 module 后面的字面上是什么，就会import 什么，没有就会报错，import 后面的语句不会进行运算
    
    eg.2
    正确： import math  
    
          argv = ['test.py','math]
    错误： import argv[1]  
    
    那么如果想要通过命令行来指定要 import的 module，怎么办
    这里，我们引入 __import__() 函数
    
    eg.3
    >>> import sys
    >>> module = __import__(sys.argv[1])   # 就顺利的 import 需要的 module 了
    
    如果要进一步调用函数，可以用 getattr
    >>> getattr(module, sys.argv[2])()
       
    或者如下面示范的那样，用 dir() 来提取出需要的函数： 
    
    eg.4
    
    >>> import sys

    >>> module = __import__(sys.argv[1])

    >>> def candidate(name):
            return not name.startswith('__')

    >>> for name in filter(candidate,dir(module)):
            try:
                getattr(module,name)()
            except:
                pass
    
    

