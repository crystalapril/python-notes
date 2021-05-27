# decimal & fractions module

### floating point arithmetic

    浮点数在计算机里，经常会出现误差，例如：
    >>> 0.1
    0.1000000000000000055511151231257827021181583404541015625     # 0.1 在计算机中的真实近似值
    
    这是因为，我们日常使用的小数是十进制的，例如： 0.125 = 1/10 + 2/100 + 5/1000
    而计算机中的计算是二进制的， 0/2 + 0/4 + 1/8
    大部分的十进制的分数，不能被二进制分数，精确的表示，就会出现误差    
    
    计算机中 1/10 的二进制分数实际上是 3602879701896397 / 2 ** 55
    
    在python 中解决 floating point error 有2 个办法，一个是 decimal module，另一个是 fraction module
    

### decimal module

    

### fraction module




### 附录

    https://docs.python.org/3/tutorial/floatingpoint.html
    
