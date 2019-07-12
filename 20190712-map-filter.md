# map filter range

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

    range in python2 返回 list
    range in python3 返回 iterable
    
要点 3：

    generator expression 的括号有时候可以省，如：
        
    sum(i*i for i in range(10)) 
    
    
    tuple的括号
    
    有时候可以省略：
    x, y = y, x
    
    x0, x1 = 1, 2

    def divmod(x, y):
        return x//y, x%y
           
    有时候不能省略：
    
    melting_point = [ ('C'  , 3800   ),('Al' , 933.47), ...]   
    
    f(x,y)  f((x,y))    
    
    [(x,y)]  [x,y]

### 术语表

* [iterator](https://docs.python.org/3/glossary.html#term-iterator)
* [iterable](https://docs.python.org/3/glossary.html#term-iterable)
* [list comprehension](https://docs.python.org/3/glossary.html#term-list-comprehension)
* [generator expression](https://docs.python.org/3/glossary.html#term-generator-expression)
  [zh-cn](https://docs.python.org/zh-cn/3/glossary.html#term-generator-expression)
