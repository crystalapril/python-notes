# Higher-order function 高阶函数

一个函数就可以接收另一个函数作为参数，或者接受另一个函数作为返回值，这种函数就称之为高阶函数。

       
    以Python内置的求绝对值的函数abs()为例，解释接收函数作为参数:
    
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

    高阶函数，可以把函数当成参数传递的一种函数。
    

### 常见高阶函数

  - Map 
  - Reduce 
  - Filter 
  - Sorted 
  - Reserved  
  - return to a function(返回函数，英文名不确定)  
  - Enumerate
  - Zip 
  - Apply
  - closure
  - decorator
  

### Map

    map(function, iterable, ...)

    -map()接收一个函数f 和一个sequence，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的object并返回。
    -map有两个参数，第一个参数为某个函数，第二个为可迭代对象。
    -python3中map()返回的是一个object，因为map()转变成了迭代器来节约空间，返回的是可迭代对象。（python2返回列表）                                           
    -如果需要获得list返回值，可以直接用list()来转换。 
    
    例 2.1： 
    f(x) = x * x， 将这个函数作用在一个list1[1,2,3,4,5,6,7,8,9]上：
    
                         f(x) = x * x
                               |
         [ 1    2    3    4    5    6    7    8    9 ]
           |    |    |    |    |    |    |    |    |             
         [ 1    4    9    16   25   36   49   64   81 ]
         
    用map函数实现：
    >>> def f1(x):
    ...     return x * x
    ...
    >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> list(r)
    [1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    map()传入的第一个参数是f，即函数对象本身。
    结果r是一个Iterator，Iterator是惰性序列，需要通过list()函数让它把整个序列都计算出来并返回一个list。     
    
    如果用普通函数，使用for循环实现：
    >>> def f2(f1,x):
            l=[]
            for i in x:
                l.append(f1(x))    # l.append(x*x)
            return l
    >>> list1 = [1,2,3,4,5,6,7,8,9]
    >>> f(f1,list1)
    [1, 4, 9, 16, 25, 36, 49, 64, 81]
    对比上下两个函数，可以发现map()的内部原理：
    ▪ map()实际上是传导入两个参数，一个f，一个序列
    ▪ map()在内部新建一个[]（python2），对序列内的每一个x，进行运算，将运算结果依次添加到新建的list中去。
      (python3返回的是iterator，不是list)
    ▪ 因此map()作为高阶函数，只用了一行代码,对上述运算过程进行了抽象。    

    -map还可以接受多个序列，如：
    >>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    [3, 7, 11, 15, 19]

    -Map的主要作用是：并行！map函数和zip函数都是用来进行并行运算，迭代等。
    -在多进程编程中，利用map函数开启多进程，可以大大提高程序的效率。


### Reduce
       
    reduce(function, iterable[, initializer])
       
    -reduce()函数接收一个函数 f 和一个sequence。
    -对序列的每个元素依次调用函数f，并把每次运算结果和序列的下一个元素做累积计算，返回最终结果。    
    
    reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)    
    
    -参数f（x）必须接收两个参数，initializer是可选的。   

    例 3.1：
    >>> from functools import reduce
    >>> def f1(x, y):
    ...     return x * 10 + y
    ...
    >>> reduce(f1, [1, 3, 5, 7, 9])
    13579    
    
    -调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
    ▪ 先计算头两个元素：f(1, 3)，结果为 1*10+3=13；
    ▪ 再把结果和第3个元素计算：f(13, 5)，结果为 13*10+5=135；
    ▪ 再把结果和第4个元素计算：f(135, 7)，结果为 135*10+7=1357；
    ▪ 再把结果和第5个元素计算：f(1357, 9)，结果为 1357*10+9=13579；
    
    reduce使用了一个二元函数，一个序列，和一个可选的初始化器，将列表的内容"减少"为一个单一的值，如同它的名字一样。
    （这个二元函数，接收两个值作为输入，进行了一些计算，然后返回一个值作为输出。）

    -用普通函数，使用for循环实现上面的运算过错，例3.2：
    >>> def f2(f1,x):            
            a = x[0]
            for b in x[1:]:
                a = f(a,b)     # a = a*10+b
                #a *= 10   
                #a += i     
            return a
    >>> list2 = [1, 3, 5, 7, 9]
    >>> f2(f1,list2)
    13579
    
    -当reduce()接收可选参数作为计算的初始值时，例 3.3：
    >>> reduce(f, [1, 3, 5, 7, 9], 100)
    10013579
    此时reduce()第一轮计算是：计算初始值和第一个元素：f(100, 1)，结果为 100*10+1=1001，往后以此类推。
    而普通函数的写法中，初始值a不再是0，而是 a = 100。    
        
    -对比上下两个函数，可以发现reduce()函数的内部原理：
    ▪ 实际上是传导入一个f，一个序列。
    ▪ 当给定可选参数作为初始值时，初始值被作为第一个运算对象(a=100)，没有给定初始值时，默认序列的第一个值x[0]为初始运算对象。
    ▪ 随后，对序列内的每一个b，进行运算f(a,b)，运算结果返回给值a，直至结束。
    ▪ 因此，reduce()本质是一个accumulator（累加器）(eg. *=,+=,-=)
    
    -reduce()多数情况下，返回一个值，有时也可以返回一个序列。
    #例 3.4 : 构造 reverse 函数
    rlist2=reduce(lambda x,y:[y]+x,rlist,[])
    
    -reduce()函数也可以和map()函数搭配使用：
    >>> def fn(x, y):
    ...     return x * 10 + y    
    >>> def char2num(s):
    ...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    ...     return digits[s]
    >>> reduce(fn, map(char2num, '13579'))
    13579            
                

### Filter

    filter(function or None, iterable) --> filter object  
    
    -filter()函数用于过滤序列，接收一个函数 f 和一个序列。
    -filter()把传入的f依次作用于每个元素x，仅保留f(x)判断为True的元素，返回一个iterator。

    #例 4.1: 在一个list中，删掉偶数，只保留奇数
    >>> def is_odd(n):
            return n % 2 == 1
    >>> list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
    [1, 5, 9, 15]

    使用普通函数，for循环来实现上述运算，例 4.2：
    >>> list3 = [1, 2, 4, 5, 6, 9, 10, 15]
    >>> def f2(f1,xs):
           l = []
           for x in xs:
              if f1(x) == True:     # if x % 2 == 1:
                  l.append(x)
           return l
    >>> f2(is_odd,list3)
    
    对比上下两个函数，可以发现filter()的内部原理：
    ▪ filter()传导入两个参数，一个f，一个序列。
    ▪ filter()内部新建一个[]（python2），对序列内的每一个x，进行bool判断，将判断为True的元素依次添加到新建的[]中去，最后返回list。
    (python3返回的是iterator，不是list)    
    
    注意事项：
    -如果function传入None，则返回所有本身可以判断为True的元素
    -filter返回的是一个iterator，它是惰性计算，只有next或者list的时候，才真正开始计算过程。

    -filter()与map()的比较：
    ▪ 相同点：map()和filter()均接收一个函数和一个序列，经过运算后，返回一个迭代器（iterator）。
    ▪ 不同点：map()对xs中的元素x进行运算，返回运算后的以f(x)为元素的序列，元素个数不变，len(xs)=len(map(f1,xs))；
             filter()不对xs中的元素进行改变，只进行筛选，通常元素会减少，len(xs)>=len(filter(f2,xs))。


### Sorted




### Zip


### Apply
