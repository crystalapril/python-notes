# Python3 内置函数

|               |             |   内置函数    |              |                |
| ------------- | ----------- | ------------ | ------------ | -------------- | 
| abs()         | delattr()   | hash()       | memoryview() | set()          |
| all()         | dict()      | help()       | min()        | setattr()      |
| any()         | dir()       | hex()        | next()       | slice()        |
| ascii()       | divomod()   | id()         | object()     | sorted()       |
| bin()         | enumerate() | input()      | oct()        | staticmethod() |
| bool()        | eval()      | int()        | open()       | str()          |
| breakpoint()  | exec()      | isinstance() | ord()        | sum()          |
| bytearaary()  | filter()    | issubclass() | pow()        | super()        |
| bytes()       | float()     | iter()       | print()      | tuple()        |
| callable()    | format()    | len()        | property()   | type()         |
| chr()         | forzenset() | list()       | range()      | vars()         | 
| classmethod() | getattr()   | locals()     | repr()       | zip()          |
| complie()     | globals()   | map()        | reversed()   | __import__()   |
| complex()     | hasattr()   | max()        | round()      |                |

# 常用函数类型

  - 序列操作 
  - 数据类型
  - 数学函数


### 序列操作 

```sh
list(), tuple(), sorted(), reversed(), slice(), zip(), len(), set(), dict(), enumerate(), all(), any()     
```

Reversed():

    对于一个指定的列表，对其反向排序，可以用reversed()函数，list.reverse()方法，或[：：-1]
    
    reversed(seq)   
    -seq是要转换的序列，可以是 tuple, string, list 或 range
    
    reversed() 函数返回一个反转的迭代器，需要通过遍历，或者List,或next()等方法，获取运算后的值。
    例 1.1：
    >> seqString = 'Runoob'
    >> print(list(reversed(seqString)))
    ['b', 'o', 'o', 'n', 'u', 'R']
    
    >> seqList = [1, 2, 4, 3, 5]
    >> print(list(reversed(seqList)))
    [5, 3, 4, 2, 1]
    reversed() 函数返回一个新的序列，不会对原有序列做出修改
    
    list.reverse()
    python中list的有一个内置方法list.reverse()也可以进行反转，但仅用于list，不能用于其他序列包括dict
    例 1.2：    
    >> list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
    >> list1.reverse()
    >> list1 
    ['Baidu', 'Taobao', 'Runoob', 'Google']
    使用Reverse()方法会修改list本身，不会返回新list（没有返回值）

    [::-1]
    这个是python的slice notation的特殊用法，也可以对序列进行反转操作
    list的切片有三个参数:起点,终点,步长
    list[::-1] 相当于起点为最后的一个,终点为第一个,然后依次减少一个




### 数据类型 

```sh
int(), str(), complex(), isinstance(), format()
```

### 数学函数

```sh
min(), max(), round(), pow(), float(), int(), sum()
```



### 附录：

https://docs.python.org/zh-cn/3/library/functions.html


