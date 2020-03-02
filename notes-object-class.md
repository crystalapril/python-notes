# Object & Class

- 对象概述 outline of object
- 类，对象和实例 class, object & instance
- 类的属性和方法 attribute & method 
- 自定义类
- 类的封装及私有化 encapsulation
- 类的多态 polymorphism
- 类的继承和超类 inheritance
- 类的魔方方法

### 对象概述 outline of object

    一切皆对象 everything is object
    
    python有句话叫一切皆对象
    什么意思呢，就是你之前学过的，接触过的，都是对象
    
    举个栗子，第一篇里的整数 int 是 object，字符串 string 也是 object，同样 list 也是object 
    包括前天提到的，open 函数打开文档，返回的也是 file object
    
    那么，什么是对象？
    对象是python 里面一切事物的 基类（即基本类别）
    
    是不是到了这里，还是很困惑，一切都是对象，这有概念什么意义呢，我们接着往下看。
    

### 类，对象和实例 class, object & instance

    上面提到了，object 是python里面的最基础的类别
    
    那除了基类还有别的类别吗，当然有
    
    我们把 很相似（相似的属性、方法）的object 归为一类 （class）
    
    比如说，
    字符串 strings是一类，而 具体的'abc'是 str 类的 实例（instance）
    integer 整数是一类，具体的 123 是 int 类的 instance       
    
    这里有点类似生物界的分类
    我们人类是一个类别，每个具体的人呢，april是 Human 类中的 instance
    (python3里，class和type几乎同义，python2有所不同，这个不用深究)        
    

### 类的属性和方法 attribute & method 

    上面提到了我们把具有相似属性和方法object 归为一类
    
    那么，什么是属性 attribute ，什么是方法 method
     - 属性attribute 就是该对象的一些特有的性质，同一类的实例往往具有相同的属性
     - 方法就是该对象上绑定的函数
       之前我们见到了 len（）函数，strip（）方法，可能很困惑，这两个明明看起来差不多，为什么名称不同
       其实差别就在这里，函数可以单独使用，方法要对象的实例 instance 调用，是绑在实例上的
    
    我们还是以 字符串为例来说明：
    >>> a = '123 '
    >>> a.__class__
    <class 'str'>
    __class__ 字符串这个类的属性之一，告诉你 '123 '属于 str 这个类
    >>> a.strip()
    '123'
    strip() 是字符串可以调用的方法之一，经strip处理后，字符串 '123 '去掉了空格   
        
    我们再对比一下函数
    >>> len(a)
    4
    发现区别没有，方法的调用是 instance.method() ,函数是 function(instance)    
       函数                 方法
      id(a)              a.title() 
      min(a)             a.split()    
    

### 自定义类

    上面我们以字符串'123 '为例，简单的介绍了object的要素
    
    有同学可能不满足于此，如果我们想自己定义一个类，或者改进python原有的类怎么办
    
    这节我们尝试自定义一个简单的类
    
    class Person: #类名需要大写
        def __init__(self,age,name):  # 定义了年龄和姓名属性，__init__后面再说
            self.age = age            
            self.name = name

        def eat(self,times):  # 定义了 eat 方法
            print(f'I have {times} meals a day.')

        def sleep(self,hour):  # 定义了 sleep 方法
            print(f'I sleep for {hour} hours a day.')
            
    从上面可以看到，自定义类：
       - 要用class语句，后面跟类名，这里是Person，类名需首字母大写
       - 类名后面可以加(object),或其他类的(类名),括号里的类名为我们自定义类的父类（父类的概念后面再说）
       - 如果父类是object，也可以省略，如 Person(object) 等同于 Person
       - class 里面可以自定义方法和属性
       - 定义方法与定义函数类似，都是通过 def 语句，区别在于定义方法的第一个参数默认是self，
         self意味着 object 本身，方法也可以被看做成是绑定到 self 上的函数
            
    我们以 Person 为例来建立一个实例：
     
    >>> april = Person(25,'april')   # 建立了一个april的实例instance
    >>> april.age
    25
    >>> april.name
    'april'
    >>> april.eat(3)     # 还可以用 Person.eat(april,3)
    I have 3 meals a day.     
    >>> april.sleep(8)
    I sleep for 8 hours a day. 
     
    这里，april 是 Person 的实例
    april.age 跟 self.age 是不是很相似
    没错，这里的 april 就作为第一个参数 self 自动被传入进去了  
     
    当然，不是所有的自定义类，都要有属性和方法，也可以什么都不做，例如：
    >>> class Person: 
    ...:    pass
    
    >>> class Person: 
    ...:    print("haha")
    haha
     
    定义属性，也不是非要用 __init__ ，也可以直接：
    >>> class Person:
    ...:     member = 0
    >>> april = Person(25,'april')
    >>> april.member
    0     
        

### 类的封装及私有化 encapsulation and privacy

    类的一个特点就是封装 encapsulation ，跟函数的封装类似
    
    我们在调用函数的时候，例如 
    >>> pow(2,4)
    16
    我们不需要知道pow函数里面是怎么写的，只需要知道pow可以用来进行幂运算，直接拿过来用就可以了
    
    同样，类也是如此，我们在调用方法时，也不需要知道方法是怎么写的
    >>> '123 '.strip()
    '123'
    >>> april.eat(3)     # 还可以用 Person.eat(april,3)
    I have 3 meals a day.   
    知道怎么用，能实现什么功能就好，这样让程序更简单
    
    
    Privacy
    
    但是有的同学说，这样还不够
    有些方法不希望别人使用，只有自己能用
    python为这种情况，提供了一个选项就是 私有化 privacy
    通过把想要隐藏的方法设为私有的（方法前加2个下划线 __method），让外面无法访问（其实是看起来无法访问）：
    
    我们通过下面的例子来说明：
    
    >>> class Person:
    ...:     def __init__(self,age,name):
    ...:         self.age = age
    ...:         self.name = name
    ...: 
    ...:     def __myweight(self):
    ...:         print("I won't tell you.")
    ...: 
    ...:     def weight(self):
    ...:         print("the weight is ...")
    ...:         self.__myweight()
    ...: 
    >>> april = Person(25,'april')
    >>> april.__myweight()
    Traceback (most recent call last):
      File "<ipython-input-17-b6512bc696d6>", line 1, in <module>
        april.__myweight()
    AttributeError: 'Person' object has no attribute '__myweight'
    >>> april.weight()
    the weight is ...
    I won't tell you.
    
    直接访问__myweight 被拒绝，这时候__myweight是私有的，程序显示没有这个属性
    通过weight方法进行内部访问，才可以访问到私有的内容
    
    但是事实上，python并不是绝对禁止访问私有的属性
    有一个办法可以让我们从外部访问私有属性：
    >>> april._Person__myweight()
    I won't tell you.
    
    在类名前加单下划线，后面跟着双下划线+私有方法名，就可以进入
    _Classname__privatemehtod
    
    尽管我们可以通过这个办法访问私有属性，但是还是尽量不要去这样做
    私有属性就类似一个提示，告诉大家没事不要去那里搞事情    
    

### 类的多态 polymorphism

    多态其实我们已经见过很多次了，例如下面：
    >>> 'abccd'.count('c')
    2
    >>> [1,2,3,4].count(3)
    1
    count方法，可以用于很多种对象，不仅仅限于str，list，这个就是多态
    
    多态就是一个方法，在不同种类的对象上都可以使用
    而不用去管这个对象是什么样的，对象的方法到底是怎么写的
    只需要知道这个实例或对象能用这个方法就行了（其实这点也跟封装有些相似）
    
    除了方法以外，某些运算也可以看做是多态性，例如：
    >>> 1+2
    3
    >>> 'a'+'bc'
    'abc'   
    

### 类的继承和超类 inheritance

    继承是类里面特别重要的一个特性
    
    其实，看名字我们也能大概猜到，类的属性和方法等是可以被继承的
    被继承的类叫做超类、父类或基类，承接的类叫做子类，这个名字也蛮形象的
    
    这个有什么意义呢
    当我们已经创建好了一个类，并且已经在使用中
    如果我们在这个类的基础上，开发新的功能，我们三个办法：
    1.修改之前的类，以适应新的功能
      这样需要修改随之而来的各种，容易造成混乱
    2.写一个新的类，但是会存在重复代码，重复是很糟糕的事情
    3.继承
      写一个新的类，让它继承原有类的属性和方法，添加新的功能，同时不影响原来的类的使用
      
    因此，继承很好的解决了功能扩展，以及避免代码重复
    
    我们还是以 Person 为例，接着创建它的子类：
    class Athlete(Person):
        def run(self,meters):
            print(f'I run {meters}m in a minutes.')
        def sleep(self):
            print(f'I always sleep at the daytime')
            
    子类创建好了，我们来验证一下：
    >>> issubclass(Athlete,Person)   # issubclass用于检验是否为子类： Athlete 是否为 Person 的子类
    True
    >>> issubclass(Person,Athlete)
    False
    
    >>> Person.__bases__   # __bases__用于查询类的父类是什么 ：Athlete的父类是 Person
    (object,)
    >>> Athlete.__bases__
    (__main__.Person,)
    
    我们来给 Athlete 创建一个实例，并分别验证属性和方法：
    >>> roc = Athlete(22,'roc')
    >>> roc.__class__
    __main__.Athlete
    >>> isinstance(roc,Person)
    True
    >>> isinstance(roc,Athlete)
    True
    >>> isinstance(roc,str)
    False    
    
    >>> roc.age      # 调用父类 Person 的属性
    22
    >>> roc.eat(2)       # 调用父类 Person 的方法
    I have 2 meals a day.
    >>> roc.run(50)       # 调用子类 Athlete 的方法
    I run 50m in a minutes.
    
    我们注意到了，Athlete 和 Person 都有一个sleep 方法，并且写的不同
    当这种情况的时候，调用子类的方法还会继承父类的sleep吗：
    >>> roc.sleep()
    I always sleep at the daytime
    此时，roc 调用的是子类的 sleep方法，父类的同名方法没有被调用
    这叫做 override 重写
    当有子类有同名的方法出现时，子类的实例调用的是子类自己的方法
    
    
    除此以外，python 还支持多重继承  mutiple superclasses
    就是一个类可以有多个爸爸，我们来举例：
    class Student(Person):
        def learn(self,hours):
            print(f'I study for {hours} hours a day')

    class AthleteStudent(Athlete,Student):
        pass
        
    >>> AthleteStudent.__bases__
    (__main__.Athlete, __main__.Student)     # AthleteStudent 有两个父类，Athlete 和 Student
    >>> rabbit = AthleteStudent(24,'rabbit')  # 创建实例
    >>> rabbit.age                            # 调用爷爷类 Person 的属性 （继承可以一直延续、追溯）
    24
    >>> rabbit.learn(6)                       # 调用父类 Student 的属性
    I study for 6 hours a day

    我们还有其他方法来验证类的属性和方法
    >>> hasattr(rabbit,'age')  # hasattr 用于检验实例 rabbit 有无 age 属性
    True
    >>> hasattr(roc,'learn')
    False
    >>> callable(getattr(rabbit,'age'))  # getattr 用于获取实例 rabbit 有无 age 属性
    False
    >>> callable(getattr(rabbit,'learn'))  # callable用于检验参数是否可以被调用（类似函数一样）
    True
    >>> setattr(rabbit,'gender','male')  # setattr 用于设置属性
    >>> rabbit.gender
    'male'
    
           
### 类的魔方方法 Magic methods

    类里面有一些特殊的方法，眼尖的同学可能已经留意到了
    前面我们的例子中，出现了一些带双下划线的方法，如__init__
    
    下面是一个类和普通的方法：
    >>> class Student:
    ...:     def init(self,grade):
    ...:         self.grade = grade
    >>> e = Student()
    >>> e.init(5)
    >>> e.grade
    5
    
    下面是一个类和特殊方法：
    >>> class Student(Person):
    ...:     def __init__(self,grade=5):
    ...:         self.grade = grade
    >>> f = Student()
    >>> f.grade
    5
    
    发现了吗，__init__ 和 init 实现的是同一种功能
    但是 __init__ 比 init 少一个步骤，无需单独调用
    
    因为 __init__ 是创建实例的时候，自动对类进行了初始化，__init__又叫构造器 constructor
    __init__ 像施魔法一样实现了这个功能，又叫魔方方法
    魔方方法不仅仅是 __init__ ，还有很多，后面会提到
    
    这个例子里的参数是可选的，那么如果我们对这个参数进行指定呢？    
    >>> duobao = Student('I am college student.')
    >>> duobao.grade
    'I am college student.'

    当然，也可以连可选参数都不设置：
    >>> class Student(Person):
    ...:     def __init__(self):
    ...:         self.grade = 5
    >>> f = Student()
    >>> f.grade
    5
    
    前面我们提到过，当子类和父类有同样的方法时，会存在一个override的问题
    那么 __init__ 是否也会有这个问题：
    >>> class Person:
    ...:    def __init__(self,age,name):
    ...:        self.age = age
    ...:        self.name = name
    ...:    def eat(self,times):
    ...:        print(f'{self.name} have {times} meals a day.')

    >>> class Student(Person):
    ...:    def __init__(self):
    ...:        self.grade = 5

    >>> f = Student()
    >>> f.grade
    5
    >>> f.eat(3)
    Traceback (most recent call last):
      File "<ipython-input-104-ce0860987d66>", line 1, in <module>
        f.eat(3)
      File "<ipython-input-101-4c51b8c00442>", line 8, in eat
        print(f'{self.name} have {times} meals a day.')
    AttributeError: 'Student' object has no attribute 'name'
    
    从这个报错可以看到
    Student 没用 eat 这个方法，f.eat(3) 调用的是父类 Person 的eat方法，这步没有问题
    但是接下来，Person 的eat 在引用 self.name 的时候报错了
    显示 Student 没有 name 这个属性
    也就是说，子类 Student 的 __init__ 覆盖override了父类的__init__ 方法，不再有父类的name属性了
    
    那么如何解决这个问题？
    有两种方法：
    1.调用未关联的超类构造函数 unbound superclass constructor
    2.使用super函数
    
    我们来看第一个：
    >>> class Student(Person):
    ...:     def __init__(self,age,name):
    ...:         Person.__init__(self,age,name)   
    >>> f = Student(22,'roc')
    >>> f.age
    22    
    通过 Person.__init__(self) 的方式，成功调用了父类Person 的 age 属性
    这里，通过调用Person.__init__，没用实例与其相关联，因此叫做未关联的 （其实这个概念还不是很明白。。。）
    
    第二个方法：
    >>> class Student(Person):
    ...:     def __init__(self,age,name):
    ...:         super().__init__(age,name)
    ...:         self.grade = 5
    >>> f = Student(22,'roc')
    >>> f.age
    22
    通过super()函数，也成功调用了父类的属性
    注意，super()函数里，不包含self，可以没有参数
    
    super()现在应用的更多，也更适用于python3，尽量用super()来解决这个问题
    
    
    除了__init__ ，还有几个常用的魔方方法：
    __getattr__
    
    __setattr__
    
    __delattr__
    
    
    
    
    
    

    
    
    
    
