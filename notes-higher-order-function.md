# Higher-order function 高阶函数

一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

       
    以Python内置的求绝对值的函数abs()为例:
    
    1.1 变量可以指向函数
    >>> abs(-10)
    10
    >>> abs
    <built-in function abs>
    可见，abs(-10)是函数调用，而abs是函数本身。
    
    要获得函数调用结果，我们可以把结果赋值给变量：
    >>> x = abs(-10)
    >>> x
    10    
    函数本身也可以赋值给变量：
    >>> f = abs
    >>> f
    <built-in function abs>
    赋值后，可以通过该变量来调用这个函数：
    >>> f = abs
    >>> f(-10)
    10    
    变量f现在已经指向了abs函数本身。    
    
    1.2 函数名也是变量
    
    函数名其实就是指向函数的变量。   
    对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数。    
    如果把abs指向其他对象：
    >>> abs = 10
    >>> abs(-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not callable
    把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数了！    
    
    1.3 传入函数
    
    既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
    
    def add(x, y, f):
        return f(x) + f(y)
        
    当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：
    x ==> -5
    y ==> 6
    f ==> abs
    f(x) + f(y) ==> abs(-5) + abs(6) ==> 11

    验证一下：
    >>> add(-5, 6, abs)
    11

    高阶函数，就是把函数当成参数传递的一种函数。
    

### 常见高阶函数

  - Map 
  - Reduce 
  - Filter 
  - Sorted 
  - Reserved  
  - Enumerate
  - Zip 
  - Apply

### Map

    map(function, iterable, ...)

    -map(function, iterable)接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的object并返回。
    -map有两个参数，第一个参数为某个函数，第二个为可迭代对象。
    -python3中map()返回的是一个object，因为map()转变成了迭代器来节约空间，返回的是可迭代对象。（python2返回列表）                                           
    -如果需要获得list返回值，可以直接用list()来转换。 
    
    例 2.1： 
    f(x) = x * x， 将这个函数作用在一个list[1,2,3,4,5,6,7,8,9]上：
    
                         f(x) = x * x
                               |
         [ 1    2    3    4    5    6    7    8    9 ]
           |    |    |    |    |    |    |    |    |             
         [ 1    4    9    16   25   36   49   64   81 ]
         
    用Python代码实现：
    >>> def f(x):
    ...     return x * x
    ...
    >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> list(r)
    [1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    map()传入的第一个参数是f，即函数对象本身。
    结果r是一个Iterator，Iterator是惰性序列，需要通过list()函数让它把整个序列都计算出来并返回一个list。               



    map可以接受多个序列，如：
    map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    [3, 7, 11, 15, 19]

    Map的主要作用是：并行！map函数和zip函数都是用来进行并行运算，迭代等。
    在多进程编程中，利用map函数开启多进程，可以大大提高程序的效率。

### Reduce
reduce(function, iterable[, initializer])
reduce()函数接收的参数和 map()类似，一个函数 f，一个list
不过参数f（x）必须有两个参数，initializer是可选的
reduce()对list的每个元素反复调用函数f，并返回最终结果值
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
reduce 使用了一个二元函数（一个接收带带两个值作为输入，进行了一些计算然后返回一个值作为输出），一个序列，和一个可选的初始化器，卓有成效地将那个列表的内容"减少"为一个单一的值，如同它的名字一样

reduce的工作过程举例 ：
"def f(x, y):
    return x + y"

调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
先计算头两个元素：f(1, 3)，结果为4；
再把结果和第3个元素计算：f(4, 5)，结果为9；
再把结果和第4个元素计算：f(9, 7)，结果为16；
再把结果和第5个元素计算：f(16, 9)，结果为25；
由于没有更多的元素了，计算结束，返回结果25。

reduce()还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100，计算：
reduce(f, [1, 3, 5, 7, 9], 100)
结果将变为125，因为第一轮计算是：计算初始值和第一个元素：f(100, 1)，结果为101。

### Filter
 filter(function or None, iterable) --> filter object  
filter通过function对iterable中的元素进行过滤，并返回一个迭代器（iterator），里面是function判断后返回True的元素
如果function传入None，则返回所有本身可以判断为True的元素
因为filter返回的是一个iterator，它是惰性计算，只有next或者list的时候，才真正开始计算过程

和map()类似，filter()也接收一个函数和一个序列。
和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

### Zip


### Apply
