# decimal & fractions module

### floating point arithmetic

    浮点数在计算机里，经常会出现误差，例如：
    >>> 0.1
    0.1000000000000000055511151231257827021181583404541015625     # 0.1 在计算机中的真实近似值
    
    这是因为，我们日常使用的小数是十进制的，例如： 0.125 = 1/10 + 2/100 + 5/1000
    而计算机中的计算是二进制的， 0/2 + 0/4 + 1/8
    大部分的十进制的分数，不能被二进制分数，精确的表示，就会出现误差    
    
    计算机中 1/10 的二进制分数实际上是 3602879701896397 / 2 ** 55
    
    在python 中解决 floating point error 有一些简单的方法
    
    format   # 给出指定精度的分数
    >>> format(math.pi, '.12g')  # give 12 significant digits
    '3.14159265359'    
    
    float.as_integer_ratio      # 把分数转化成 2 个整数的比率
    >>> x = 3.14159
    >>> x.as_integer_ratio()
    (3537115888337719, 1125899906842624)
    
    除此以外，还有2个模块 decimal module 和 fraction module， 可以处理这个问题
    

### decimal module

    decimal module 可以让计算结果，与数学计算结果一致
    
    例如： 
    >>> 1.1 + 2.2
    3.3000000000000003     # 二进制浮点数
    
    >>> import decimal
    >>> decimal.Decimal('1.1')+decimal.Decimal('2.2')
    Decimal('3.3')
    >>> getcontext().prec(28)     # 指定精度，可达
    >>> decimal.Decimal(1)+decimal.Decimal(7)
    Decimal('0.1428571428571428571428571429')       
    

### fractions module

    fractions module 可以对有理数进行运算，将有理数表现为 2个整数的 ratio
    
    [sign] numerator ['/' denominator]
    
    >>> from fractions import Fraction
    >>> Fraction('7e-6')
    Fraction(7, 1000000)
    >>> Fraction('-.125')
    Fraction(-1, 8)    
    
    Fraction.from_float()
    Fraction.from_decimal()
    Fraction.limit_denominator()
      
    


### 附录

    https://docs.python.org/3/tutorial/floatingpoint.html
    
