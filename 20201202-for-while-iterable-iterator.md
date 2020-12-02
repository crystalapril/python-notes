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
    
### iterable & iterator
