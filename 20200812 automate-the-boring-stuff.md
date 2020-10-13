# Note of Automate the Boring Stuff

### 1.Basic

    1.1 operator
    1.1.1 // , %
    1.1.2 * ，只能用于2数字，或str和一个整数， 错误： 'Alice' * 5.0
    
    1.2 assignment statement
    把变量想象成一个贴了标签的盒子，value的reference放在了盒子里
    
    1.3 variable name : 
    no hyphens (连字符)，不能以数字开头，不能有特殊符号如￥
    
    1.4 int function:     
    正确： int(99.99)
    正确： int('99')
    错误： int('99.99')
    
    1.5 数字前可以加0 ，正确： 42.0 == 0042.000
   

### 2.Flow Control

    2.1 can't assign to keyword ，布尔值不可以被赋值， 错误： True = 2 + 2
    
    2.2 and, or, not  
    
    2.3 break, continue


### 3.Function

    3.1 print() returns None

    3.2 the Call Stack ： 
    stack-like structure 先进后出
    the current topic is always at the top of the stack

    3.3 local and global scope
    3.3.1 global scope : global variable
    3.3.2 global statement : global variable
    3.3.3 function and assignment statement: local variable 
    3.3.4 function and without assignment statement : global variable  
    
    3.4  sys.exit()
    
    3.5 variable-length number of arguments with *args and **kwargs
    f(*args) , 其实是 <expr>(*<expr-arg>)
    args 是表达式，可以是变量表达式，如 *xs，也可以是其他的expression，如 *xs[i]下标表达式等
    
    *args 会作为 tuple 被传入f中， * 的作用是将后面的 args 一一展平
    如 f(*(x1,x2,x3))== f(x1,x2,x3)
       f(*([x0] + [x1] + [x2]))  == f(x1,x2,x3)


### 4.List
    
    4.1 index 必须整数，错误：alist[1.0]

    4.2 multiple assignment 个数必须一致
    正确： size, color, disposition = ['fat', 'gray', 'loud']  
    错误： size, color, disposition, name = ['fat', 'gray', 'loud']  
    
    4.3 random.choice(),random.shuffle()

    4.4 alist.sort()   
    4.4.1 默认情况下，Z(大写) 排在  a（小写） 前面
    4.4.2 alist.sort() : return None , 只用于list, sort list in place 当场修改原list
          sorted(list) ：return new list
    
    4.5 \ line continuation character 
    
    4.6 mutable: list , dict  ; immutable : integer, string, tuple
        
    4.7 overwritten ： 下面例子，没有修改eggs 这个list：
        >>> eggs = [1, 2, 3]
        >>> eggs = [4, 5, 6]
        
        modify： 下面这个例子，才是修改了eggs，这个list：
        >>> eggs = [1, 2, 3]
        >>> del eggs[2]     >>> del eggs[1]     >>> del eggs[0]
        >>> eggs.append(4)  >>> eggs.append(5)  >>> eggs.append(6)
        原因在于，我们赋值的时候，假设 variable是个盒子，这个盒子里，装的不是list本身，而是存放list的地址这个链接reference
        第一个例子，eggs 被装进了新的 reference，跟新的list关联上了，原有的list没有被修改，只是跟eggs取关
        
    4.8 id()
    
    4.9 copy.copy(), copy.deepcopy()

    4.10 in
         错误： 1 or 2 in [4,5,6]
         正确： 1 in [4,5,6] or 2 in [4,5,6]
         
         留意：有些语言中 0 < x < 100 是不行的，必须 0 < x and x < 100 ，不过python没有这个问题
         
    
    
### 5.Dictionaries and Structuring Data

    5.1 unodered，字典是无序的
    相同的key-value pair, 不同的order, 字典的值相等
    
    5.2 python3.7之后，从dict里取出的key的list，保留原来的 'key' 的顺序
    >>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    >>> list(eggs)
    ['name', 'species', 'age']
    
    5.3 d.keys(),d.values(),d.items() 返回dict_keys, dict_values, and dict_items （不是 list）
    可以用for loop，list()
    
    5.4 dict.get(key,defualt), dict.setdefualt(key,defualt)
    
    5.5 pprint.pprint()
 
 
 ### 6.Manipulating Strings

    6.1 escape character, raw string
    
    6.2 >>> '' in 'april'
        True
        
    6.3 f-string, % , format

    6.4 str.method   
        6.4.1 str.lower()    , str.upper()    不修改原str，返回新的
              str.isupper()  , str.islower()  至少有一个字母，所有的字母大写（小写），return True
              eg.   >>> '12345'.islower()     >>> '12345'.isupper()          >>> '12abc'.islower() 
                    False                     False                             True                     

        6.4.2 split(), partition()
        6.4.3 rjust(), ljust(), center() | rstrip(),lstrip(),strip()  除了删除两端的 space，也可以删除 character
     
    6.5 ord(), chr()
 
 
### 7.Pattern Matching with Regular Expressions

    7.1 re模块    
    7.1.1 re.compile()， 返回 Regex Objects 
    7.1.2 re.search() ，返回 Match object of the first matched text 
    7.1.3 re.group(), re.groups() 
    7.1.4 re.findall()， 返回 list of strings of every match
          string 没有 group的时候，返回 [s1,s2]；有group的时候，返回[(s1,s2),(s3,s4)]    
    7.1.5 re.DOTALL ，让 . (dot character)可以匹配一切字符，包括换行符
    
    7.2 escape characters \
    
    7.3 | pipe
    
    7.4 匹配符号    

        ?      matches 0 or 1 
        *      matches 0 or more 
        +      matches 1 or more 
        {n}    matches exactly n ; {n,} matches n or more ; {,m} matches 0 to m ; {n,m}  matches n ~ m
        {n,m}? or *? or +? performs a non-greedy match of the preceding group.
        ^      means the string must begin with spam. （脱字符 caret character）
        $      means the string must end with spam. 
        .      matches any character, except newline characters.
        [abc]  matches any character between the brackets (such as a, b, or c).
        [^abc] matches any character that isn’t between the brackets.
        
    7.5 greedy & non-greedy
        greedy: 默认的，最大匹配  ，             r'(Ha){3,5}' 匹配 'HaHaHaHaHa'中的 'HaHaHaHaHa'
        non-greedy（后面加？）： 最小程度匹配 ，  r'(Ha){3,5}?' 匹配 'HaHaHaHaHa'中的 'HaHaHa'        
        
    7.6 Character Classes
        \d  [0-9]
        \D  [^0-9]
        \w  [a-zA-Z0-9_]
        \W  [^a-zA-Z0-9_]
        \s  [\n\t\space] 
        \S  [^\n\t\space]        
   
    7.7
        
       

        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
              
        
        
        
        
          
          
       
    
    
    

