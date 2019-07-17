* Map Filter Reduce


* Map

# 1.1 用 for loops 表达 map 函数，返回list（类似python2 map）
def map1(f,xs):
   l=[]
   for x in xs:
      l.append(f(x))
   return l

# 1.2 用 while 表达 map 函数，返回list（类似python2 map）
def map2(f,xs):
   i=0
   l=[]
   while i < len(xs):
      l.append(f(xs[i])
      i +=1
   return l

               
* Filter

# 2.1 用 for loops 表达 filter 函数，返回list（类似python2 filter）
def filter1(f,xs):
   l=[]
   for x in xs:
      if f(x):
         l.append(x)
   return l

# 2.2 用 while 表达 filter 函数，返回list（类似python2 filter）
def filter2(f,xs):
   i=0
   l=[]
   while i < len(xs):
      if f(xs[i]):
         l.append(xs[i])
      i +=1
   return l

               
* Reduce

# 3.1 用 for loops 表达 reduce 函数，返回list
def reduce1(f,xs,init=0):
    for x in xs:
      init = f(init,x)
    return init

# 3.2 用 while 表达 reduce 函数，返回list
def reduce2(f,xs,init=0):
   i=0
   while i < len(xs):
      init = f(init,xs[i])
      i +=1
   return init
               

