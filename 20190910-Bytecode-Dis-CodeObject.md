# Stack-Bytecode-DisModulde-Compiler-Interpret-CodeObject

### Stack

    栈（stack）是一种数据结构
    first in last out的就叫栈，或者last in first out，后进先出
    调用栈的时候，调试里面一层一层的调用
    调用的那个层次就是一个stack，后调用的先返回，先调用的后返回
    就是比如说一叠盘子，拿的时候也是从最上面拿
    
    相对的是first in first out，先进先出，这个叫队列 queue（list，tuple都是queue）
    

### Bytecode-DisModulde

    调用栈的时候，调试器里看到的就是很多层，每一层叫做一个frame，里面有局部变量，参数，这些还记录了应该返回哪里
    所有的frame是一个stack
    最近产生的frame最先因为对应的函数返回而消失   
    
    在字节码层面，还有一个operand stack，操作数stack    

    example 1
    >>> import dis    
    
    >>> def add(a,b):
    ...     return a+b        
    >>> dis.dis(add)
     3        0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
    
    进入add函数之后
    add有2个局部变量（参数和局部变量统一算在一起）, operand stack最开始是空
    2             0 LOAD_FAST                0 (a)
    把序号为0的局部变量,也就是a， 加载(load)到operand stack里, 加载后operand stack的内容是 [a]
                  3 LOAD_FAST                1 (b)
    把序号为1的局部变量 b 加载到 operand stack 里， 加载后就是 [a, b]
                  6 BINARY_ADD          
    add 操作从 operand stack 里取出最上面两个， 把它们的和放到operand stack的最顶层
    也就是 [a + b的结果]
                  7 RETURN_VALUE     
    取出并返回operand stack的最顶层也就是 a+b 的结果
    local : [a, b]
    stack : []
    load_fast 0 之后
    stack : [a]
    load_fast 1 之后
    stack : [a, b]
    binary_add 之后
    stack : [a + b] # 注意这里只有1个元素了， 是a和b的sum
    return 之后
    stack : []  返回的是刚刚stack的顶层， 也就是a和b的sum

    就这个样子完成了def add(a, b):  return a + b 的操作
    
    
    example 2
    >>> def heron(a, b, c):
    ...     s = (a + b + c) / 2
    ...     return sqrt(s * (s - a) * (s - b) * (s - c))
     3        0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 LOAD_FAST                2 (c)
              8 BINARY_ADD
             10 LOAD_CONST               1 (2)
             12 BINARY_TRUE_DIVIDE
             14 STORE_FAST               3 (s)
     4       16 LOAD_GLOBAL              0 (sqrt)
             18 LOAD_FAST                3 (s)
             20 LOAD_FAST                3 (s)
             22 LOAD_FAST                0 (a)
             24 BINARY_SUBTRACT
             26 BINARY_MULTIPLY
             28 LOAD_FAST                3 (s)
             30 LOAD_FAST                1 (b)
             32 BINARY_SUBTRACT
             34 BINARY_MULTIPLY
             36 LOAD_FAST                3 (s)
             38 LOAD_FAST                2 (c)
             40 BINARY_SUBTRACT
             42 BINARY_MULTIPLY
             44 CALL_FUNCTION            1
             46 RETURN_VALUE
             
    local : [a, b, c, s]
    load_fast 0: 从local里取出0， 也就是a， 放到stack顶层， 之后stack是[a]
    load_fast 1: 执行后stack是[a, b]
    binary_add: 从stack顶层取出2个， 放回它们的和， 执行后 [a + b]
    load_fast 2: 执行后 [a + b, c]
    binary_add: [a + b + c]
    load_const 2: [a + b + c, 2]
    binay_true_divide: 同样是从顶层取2个， 进行除法， 放回stack， [(a + b + c) / 2]   
    store_fast 3: 从栈顶取出存放到局部的3号位置， 也就是s， 就完成了 s = (a + b + c) / 2。 然后栈就空了。
    load_global math: 加载全局的math [math]
    load_method : 加载方法 sqrt [math, sqrt]
    load_fast 3: 加载s [math, sqrt, s]
    load_fast 3: 加载s [math, sqrt, s, s]
    load_fast 0: 加载a [math, sqrt, s, s, a]
    binary_subtract: 取出2个放回它们的差 [math, sqrt, s, s - a ]
    binary_multiply: 取出2个放回它们的乘积 [math, sqrt, s * (s - a)]
    load_fast 3: 加载s [math, sqrt, s * (s - a), s]
    load_fast 1: 加载b [math, sqrt, s * (s - a), s, b]
    binary_subtract: 取出2个放回差 [math, sqrt, s * (s - a), s - b]
    binary_multiply: 取出2个放回乘积 [math, sqrt, s * (s - a) * (s - b)]
    load_fast 3: 加载s [math, sqrt, s * (s - a) * (s - b), s]
    load_fast 2: 加载c [math, sqrt, s * (s - a) * (s - b), s, c]
    binary_subtract: 取出2个放回差 [math, sqrt, s * (s - a) * (s - b), s - c]
    binary_multiply: 取出2个放回乘积 [math, sqrt, s * (s - a) * (s - b) * (s - c)]
    call_method 1: 取出3个元素， 最后1个是参数， 倒数第2个是方法， 倒数第1个是object， 进行调用。
    执行后栈的内容就是 [math.sqrt(s * (s - a) * (s - b) * (s - c))]
    return_value: 取出1个元素作为返回值返回

    python的这种叫做stack virtual machine，java和emacs的也是
    所有的计算，都是在 operand stack里完成的
    从里面取出一些东西， 进行一些操作， 然后把结果放回去
    因为是stack， 所以取和放都是最顶层
    
    对应的叫做register virtual machine，寄存器虚拟机，lua, erlang, 安卓和llvm都是这种
    (应该叫random access virtual machine，随机访问虚拟机，比较妥当，取和放回都不局限于顶层了)
    
    然后真正的硬件的cpu， 里面又有一种东西叫做register，真正的cpu就操作register和memory
    
    python bytecode 类似汇编语言，真正的cpu的汇编指令会更多，更不规律
    一条一条指令，操作一些东西，并不复杂，正是因为不复杂，所以要完成同样的工作相比高级语言就需要很多行   
    要读懂代码是干什么更费劲，上面还没有if, while这些东西，也没有try, except
 
 
### Compiler 编译器
    
    python是一个语言， 它有变量， 有if， 有while, for, 有function, （有class, ） 
    python的bytecode也是一个语言， 有local, 有operand stack， 有binary_add/sub/mul/div 有method_call, return_value
    把python转换成python bytecode的程序， 就是编译器
    要维持原有的含义，不是瞎转换
    
    一个程序 C， 它可以接受任意合法的python程序S， 输出python的 bytecode组成的程序T
    对任意合法的输入 I, S 会产生对应的输出 O
    对同样的输入 I， T 也要产生同样的输出 O
    这样的程序 C， 就叫做编译器 compiler
    如果不满足后面那个条件， 就是对合法的输入 I， T 产生了不一样的输出 O， 就是这个编译器 C 有 bug啦
    
    把上面的python程序和 python bytecode 程序替换掉， 就是一般的广义的编译器的定义：    
    一个程序 C
    * 它接受由 LS 语言构成的合法的程序 S
    * 输出由 LT 语言构成的程序 T
    * 对任意合法的输入 I， S 会产生输出 O
    * 对同样的输入 I， T 要产生同样的输出 O
    C就是编译器，语言之间的转换工具
    
    S (source) 和 T (target) ， target并不一定需要是汇编
    目标语言是某种汇编的情况比较常见，javascript的也比较常见，还有很多用C当目标语言的
    
    汇编也是一种编程语言，有自己的规则
    编译器也是一种程序，输入输出是别的程序
    
### Interpret
 
    当我们编写Python代码时，我们得到的是一个包含Python代码的以.py为扩展名的文本文    
    要运行代码，就需要Python解释器去执行.py文件
    
    
    
    compiler 和 interpret 的区别：
    

### CodeObject
    
    add.__code__
    python3.7中，code object 是一段可执行的 Python 代码在 CPython 中的内部表示
    code object 包含一系列直接操作虚拟机内部状态的指令
    这跟用 C 语言编程时是类似的，你写出人类可读的文本，然后用编译器转换成二进制形式
    二进制代码（C 的机器码或者是 Python 的字节码）被 CPU（对于 C 语言来说）或者 CPython 虚拟机虚拟的 CPU 直接执行
    
    code object 除了包含 指令，还提供了虚拟机运行代码所需要的一些 额外信息
    可以通过 func.__code__.attr 来查询，一共有 15 个 attr (属性)
    
|     attribute     |                            description                                     |
|-------------------|----------------------------------------------------------------------------|
| co_argcount       | 	number of arguments (not including keyword only arguments, * or ** args) |
| co_code           |	string of raw compiled bytecode                                          |
| co_cellvars       | 	tuple of names of cell variables (referenced by containing scopes)       |
| co_consts         |	tuple of constants used in the bytecode                                  |
| co_filename       |	name of file in which this code object was created                       |
| co_firstlineno    |	number of first line in Python source code                               |
| co_flags          |   bitmap of CO_* flags, read more here                                     |
| co_lnotab 	    |   encoded mapping of line numbers to bytecode indices                      |
| co_freevars 	    |   tuple of names of free variables (referenced via a function’s closure)   |
| co_kwonlyargcount |	number of keyword only arguments (not including ** arg)                  |
| co_name 	        |   name with which this code object was defined                             |
| co_names 	        |   tuple of names of local variables                                        |
| co_nlocals        |	number of local variables                                                |
| co_stacksize      | 	virtual machine stack space required                                     |
| co_varnames       |   tuple of names of arguments and local variables                          |

    
    add.__code__.co_argcount
    add.__code__.co_varnames
    add.__code__.co_code


  
  

