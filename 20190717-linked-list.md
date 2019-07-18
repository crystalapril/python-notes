# Linked List

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



### Linked Lists图形

    Singly Linked List 
    
    
    
    绘图代码：
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
    
    
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/single.png)
    
    
    Doubly Linked Lists：
    
    
    绘图代码：
    
    
    
    
![image](https://github.com/crystalapril/python-notes-april/blob/master/image/double.png)
    
    
    
    
    



    
    
    
### 附录    
    
    绘图网址： https://dreampuf.github.io/GraphvizOnline/
    
    

