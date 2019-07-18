* Map Filter Reduce


* Map

# 1.1 用 for loops 表达 map 函数，返回list（类似python2 map）
def map1(f,xs):
    l=[]
    for x in xs:
        l.append(f(x))
    return l

# 1.2 用 while 表达 map 函数，返回list（类似python2 map）  

# 1.2.1 适用于list，tuple
def map2(f,xs):
    i=0
    l=[]
    while i < len(xs):
        l.append(f(xs[i]))
        i +=1
    return l

# 1.2.2 适用于set，dict   缺点：会破坏原有的序列
def map3(f,xs):
    i=0
    l=[]
    a=len(xs)
    while i < a:
        if type(xs) != dict:
            l.insert(0,f(xs.pop()))
        else:
            l.insert(0,f(xs.popitem()))
        i +=1
    return l

# 1.2.3 适用于 set,dict   next({'a':1,'b':2})之后，默认返回key{'a','b'}
def map4(f,xs):
    i=0
    l=[]
    a=iter(xs)
    while i < len(xs):
        l.append(f(next(a)))
        i +=1
    return l

# 1.2.4 适用于 set,dict  by enumerate
def filter4(f,xs):
    i=0
    l=[]
    a=iter(xs)
    while i < len(xs):
        x = next(a)
        if f(x):
            l.append(x)
        i += 1
    return l
# eg.  list(map3(abs,{-1,-2,3})),  list(map3(lambda x:x,{'a':-1,'b':-2,'c':-3})) 


* Filter

# 2.1 用 for loops 表达 filter 函数，返回list（类似python2 filter）
def filter1(f,xs):
    l=[]
    for x in xs:
        if f(x):
            l.append(x)
    return l

# 2.2 用 while 表达 filter 函数，返回list（类似python2 filter）

# 2.2.1 适用于list，tuple
def filter2(f,xs):
    i=0
    l=[]
    while i < len(xs):
        if f(xs[i]):
            l.append(xs[i])
        i +=1
    return l

# 2.2.2 适用于set，dict,by pop
def filter3(f,xs):
    i=0
    l=[]
    a=len(xs)
    while i < a:        
        if type(xs) != dict:
            a=xs.pop()
        else:
            a=xs.popitem()
        if f(a):
            l.insert(0,a)        
        i +=1
    return l

# 2.2.3 适用于set，dict ,by iter(),next()
def filter4(f,xs):
    i=0
    l=[]
    a=iter(xs)
    while i < len(xs):
        x = next(a)
        if f(x):
            l.append(x)
        i += 1
    return l

# 2.2.4 适用于set，dict ,by enumerate
def filter5(f,xs):
    i = 0 
    l1 = list(enumerate(xs))
    l2 =[]
    while i < len(l1):
        if f(l1[i][1]):
            l2.append(l1[i][1])
        return l2
    
* Reduce

# 3.1 用 for loops 表达 reduce 函数，返回list
def reduce1(f,xs,init=0):
    for x in xs:
        init = f(init,x)
    return init

# 3.2 用 while 表达 reduce 函数，返回list

# 3.2.1 适用于list, tuple
def reduce2(f,xs,init=0):
    i=0
    while i < len(xs):
        init = f(init,xs[i])
        i +=1
    return init

# 3.2.2 适用于set,dict  by iter(),next()
def reduce4(f,xs,init=0):
    i =0
    a = iter(xs)
    while i < len(xs):
        init = f(init,next(a))
        i += 1
    return init

# 3.2.3 适用于set,dict  by enumerate
def reduce5(f,xs,init=0):
    i = 0
    l = list(enumerate(xs))
    while i < len(xs):
        init = f(init,l[i][1])
        i +=1
    return init

               

