# for & while, iterable & iterator

### for & while

    for 循环的内在运行机制其实是while 循环的改写
    
    for variable... in expression:
        statement
        ...   
        
    == transform to ==>
    
    iterable = expression
    iterator = iter(iterable)
    try:
        while True:
            variable... = next(iterator)
            statement
            ...
    except StopIteration:
        pass
        
    上面for loop 的内部运行，实际上是下面的一整套 while 循环
    
    当 for in 语句，收到一个 表达式 expression 之后
    首先，对这个表达式用 iter() 函数，将该表达式，转换成 iterator
    然后再放到 while 循环下
    通过 next() 获取 variable
    一直到 iterator 取完，抛出 StopIteration
    用 try...except...语句接住
    
    那么有的同学可能会问了，如果 expression 本身就是 iterator 怎么办
    for 循环还会对其进行 iter()吗， iter(iterator) 会得到什么
    带着这个疑问，我们来看 2 个例子
    eg.1
    >>>next([1])  # [1] 是 list，list 是 iterable 
    TypeError: 'list' object is not an iterator  # 这句说明，next() 只能对 iterator 用，不能对 iterable 用
    eg.2
    for x in sorted(xs):
        statement
    把上面的 for 循环转换成 while 循环：
    i = iter(sorted(xs))   # 这里的 for 循环时没有 iter()的，转换成 while 里面就有一个 iter()
    try:
        while True:
            next(i)
    except StopIteration:
        pass
        
    当 expression 本来就有 iter()的时候, for转换还是会加一个 iter
    因为 for 循环不知道 expression 是不是 iterator，不能智能识别
    为了以防万一，都加上一个 iter()
    而 iter(iterator) == iterator
    
    eg.3
    for data in iter(lambda:file.read(1024),b''):
        statement
    转换后：
    iterator = iter(iter(lambda:fire.read(1024),b''))   # 被套了2个 iter()
    
    那么为什么 iter(iterator) 也要是 iterator 呢
    我们来看这2个例子：
    map(str,[1,2,3])， 返回一个 iterator
    sorted([1,2,3])， 返回一个 list
        
    for 要支持
    for x in sorted([1,2,3]):
        statement
    for 要调用 iter(sorted[1,2,3]) 来获得一个 iterator，然后 next()
    如果没有这个 iter，sorted([1,2,3]) 得到的 list 是没有办法用 next()的       
        
    而 for 又要支持
    for x in map(str,[1,2,3]):
        statement
    但是 for 没有那么智能，会根据 in 后面的结果来调整，它只能死板的调用 iter()
    所以上面的代码，也会经历 iter(map(str,[1,2,3])) 来获得一个 iterator
    
    
### iterable & iterator


