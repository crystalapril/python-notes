# Stack-Bytecode-DisModulde-CodeObject

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
     3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
    
    进入add函数之后
    add有2个局部变量（参数和局部变量统一算在一起）
    operand stack最开始是空
    2           0 LOAD_FAST                0 (a)
    把序号为0的局部变量 —— 也就是a， 加载(load)到operand stack里
    加载后operand stack的内容是 [a]
                  3 LOAD_FAST                1 (b)
    把序号为1的局部变量b加载到operand stack里， 加载后就是 [a, b]
                  6 BINARY_ADD          
    add操作从operand stack里取出最上面两个， 把它们的和放到operand stack的最顶层
    也就是 [a + b的结果]
                  7 RETURN_VALUE     
    取出并返回operand stack的最顶层也就是 a+b的结果
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
     3           0 LOAD_FAST                0 (a)
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
    
    对应的叫做register virtual machine，寄存器虚拟机
    应该叫random access virtual machine，随机访问虚拟机，比较妥当，取和放回都不局限于顶层了
    lua, erlang, 安卓和llvm都是这种
    然后真正的硬件的cpu， 里面又有一种东西叫做register，真正的cpu就操作register和memory
    
    python bytecode 类似汇编语言，真正的cpu的汇编指令会更多，更不规律
    一条一条指令，操作一些东西，并不复杂，正是因为不复杂，所以要完成同样的工作相比高级语言就需要很多行   
    要读懂代码是干什么更费劲，上面还没有if, while这些东西，也没有try, except
 
 
### compiler 编译器
    
    python是一个语言， 它有变量， 有if， 有while, for, 有function, （有class, ） 
    python的bytecode也是一个语言， 有local, 有operand stack， 有binary_add/sub/mul/div 有method_call, return_value
    把python转换成python bytecode的程序， 就是编译器
    要维持原有的含义，不是瞎转换
    
    一个程序 C， 它可以接受任意合法的python程序S， 输出python的bytecode组成的程序T。
    对任意合法的输入I, S会产生对应的输出O。
    对同样的输入I， T也要产生同样的输出O。
    这样的程序C， 就叫做编译器compiler
    如果不满足后面那个条件， 就是对合法的输入I， T产生了不一样的输出O， 就是这个编译器C有bug啦
    
    把上面的python程序和python bytecode程序替换掉， 就是一般的广义的编译器的定义：    
    一个程序C
    * 它接受由LS语言构成的合法的程序S
    * 输出由LT语言构成的程序T
    * 对任意合法的输入I， S 会产生输出O
    * 对同样的输入I， T要产生同样的输出O
    C就是编译器，语言之间的转换工具
    
    S (source) 和 T (target) ， target并不一定需要是汇编
    目标语言是某种汇编的情况比较常见，javascript的也比较常见，还有很多用C当目标语言的
    
    汇编也是一种编程语言，有自己的规则
    编译器也是一种程序，输入输出是别的程序
    
    

### CodeObject
  
  

