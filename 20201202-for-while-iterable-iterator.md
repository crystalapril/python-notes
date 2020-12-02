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
        
    上面for loop 等价于下面的 while 循环
    
### iterable & iterator
