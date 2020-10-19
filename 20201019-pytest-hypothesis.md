# pytest & hypothesis

### brief introduction

    pytest 是 python 下的一个第三方测试工具，是一种 test runner
    类似于 unittest，但是比 unittest 好用的多
    
    hypothesis 是 python 的第三方库，主要用于随机生成大量测试数据
  
    pytest 与 hypothesis 通常结合起来进行测试工作
    注： pytest 可以单独使用
        hypothesis 必须与 pytest 或其他的 test runner 一起使用
    
### running method

    cmd 运行命令行（pycharm 的 terminal 也行）：
    
    pytest py_test.py
    pytest py_test.py::test_commutative   # 测试 py_test.py 中的 test_commutative 函数
    pytest -v py_test.py::test_commutative  # -v， --verbose ，显示测试的细节
    
    
### test file example
    
    eg. 
    >>> import math
    >>> from hypothesis import given
    >>> from hypothesis.strategies import integers

    1.given 
    eg1.：
    >>> @given(integers(min_value = 1, max_value =10000), integers(min_value = 1, max_value =10000))
    >>> def test_commutative(x, y):
            assert math.gcd(x,y) == gcd(x,y)
        
    # intergers: 给出的参数为整数， min_value  限定参数最小值， max_value 限参数最大值
    
    注： hypothesis 的报错，一般会尽量找会出错的值里面，最小的那几个
         hypothesis 在发现错误之后，会尝试把数据不断缩小，直到把接近临界点的错误值找出来 
    
    2. setting（deadline， max_examples）
    eg2.：
    >>> def log(n):
            return math.log10(n) / 10
    
    >>> def sleep(n):
            time.sleep(log(n))
    
    >>> @settings(deadline = 300)
    >>> @given(integers(min_value = 1))
    >>> def test_deadline300(x):
            sleep(x)
        
    hypothesis 为了避免运行实现过长，设置了一个 deadline ，默认就是 200 ms（1000 毫秒 = 1秒 ）
    (一般情况下，实际会略小于 250 ms，设限制的 1.25倍左右 ，如果限制是 300 ms， 实际运行会略小于 375ms，也就是允许超过 25%，
    current_deadline = ( current_deadline // 4) * 5 )
    通过 set deadline 来解决超时的问题，比如 deadline = 300，或者 deadline = None
    
    除了 deadline ，缩小样本，也可以解决超时的问题
    eg3.:
    >>> @given(integers(min_value = 1, max_value = 100))   # 限制样本取值的范围
    >>> def test_100(x):
            sleep(x)
    
    >>> @settings(max_examples = 20)     # 限制取样的个数，如只能取 20个
    >>> @given(integers(min_value = 1, max_value = 200))
    >>> def test_200(x):
            sleep(x)
    
    3. parametrize
    
    eg4.：    
    def test_unrolling():
        assert log(    10) == 0.1
        assert log(   100) == 0.2
        assert log(  1000) == 3.0
        assert log( 10000) == 0.4
        assert log(100000) == 5.0
    
    # 不管 def f（）: 下的 assert 有多少个，test 只被认为是一个    
    
    
    



