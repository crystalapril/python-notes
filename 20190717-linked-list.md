# Linked List

### 计算机语言的list 与 python list 的区别

    计算机语言里有广义的 list（列表），类似 python 里面的 sequence(序列)
    
    广义的 list 就是有顺序的一堆东西，a0 a1 a2 a3 ...
    
    array 和 vector 更多的指一种数据结构，vector 就是一维向量，array 可以是多维的，一般来说都是一段连续内存。
    
    vector 和一维的 array 是一种广义的 list，包含 a0 a1 a2 ...这些元素，这些元素在内存位置上是连续的：
    
    |a0|a1|a2|...|...|...
    
    每个格子放一个元素，格子与格子紧挨着  



### singly linked list(单链表）

    singly linked list 的数据构成是下面这样：
    
    |a0|p0| -> |a1|p1| -> |a2|p2| ...
    
    两个格子一组，叫做一个node
    
    每个node里面，一个格子保存元素a0 a1 a2 ...，另一个格子指向本node的下一个node
    
    每两个格子是挨一起的，组成一个node。
    
    但node和node之间的位置就不固定了，每个node里有一个格子用来把它们串成一串，所以叫linked list
    



#### Doubly Linked Lists（双链表）



### Linked Lists图形

