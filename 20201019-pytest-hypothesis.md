# pytest & hypothesis

### pytest & hypothesis

    pytest 是 python 下的一个第三方测试工具，是一种 test runner
    类似于 unittest，但是比 unittest 好用的多
    
    hypothesis 是 python 的第三方库，主要用于随机生成大量测试数据
  
    pytest 与 hypothesis 通常结合起来进行测试工作
    注： pytest 可以单独使用
        hypothesis 必须与 pytest 或其他的 test runner 一起使用
    
    cmd 运行测试方法：
    pytest py_test.py
    pytest py_test.py::test_commutative   # 测试 py_test.py 中的 test_commutative 函数
    pytest -v py_test.py::test_commutative  # -v， --verbose ，显示测试的细节
    
    
    测试文件举例：
    eg. 
    import math
    from hypothesis import given
    from hypothesis.strategies import integers

    1.given 
    eg1.：
    @given(integers(min_value = 1, max_value =10000), integers(min_value = 1, max_value =10000))
    def test_commutative(x, y):
        assert math.gcd(x,y) == gcd(x,y)
        
    # intergers: 给出的参数为整数， min_value  限定参数最小值， max_value 限参数最大值
    
    2. setting
    eg2.：
    def log(n):
        return math.log10(n) / 10
    
    def sleep(n):
        time.sleep(log(n))
    
    @settings(deadline = 300)
    @given(integers(min_value = 1))
    def test_deadline300(x):
        sleep(x)
    
    
    
    3. parametrize
    
    eg3.：

    
    def test_unrolling():
        assert log(    10) == 0.1
        assert log(   100) == 0.2
        assert log(  1000) == 3.0
        assert log( 10000) == 0.4
        assert log(100000) == 5.0
    
    # 不管 def f（）: 下的 assert 有多少个，test 只被认为是一个    
    
    
    



