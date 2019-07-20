# Linked List

 - 计算机语言的list 与 python list 的区别
 - Singly Linked List(单链表）
 - Doubly Linked Lists（双链表）
 - Singly Linked List to Array by Python
 - Linked Lists图形


### 计算机语言的list 与 python list 的区别

    计算机语言里有广义的 list（列表），类似 python 里面的 sequence(序列)
    
    广义的 list 就是有顺序的一堆东西，a0 a1 a2 a3 ...
    
    array 和 vector 更多的指一种数据结构，vector 就是一维向量，array 可以是多维的，一般来说都是一段连续内存。
    
    vector 和一维的 array 是一种广义的 list，包含 a0 a1 a2 ...这些元素，这些元素在内存位置上是连续的：
    
    |a0|a1|a2|...|...|...
    
    每个格子放一个元素，格子与格子紧挨着 
    
    
    python里如果把list叫做vector或者array，会比较准确
    
    但是因为python的标准库并没有提供 linked list ，把vector叫做list写起来比较短，在python里面也不会有歧义
    
    在更广泛的领域里list的含义要广得多     



### Singly Linked List(单链表）

    singly linked list 的数据构成是下面这样：
    
    |a0|p0| -> |a1|p1| -> |a2|p2| ...
    
    两个格子一组，叫做一个node
    
    每个node里面，一个格子保存元素a0 a1 a2 ...，另一个格子指向本node的下一个node
    
    每两个格子是挨一起的，组成一个node。
    
    但node和node之间的位置就不固定了，每个node里有一个格子用来把它们串成一串，所以叫linked list，link成一串   
        


### Doubly Linked Lists（双链表）

    双链表的结构如下：
    
    ...  <-> |p i-1|a i-1|n i-1| <-> |p i||a i|n i| <-> |p i+1||a i+1|n i+1| <-> ...
    
    每个node有3个格子，一个用来指向前面的node，一个用来指向后面的node
    

### Singly Linked List to Array by Python

    1.1 构造 to_list(('c', ('b', ('a', None)))) == ['c', 'b', 'a']
    def to_list(slist):
        l=[]
        while slist!=None:
            l.append(slist[0])
            slist = slist[1]
        return l  
        
    1.2 构造 to_slist([1,2,3])== (1, (2, (3, None)))
    def to_slist(xs):    
        t = None
        for x in xs[::-1]:
            t = (x,t)
        return t
    
    
    1.3 构造 reduce
    def reduce_s(f,slist,init=0):
        while slist != None:
            init = f(init,slist[0])
            slist = slist[1]
        return init
        
    # reduce_s(lambda x,y:x+y,(3, (2, (1, None))),init=0)    
    
    1.4 构造 map 
    1.4.1 slist to slist
    
    def map_s(f,slist):    
        t = []
        while slist != None:
            t.append([f(slist[0])])
            slist = slist[1]
        return t
    
    map_s(lambda x:x*2,[2,[3,[4,None]]])
    
    
    1.4.2 list to slist
    def map_s(f,slist):
        l=[]
        while slist !=None:
            l.append(f(slist[0]))
            slist = slist[1]
        return l      
        
    # map_s(lambda x:x*2,(3, (2, (1, None))))     
    
    1.5 构造 filter    
    1.5.1 slist to slist
    
    
    1.5.2 list to slist
    def filter_l(f,slist):
        l = []
        while slist != None:
            if f(slist[0]):
                l.append(slist[0])
            slist = slist[1]
        return l  

    # filter_l(lambda x: x % 2 ==1,(3, (2, (1, None))))
    
    
    # 构造 reverse  (x0, (x1, (x2, None)))  ---> (x2, (x1, (x0, None)))
    def reverse_s1(slist):    
        t=None
        while slist != None:
            t = (slist[0],t)
            slist = slist[1]
        return t    


### Linked Lists图形

    Singly Linked List 
    
    例 ：
    
    现在用tuple来表示节点，2元素的tuple(也叫pair)来表示node，用None来表示结尾
    
    1.None是一个空(linked 后面不说了)list
    2.假设xs是一个list
    3.那么ys = (x, xs) 就是一个新的list，ys在xs的前面添加了一个元素x
    
    
    假设有一个函数叫to_list
    
    1.这个函数接受上面说的linked list， 返回一个python的list
    2.那么，to_list(None) == []，就是说None表示空linked list，一个元素都没有
    3.(‘a',None) 就是在空linked list前面添加了一个元素'a'，
      to_list(('a', None)) == ['a']
    4.('b', ('a', None)) 就是在刚刚那个1个元素的linked list前面再添加了一个元素'b'
      to_list(('b', ('a', None))) == ['b', 'a']
    5.('c', ('b', ('a', None))) 就是在2元素的linked list前面再添加了一个元素'c'
      to_list(('c', ('b', ('a', None)))) == ['c', 'b', 'a']
    
    这就是一种用pair —— 2个元素的tuple —— 构造linked list的方式
    
    这里结尾就是用的None， |a0|n0| -> |a1|n1| -> ... |ai|ni| -> None
    
    空： None
    1个元素： |a0|n0| -> None
    2个元素： |a0|n0| -> |a1|n1| -> None
    多个元素： |a0|n0| -> |a1|n1| -> ... |ai|ni| -> None
    
    注意： 
    1. 比如说python的list，xs = ['a', 'b', 'c'] 
       然后可以 xs[-1], xs[-2], xs[-3] 这样取'c', 'b', 'a'
       也可以 xs[0], xs[1], xs[2] 这样取 'a', 'b', 'c'
       
    2. 单链表反过来就不行，每个node只有一个格子指向下一个，没有指向上一个的
       |a0|n0| -> |a1|n1| -> ... |ai|ni| -> None
       按 a0, a1, ... ai 的顺序可以顺着 n0, n1, ... 一直找直到None
       
       但是从None找不到ai，从a1找不到a0
       甚至指向None的不一定只有一个，指向a1的也不一定只有1个
       单链表的结构就注定了它只能从一个方向遍历  
             
    
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/single.png)
    
    
    Doubly Linked Lists：
    
    双链表可以双向走      
    
    如果双链表的“一端”（这里不说头尾）的prev指向“另一端”，“另一端”的next指向“一端”。
    
    1. xs, ys就是两个变量
    2. xs指向x0那个node，然后可以顺着next部分访问x1, x2, x3, 然后还可以接着x3的next部分回到x0
    3. 同时，顺着prev， 可以从xs -> x0 -> x3 -> x2 -> x1 -> x0 -> x3 -> x2 ...
    4. 一个双向的环， 所以双链表可以往两个方向
    5. 是一个闭合的环
    6. ys呢就指向x2那个
       可以顺着next访问 x2 -> x3 -> x0 -> x1 -> x2
       也可以顺着prev 访问 x2 -> x1 -> x0 -> x3 -> x2
    7. ys跟xs的区别就是起始点不一样，xs一开始指向的是x0,ys指向的是x2，还可以有zs指向x3
    8. 也有不构成环的双链表
    9. 双链表的特点就是有prev和next，指向前和后，有些喜欢构成环，有些不喜欢
    10. 不喜欢的话就有一个明确的头和尾
        头的prev指向None
        尾的next指向None
        图里画的是构成环的，也有不构成环的情况，不构成环也算双链表
            
    
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/double.png)

   
    
    
### 附录    
    
    绘图网址： https://dreampuf.github.io/GraphvizOnline/
    
Singly Linked List 例子的绘图代码：

    # slist
    // As = ('A', None) #       A
    // xs = ('a', None) #       a
    // Bs = ('B', xs)   #     B a
    // xs = ('b', xs)   #     b a
    // xs = ('c', xs)   #   c b a
    // Ds = ('D', xs)   # D c b a
    // xs = ('d', xs)   # d c b a

    digraph slist
    {
      None [shape=none]

      node [shape=record]

      a [label="'a' | <n>"]
      b [label="'b' | <n>"]
      c [label="'c' | <n>"]
      d [label="'d' | <n>"]

      A [label="'A' | <n>"]
      B [label="'B' | <n>"]
      D [label="'D' | <n>"]


      a:n -> None
      b:n -> a
      c:n -> b
      d:n -> c

      A:n -> None
      B:n -> a
      D:n -> c

      node [shape=ellipse]

      xs -> d
      As -> A
      Bs -> B
      Ds -> D
    }
    
    
Doubly Linked Lists 例子的绘图代码：
    
    # digraph dlist
    {
      None [shape=none]

      node [shape=record]

      x0 [label="<p> prev | x0 | <n> next"]
      x1 [label="<p> prev | x1 | <n> next"]
      x2 [label="<p> prev | x2 | <n> next"]
      x3 [label="<p> prev | x3 | <n> next"]

      x0:n -> x1
      x1:n -> x2
      x2:n -> x3
      x3:n -> None

      x0:p -> None
      x1:p -> x0
      x2:p -> x1
      x3:p -> x2

      node [shape=ellipse]

      xs -> x0
      ys -> x2
    }
    
    
    # digraph ring

    {
      node [shape=record]

      x0 [label="<p> prev | x0 | <n> next"]
      x1 [label="<p> prev | x1 | <n> next"]
      x2 [label="<p> prev | x2 | <n> next"]
      x3 [label="<p> prev | x3 | <n> next"]

      x0:n -> x1
      x1:n -> x2
      x2:n -> x3
      x3:n -> x0

      x0:p -> x3
      x1:p -> x0
      x2:p -> x1
      x3:p -> x2

      node [shape=ellipse]

      xs -> x0
      ys -> x2
    }
    
