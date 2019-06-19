集合、元祖、列表、字典

1 集合

1.1 集合类型定义

    集合类型与数学中的集合概念一致
    
    -集合元素之间无序，每个元素唯一，不存在相同元素
    -集合元素不可更改，不能是可变数据类型
    
    -集合用大括号{}表示，元素间用逗号分隔
    -建立集合类型用{}或set()
    -建立空集合类型，必须使用set()  （不同于tuple,list可以直接用(),[]来创建，因为{}表示空的字典）
    
    >>> A = {"python",123,("python",123)}  #使用{}建立集合
    {"python",123,("python",123)} 
    
    >>> B = set("pypy123")   #使用set()建立集合
    {'1','p','2','3','y'}    
    #注意，新建集合的顺序与原字符串的顺序有所不同了
    
    >>> C = {"python",123,"python",123} 
    {"python",123}
    #相当于去重了 

1.2 集合操作符（6个操作符， 4个增强操作符）
    
    操作符及应用      描述
    S | T            并，返回一个新集合，包括在集合S和T中的所有元素    
    S - T            差，返回一个新集合，包括在集合S但不在T中的元素    
    S & T            交，返回一个新集合，包括同时在集合S和T中的元素 
    S ^ T            补，返回一个新集合，包括集合S和T中的非相同元素 
    S <= T 或 S < T   返回True/False，判断S和T的子集关系
    S >= T 或 S > T   返回True/False，判断S和T的包含关系    
 
    S |= T           并，更新集合S，包括在集合S和T中的所有元素 
    S -= T           差，更新集合S，包括在集合S但不在T中的元素 
    S &= T           交，更新集合S，包括同时在集合S和T中的元素 
    S ^= T           补，更新集合S，包括集合S和T中的非相同元素 
    
    例 1.2：
    >>> A = {"p","y",123}
    >>> B = set("pypy123")
    {'1','p','2','3','y'}   
    
    >>> A - B   # 差
    {123}
    >>> B - A
    {'3','1','2'}
    >>> A & B   # 交
    {'p','y'}
    >>> A | B   # 并
    {'1','p','2','y','3',123}
    >>> A ^ B   # 补
    {'2',123,'3','1'}

1.3 集合处理方法

    操作函数或方法   描述
    S.add(x)       如果x不在集合S中，将x增加到S
    S.discard(x)   移除S中元素x，如果x不在集合S中，不报错
    S.remove(s)    移除S中元素x，如果x不在集合S中，产生KeyError异常
    S.clear()      移除S中所有的元素
    S.pop()        随机返回S的一个元素，更新S，若S为空产生KeyError异常
    S.copy()       返回集合S的一个副本
    len(S)         返回集合S的元素个数
    x in S         判断S中元素x，x在集合S中，返回True，否则返回False
    x not in S     判断S中元素x，x不在集合S中，返回True，否则返回False
    set(x)         将其他类型变量x转变为集合类型
    
    例 1.3：
    >>> A = {"p","y",123}
    >>> for item in A:
            print(item,end="")
    p123y    
    
    >>> A
    {"p",123,"y"}
    
    >>> try:
            while True:
                print(A.pop(),end="")
            except:
                pass
    p123y
    
    >>> A
    set()   
    
1.4 集合类型应用场景

    1.4.1 包含关系的比较
    >>> "p" in {"p","y",123}
    True
    >>> {"p","y"} >= {"p","y",123}
    False
    
    1.4.2 数据去重：集合类型所有元素无重复
    >>> ls = ["p","y","p","y",123]
    >>> s = set(ls)    # 利用了集合无重复元素的特点
    {"p","y",123}
    >>> lt = list(s)   # 还可以将集合转换为列表
    ["p","y",123]
 
 
2 序列类型及操作

2.1 序列类型定义

    序列是具有先后关系的一组元素
    
    -序列是一维元素向量，元素类型可以不同
    -类似数学元素序列：s₀,s₁,...,sₙ₋₁
    -元素间由序号引导，通过下标访问序列的特定元素   
    
    序列是一个基类类型，包含:    
    字符串类型 、元祖类型、列表类型
    
    序号的定义
     
                      反向递减序号
            <--------------------------------                    
     -5         -4         -3       -2           -1   
     
    "BIT"     3.1415      1024     (2,3)     ["中国",9]
    
      0          1          2        3            4
            -------------------------------->
                      正向递增序号
        

2.2 序列处理函数及方法

    操作符及应用          描述
    x in s              如果 x 是序列 s 的元素，返回True，否则返回Fasle
    x not in s          如果 x 是序列 s 的元素，返回Fasle，否则返回True
    s + t               连接两个序列 s 和 t
    s*n 或 n*s          将序列 s 复制 n 次
    s[i]                索引，返回 s 中的第 i 个元素，i是序列的序号
    s[i:j] 或 s[i:j:k]  切片，返回序列 s 中第 i 到 j 以 k 为步长的元素子序列
    
    例 2.2.1：
    >>> ls = ["python" ,123,".io"]
    >>> ls[::-1]
    ['.io',123,'python']
    >>> s = "python123.io"
    >>> s[::-1]
    'oi.321nohtyp'
        
    函数和方法                   描述
    len(s)                      返回序列s的长度，即元素个数
    min(s)                      返回序列s的最小值，s中元素需要可比较
    max(s)                      返回序列s的最大值，s中元素需要可比较
    s.index(x)或s.index(x,i,j)  返回序列s从i开始到j位置中第一次出现元素x的位置
    s.count(x)                  返回序列s中出现x的总次数
    
    例 2.2.2：
    >>> ls = ["python" ,123,".io"]
    >>> len(s)
    3
    >>> s = "python123.io"
    >>> max(s)
    'y'       

2.3 元祖类型及操作

    2.3.1 定义
    
    元祖是序列类型的一种扩展
    
    -元祖是一种序列类型，一旦创建就不能被修改
    -使用小括号()或tuple()创建，元素间用逗号,分隔
    -可以使用或不使用小括号，如：
        def func():
            return 1,2
    
    例 2.3.1.1：
    >>> creature = "cat","dog","tiger","human"   
    >>> creature
    ("cat","dog","tiger","human")
    >>> color = (0x001100,"blue",creature)
    >>> color
    (4352,'blue',('cat','dog','tiger','human'))
    
    2.3.2 元祖类型操作
    
    元祖继承序列类型的全部通用操作
    
    注意：    
    -元祖因为创建后不能修改，因此没有特殊操作
    -使用或者不使用小括号均可

    例 2.3.2.1：
    >>> creature = "cat","dog","tiger","human"   
    >>> creature[::-1]
    ("human","tiger","dog","cat")
    >>> color = (0x001100,"blue",creature)
    >>> color[-1][2]
    'tiger'  
     

2.4 列表类型及操作

    列表是序列类型的一种扩展，十分常用
    
    -列表是一种序列类型，创建后可以随意被修改
    -使用方括号[] 或 list()创建，元素之间用逗号，分隔
    -列表中各元素类型可以不同，无长度限制
    
    例 2.4.1：
    >>> ls = ["cat","dog","tiger",1024]
    >>> ls
    ["cat","dog","tiger",1024]
    >>> lt = ls
    >>> lt
    ["cat","dog","tiger",1024]
    注意： 这里ls和lt都指向了["cat","dog","tiger",1024]，这是个赋值的过程，并没有创建新的list
          方括号[]真正创建一个列表，而赋值仅传递引用
    
    函数或方法         描述
    ls[i] = x         替换列表ls第i元素为x
    ls[i:j:k] = lt    用列表lt替换ls切片后对应元素子列表
    del ls[i]         删除列表ls第i元素
    del ls[i:j:k]     删除列表ls中第i到第j以k为步长的元素
    ls += lt          更新列表ls，将列表lt元素增加到列表ls中
    ls *= n           更新列表ls，其元素重复n次
    
    例 2.4.2：
    >>> ls = ["cat","dog","tiger",1024]
    >>> ls[1:2] = [1,2,3,4]
    ['cat',1,2,3,4,'tiger',1024]
    >>> del ls[::3]
    [1,2,4,'tiger']
    >>> ls *2
    [1,2,4,'tiger',1,2,4,'tiger']
  
    函数或方法         描述
    ls.append(x)      在列表ls最后增加一个元素x
    ls.clear()        删除列表ls中所有的元素
    ls.copy()         生成一个新列表，赋值ls中所有元素
    ls.insert(i,x)    在列表ls的第i位置增加元素x
    ls.pop(i)         将列表ls中第i位置元素取出并删除该元素
    ls.remove(x)      将列表ls中出现的第一个元素x删除
    ls.reverse()      将列表ls中的元素反转
    
    例 2.4.3：
    >>> ls = ["cat","dog","tiger",1024]
    >>> ls.append(1234)
    ['cat','dog','tiger',1024,1234]
    >>> ls.insert(3,"human")
    ['cat','dog','tiger','human',1024,1234]
    >>> ls.reverse()
    [1234,1024,'human','tiger','dog','cat']
    
2.5 序列类型应用场景

    数据表示： 
    -元祖用于元素不改变的应用场景，更多用于固定搭配场景
    -列表更加灵活，更为常见
    -最主要作用：表示一组有序数据，进而操作
    
    元素遍历：
    for item in ls:         for item in tp:
        <语句块>                 <语句块>
    
    数据保护：
    -如果不希望数据被程序改变，转换成元祖类型
    >>> lt = tuple(ls)

3 字典

3.1 字典类型定义

    映射：是一种键（索引）和值（数据）的对应
    
    例 3.1.1
                红色
    内部颜色                                  内部颜色：蓝色
                黑色       --------->   
    外部颜色                                  外部颜色：红色
                蓝色
    
    例 3.1.2：
    "streetAddr" : "中关村南大街5号"
    "city"       : "北京市"
    "zipcode"    : "100081"
    
    区别于序列类型（列表、元祖）：       
    ["python",123,".io"]
        |      |     |         ------>       内部颜色：蓝色
        0      1     2                       外部颜色：红色
    序列类型由0...N整数作为数据的默认索引        映射类型则由用户为数据定义索引
    
    
    字典类型是“映射”的体现
    
    -键值对：键是数据索引的扩展
    -字典是键值对的集合，键值对之间无序
    -采用大括号{}和dict()创建，键值对用冒号:表示   （回顾set，用{}表示，但是不能用{}创建空集合）
    {<键1>:<值1>,<键2>:<值2>,...,<键n>:<值n>}  
    
    
    在字典变量中，通过键获得值
    
    <字典变量> = {<键1>:<值1>,<键2>:<值2>,...,<键n>:<值n>}     
    <值> = <字典变量>[<键>]     <字典变量>[<键>] = <值>    
    []用来向字典变量中索引或者增加元素  （d[key]方法既可以索引，也可以赋值，增改）
    
    例 3.1.2
    >>> d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
    >>> d
    {'中国':'北京','美国':'华盛顿','法国':'巴黎'}
    >>> d
    '北京'
    >>> de = {};type(de)
    <class 'dict'>    
    type(x)
    返回变量x的类型 
    
        
3.2 字典处理函数及方法

    函数或方法    描述
    del d[k]    删除字典d中键k对应的数据值 
    k in d      判断键k是否在字典d中，如果在返回True，否则False
    d.keys()    返回字典d中所有的键信息
    d.values()  返回字典d中所有的值信息
    d.items()   返回字典d中所有的键值对信息
    
    例 3.2.1
    >>> d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
    >>> "中国" in d
    True
    >>> d.keys()
    dict_keys(['中国','美国','法国'])
    >>> d.values()
    dict_values(['北京','华盛顿','巴黎'])
    注意：这里返回的不是list，而是返回的一个可迭代的对象，如果需要转换成列表，可以用list(d.values())
    
    函数或方法             描述
    d.get(k,<default>)    键k存在，则返回相应值，不在则返回<default>值      (最为重要)
    d.pop(k,<default>)    键k存在，则取出相应值，不在则返回<default>值  
    d.popitem()           随机从字典d中取出一个键值对，以元祖形式返回
    d.clear()             删除所有的键值对
    len(d)                返回字典d中元素的个数
    
    例 3.2.2
    >>> d = {"中国":"北京","美国":"华盛顿","法国":"巴黎"}
    >>> d.get("中国","伊斯兰堡") 
    '北京'
    >>> d.get("巴基斯坦","伊斯兰堡")
    '伊斯兰堡'
    >>> d.popitem()
    ('美国','华盛顿')
    
3.3 字典类型应用场景
    
    映射的表达：
    -映射无处不在，键值对无处不在
    -例如：统计数据出现的次数，数据是键，次数是值
    -最主要作用：表达键值对数据，进而操作

    元素遍历：
    for k in d :
        <语句块>
    


