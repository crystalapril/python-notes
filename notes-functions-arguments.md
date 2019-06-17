函数的参数


1 参数个数

    函数可以有参数，也可以没有，但必须保留括号
    def fact1():
        print ("我也是函数")


2 参数传递的两种方式
    
    2.1 函数调用时，参数可以按照位置或名称方式传递
    def fact(n,m=1):
        s=1
        for i in range(1,n+1):
            s *= i
        return s//m

    >>>fact(10,5)         位置传递
       fact(m=5, n=10)    名称传递

    2.2 位置参数：    
    调用函数时，根据函数定义的参数位置来传递参数，如：
    def print_hello(name,sex):
        sex_dict={1:u'先生',2:u'女士'}
    >>>print( 'hello %s %s,welcome to python world' % (name,sex_dict.get(sex,u'先生') )
   
    调用时，两个参数的顺序必须一一对应，且少一个参数都不行
    >>>print_hello('duoduo',1)
    
3 可选参数/默认参数

    函数定义时可以为某些参数指定默认值，构成可选参数（默认参数）

    def <函数名>(<非可选参数>,<可选参数>):
        <函数体>
        return <返回值>

    例 3.1：
               m为可选参数
    def fact(n,m=1):
        s=1
        for i in range(1,n+1):
            s *= i
        return s//m
    >>>fact(10),fact(10,5)皆可      
    调用函数时可传可不传该默认参数的值

    注意事项1：所有位置参数必须在默认参数前，否则会报错，包括函数定义和调用，如：
    def print_hello(name,sex=1):    正确的定义方式
    def print_hello(sex=1,name):    错误的定义方式
    
    调用时：
    print_hello('tanggu')           正确的调用方式 
    print_hello('tanggu',sex=2)     正确的调用方式
    print_hello(sex=2,'tanggu')     错误的调用方式
    
    注意事项2：定义默认参数时，默认参数必须指向不变对象！！
    例 3.2：    著名大坑
    def add_end(L=[]):
        L.append('END')
        return L
        
    正常调用时没有问题：
    >>> add_end([1, 2, 3])
    [1, 2, 3, 'END'] 
    
    当你使用默认参数调用时，一开始结果也是对的：
    >>> add_end()
    ['END']
    
    但是，再次调用add_end()时，结果就不对了：
    >>> add_end()
    ['END', 'END']
    >>> add_end()
    ['END', 'END', 'END']   
    
    因为Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
     
    要修改上面的例子，我们可以用None这个不变对象来实现：
    def add_end(L=None):
        if L is None:
            L = []         #在函数内部定义[]，不会造成这个问题，此时L是局部变量
        L.append('END')
        return L   
        
    

4 可变参数传递

    函数定义时可以设计可变数量参数，既不确定参数总数量
    可变参数用参数前加个 *表示，传的参数要么是list，要么是tuple，也可以是0个参数，这些可变参数在函数调用时自动组装为一个tuple
    定义：def func(*args):
    调用：func()   func(a,b,c)   func([a,b,c])

    def <函数名>(<函数名>, *args):
        <函数体>
        return <返回值>
        
    例 4.1：
                 b为可变参数                
    def fact(n, *b):
        s=1
        for i in range(1,n+1)：
            s *= i
        for item in b:
            s *= item
        return s
    >>> fact(10,3)
    >>> fact(10,3,5,8)
    
    例 4.2  构造一个a² + b² + c² + …… 函数：
    确定参数的情况下，如numbers=[a,b,c]，函数为：
    def calc(numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
    调用的时候，需要先组装出一个list或tuple：
    >>> calc([1, 2, 3])   
    >>> calc((1, 3, 5, 7))
    
    函数的参数不确定的情况下可以改为可变参数：
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
    如果利用可变参数，调用函数的方式可以简化成这样：
    >>> calc(1, 2, 3)
    >>> calc(1, 3, 5, 7)
    >>> calc()
    如果已经有一个list或者tuple，可以这样调用可变参数:
    >>> nums = [1, 2, 3]
    >>> calc(*nums)
    *nums表示把nums这个list的所有元素作为可变参数传进去。  
    

5 关键字参数

    关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict（区别于可变参数的tuple）
    
    def <函数名>(<函数名>, *kw):
        <函数体>
        return <返回值>
    
    例 5.1:
    def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
    函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
    >>> person('Michael', 30)
    name: Michael age: 30 other: {}

    也可以传入任意个数的关键字参数：
    >>> person('Bob', 35, city='Beijing')
    name: Bob age: 35 other: {'city': 'Beijing'}
    >>> person('Adam', 45, gender='M', job='Engineer')
    name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
    
    关键字参数的作用：扩展函数的功能。比如你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

    和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
    >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
    >>> person('Jack', 24, **extra)
    name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

    **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict。
    注意：kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

6 命名关键字参数

    对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
    如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和gender作为关键字参数。
    
    例 6.1 :
    def person(name, age, *, city, job):
        print(name, age, city, job)
        
    >>> person('Jack', 24, city='Beijing', job='Engineer')
    Jack 24 Beijing Engineer
    命名关键字参数的输出结果其实并不是像关键字参数一样是一个dict，而是和位置参数的结果是类似的
    
    注意事项：
    -命名关键字参数必须传入参数名（名称传递），这和位置参数不同。如果没有传入参数名，调用将报错：
    
        >>> person('Jack', 24, 'Beijing', 'Engineer')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: person() takes 2 positional arguments but 4 were given
        由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。     
    
    -由于命名关键字参数city具有默认值，调用时，可不传入city参数：
        >>> person('Jack', 24, job='Engineer')
        Jack 24 Beijing Engineer            
        命名关键字参数把附加的可选参数的名字固定住了，可传可不传，传就得必须使用这个关键字参数名字

    -使用命名关键字参数时，如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了；如果没有可变参数，就必须加一个*作为特殊分隔符，如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
        def person(name, age, city, job):
            # 缺少 *，city和job被视为位置参数
            pass

7 参数组合

    函数可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以一起使用。
    但是，参数组合的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

    例 7.1：
    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
        
    在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
    >>> f1(1, 2)
    a = 1 b = 2 c = 0 args = () kw = {}
    >>> f1(1, 2, c=3)
    a = 1 b = 2 c = 3 args = () kw = {}
    >>> f1(1, 2, 3, 'a', 'b')
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
    >>> f1(1, 2, 3, 'a', 'b', x=99)
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
    >>> f2(1, 2, d=99, ext=None)
    a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

    通过一个tuple和dict，也可以调用上述函数：
    >>> args = (1, 2, 3, 4)
    >>> kw = {'d': 99, 'x': '#'}
    >>> f1(*args, **kw)
    a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
    >>> args = (1, 2, 3)
    >>> kw = {'d': 88, 'x': '#'}
    >>> f2(*args, **kw)
    a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

    所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

    虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。 




