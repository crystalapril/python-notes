# 程序的分支结构-条件语句

  - 单分支结构
  - 二分支结构
  - 多分支结构
  - 条件判断及组合
  - 程序的异常处理
  
```
python语言的程序控制有三大结构：顺序结构、分支结构、循环结构
```

### 单分支结构
    
    根据判断条件结果而选择不同的向前路径的运行方式
                               |
    if <条件> ：                |       False     
                           -----------————
       <语句块>             |  条件?  |    |
                           ----------     |
                        True:  |          |
                           ----------     |
                           |  语句块 |     |
                           ----------     |
                               |          |
                               | —————————
                               | 
    例 1.1：
    >> guess = eval(input())
    >> if guess == 99:                  >> if True:
    >>     print("猜对了")               >>     print("条件正确")
        
                   
### 二分支结构
    
                                       |
    if <条件> ：                        |         True   
                            ——————-----------———————
       <语句块1>            |      |  条件?  |       |
                           |       ----------       |
    elif <条件> ：          |           |            |
                       ----------    ......     ----------
       <语句块2>        | 语句块1 |               | 语句块2 | 
       ......          ----------               ----------
                           |                        |
     else:
     
         <语句块N>
     
                               
                           
    例 2.1：
    >> age=3
    >> if age>= 18:                   if True:
    >>     print('adult')                 print('语句块1')
    >> else:                          else:
    >>     print('teenager')              print('语句块2')
    
    紧凑形式：适用于简单表达式的二分支结构
    
    <表达式1> if <条件> else <表达式2>
    
    >> guess = eval(input())
    >> print('True') if guess ==99 else print('False')
    
    eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    >> eval('2 + 2')
    4
    
    
### 多分支结构
    
                                |
    if <条件> ：                 |          
                           ----------- True  -----------——————
       <语句块1>            |  条件1?  |—————>|  语句块1 |      |
                           ----------        -----------      |
    else <条件> ：        False |                              |
                            .......                           |
       <语句块2>          False |                              |
                           -----------       ----------       |
                           | 条件N-1? |—————>| 语句块N-1|—————>| 
                           -----------       ----------       |
                         False |                              |
                           -----------                        |
                           | 语句块N |                         |
                           ----------                         |
                               |<—————————————————————————————|
    
    
    if语句执行有个特点，从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，因此：
    
    - 注意多条件之间的包含关系
    
    - 注意变量取值范围的覆盖
    
    例 3.1：
    >> score= eval(input())
    >> if score>= 60:                   
    >>     grade = 'D'                
    >> elif score >= 70:                          
    >>     grade = 'C'    
    >> elif score >= 80:                          
    >>     grade = 'B'              
    >> elif score >= 90:                          
    >>     grade = 'A'     
    
    


### 条件判断及组合

操作符

|操作符|数学符号|   描述   |
|-----|-------|----------|
| <   |  <    |  小于    |
| <=  |  ≤    |  小于等于 |
| >=  |  ≥    |  大于等于 |
| >   |  >    |  大于    |
| ==  |  =    |  等于    |
| !=  |  ≠    |  不等于   |

条件组合

| 操作符及使用 |         描述           |
|------------|------------------------|
|  x and y   |  两个条件x和y的逻辑 与    |
|  x or y    |  两个条件x和y的逻辑 或    |
|  not x     |  条件x的逻辑 非          |


    and 表达式
    
    and表达式是由 左表达式 和 and关键字 右表达式 构成（left-expression and right-expression）
    
    求值的规则是,先对左表达式求值：
    如果左表达式的值是“假”，and表达式的值就是左表达式的值，不管右表达式
    如果左表达式的值是“真”，就继续对右表达式求值，and表达式的值就是右表达式的值

    a and b and c
    从左到右演算表达式的值，如果所有值都为真，那么 and 返回最后一个值
    如果其中某个值为假，则 and 返回第一个假值


    or 表达式
    
    or表达式的求值的规则,也是先对左表达式求值：
    如果左表达式的值是“假”，就继续对右表达式求值，整个or表达式的值就是右表达式的值
    如果左表达式的值是“真”，整个or表达式的值就是左表达式的值，不管右表达式    

    a or b or c
    左到右演算表达式的值，如果所有的值都为假，or 返回最后一个假值
    如果其中某个值为真，则 or 返回第一个真值，然后忽略剩余的比较值
    
    例 4.1：
    >> 10 and 20
    20            #从左往右，and的左边为True时，继续计算右表达式，返回右边的值
    
    >> 0 and 20
    0             #从左往右，and的左边为False时，直接返回左边的值 
       
    >> 10 or 20
    10            #从左往右，or的左边为True时，直接返回左边的值
    
    >> 0 or 20
    20            #从左往右，or的左边为False时，继续计算右表达式，返回右边的值
    
    >> 3 or 9 and 4   
    3              #从左往右，or的第一个为真，返回第一个值
    
    >> (3 or 9) and 4
    4              #(3 or 9)是一个整体，先计算得到True，and的左边为True时，返回右边的值
    


### 程序的异常处理

    >> num = eval(input("请输入一个数字："))
    >> print(num**2)
    当用户没有输入数字时，报错：
    Traceback(most recent call last):
      File "t.py",line 1, in <module>    #异常发生的代码行数
        num = eval(input("请输入一个数字："))
      File "<string>", line 1, in <module>
    NameError:name 'abc' is not defined
    #异常类型                异常内容提示
    
    5.1 异常处理的基本使用

    try:              try:
        <语句块1>          <语句块1>
    except :          except <异常类型> :
        <语句块2>          <语句块2>    
       
    例 5.1.1：
  
    try:                                          try:
        num = eval(input("请输入一个数字："))           num = eval(input("请输入一个数字：")) 
        print(num**2)                                 print(num**2)
    except :                                      except NameError :     
        print("输入不是整数")                           print("输入不是整数")
                                                  #标注异常类型后，仅响应此类异常，异常类型的名字等同于变量名 
    
    5.2 异常处理的高级使用
    
    try:
        <语句块1>
    except:
        <语句块2>
    else:
        <语句块3>             # else 对应的语句块3 在不发生异常时执行
    finally:
        <语句块4>             # finally对应的语句块4 一定会执行
    
    例 5.2.1：
    
    try:
        print('try...')
        r = 10 / int('2')
        print(r)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    else:
        print('no error')
    finally:
        print('end')
        
    - 如果没有错误发生，except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）
    - 错误有很多种类，如果发生了不同类型的错误，可以有多个except来捕获不同类型的错误
    - 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
    
    Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
    
    例 5.2.2：
    try:
        foo()
    except ValueError as e:
        print('ValueError')
    except UnicodeError as e:
        print('UnicodeError')
    
    第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了
    
   
    使用try...except捕获错误有个的好处：跨越多层调用
    
    def foo(s):
        return 10 / int(s)
    def bar(s):
        return foo(s) * 2
    def main():
        try:
            bar('0')
        except Exception as e:
            print('Error:', e)
        finally:
            print('finally...')
    
    函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时只要main()捕获到了，就可以处理。
    不需要在每个可能出错的地方去捕获错误，在合适的层次去捕获错误就可以，就大大减少了写try...except...finally的麻烦
    
    
    5.3 调用栈
    
    出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

    如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py    
    # err.py:
    def foo(s):
        return 10 / int(s)
    def bar(s):
        return foo(s) * 2
    def main():
        bar('0')
    main()

    执行，结果如下：
    $ python3 err.py
    Traceback (most recent call last):
      File "err.py", line 11, in <module>
        main()
      File "err.py", line 9, in main
        bar('0')
      File "err.py", line 6, in bar
        return foo(s) * 2
      File "err.py", line 3, in foo
        return 10 / int(s)
    ZeroDivisionError: division by zero
    
    出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：
    
    错误信息第1行：
    Traceback (most recent call last):
    告诉我们这是错误的跟踪信息。
    第2~3行：
      File "err.py", line 11, in <module>
        main()
    调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行：
      File "err.py", line 9, in main
        bar('0')
    调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
      File "err.py", line 6, in bar
        return foo(s) * 2
    原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
      File "err.py", line 3, in foo
        return 10 / int(s)
    原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
    ZeroDivisionError: integer division or modulo by zero
    根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，int(s)返回0，在计算10/0时出错，至此，找到错误源头。
    
        
    5.4 记录错误

    Python内置的logging模块可以非常容易地记录错误信息，把错误堆栈打印出来，同时，让程序继续执行下去：

    # err_logging.py
    import logging
    def foo(s):
        return 10 / int(s)
    def bar(s):
        return foo(s) * 2
    def main():
        try:
            bar('0')
        except Exception as e:
            logging.exception(e)
    main()
    print('END')

    同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
    $ python3 err_logging.py
    ERROR:root:division by zero
    Traceback (most recent call last):
      File "err_logging.py", line 13, in main
        bar('0')
      File "err_logging.py", line 9, in bar
        return foo(s) * 2
      File "err_logging.py", line 6, in foo
        return 10 / int(s)
    ZeroDivisionError: division by zero
    END

    通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
    
    
    5.5 抛出错误

    错误是class，捕获一个错误就是捕获到该class的一个实例。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
    如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
    # err_raise.py
    class FooError(ValueError):
        pass
    def foo(s):
        n = int(s)
        if n==0:
            raise FooError('invalid value: %s' % s)
        return 10 / n
    foo('0')

    执行，可以最后跟踪到我们自己定义的错误：
    $ python3 err_raise.py 
    Traceback (most recent call last):
      File "err_throw.py", line 11, in <module>
        foo('0')
      File "err_throw.py", line 8, in foo
        raise FooError('invalid value: %s' % s)
    __main__.FooError: invalid value: 0

    只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

    最后，我们来看另一种错误处理的方式：
    # err_reraise.py
    def foo(s):
        n = int(s)
        if n==0:
            raise ValueError('invalid value: %s' % s)
        return 10 / n
    def bar():
        try:
            foo('0')
        except ValueError as e:
            print('ValueError!')
            raise
    bar()

    在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了。
    捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

    raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')
    只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。    
    

    Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
    https://docs.python.org/3/library/exceptions.html#exception-hierarchy
        
    
    



### 附录


https://www.liaoxuefeng.com/wiki/1016959663602400/1017598873256736



    
    
  

