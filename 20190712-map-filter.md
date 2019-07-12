# map filter 

 - map
 - filter

 
 要点 1：
 
     1. python3 的map filter ，返回的是迭代器，python2里返回的是list
     
     2. for all expression F(x) in python2, 
        map(lambda x: F(x), xs) == [F(x) for x in xs]
        例如：
        map(lambda x: 0, xs)  == [0 for x in xs]
        
        for all express F(x) in python3,
        map(lambda x: F(x), xs) == (F(x) for x in  xs)
        
     3. for all expression P(x) in python2, 
        filter(lambda x: P(x), xs) == [x for x in xs if P(x)] 
        
        for all expression P(x) in python3, 
        filter(lambda x: P(x), xs) == (x for x in xs if P(x))    # generator expression -- 生成器表达式
        
     4. for all expression F(x) and P(x) in python2,
        map(lambda x:F(x), filter(lambda x:P(x), xs)) == [F(x) for x in xs if P(x)]
        
        for all expression F(x) and P(x) in python3,
        map(lambda x:F(x), filter(lambda x:P(x), xs)) == (F(x) for x in xs if P(x))
        

要点 2：


### 术语表

    term-generator-expression
    
    term-iterator
    
    range iterable
    
    term-generator-expression
    
    term-list-comprehension
       


### 附录

https://docs.python.org/zh-cn/3/glossary.html#term-generator-expression

https://docs.python.org/3/glossary.html#term-iterator

https://docs.python.org/3/glossary.html#term-iterable

https://docs.python.org/3/glossary.html#term-generator-expression

https://docs.python.org/3/glossary.html#term-list-comprehension









