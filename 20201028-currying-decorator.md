# Currying & Decorator

### currying

    currying（科里化）
    是将多参数的函数，转化为只接受一系列单个参数的函数的过程
    新的函数就是原有函数的 curried form
    
    eg.1                        
    def de_power(x,n):   # 多参数函数    
        p = 1
        for _ in range(n):
            p *= x
        return p
    
    def powc(x):        # 科里化后的 单参数函数
        def f(n):
            p = 1
            for _ in range(n):
                p *= x
            return p
        return f

    de_power(2,3) == powc(2)(3)
        
    eg.2    
    def de_divmod(x,y):
        return x//y, x % y

    def divmodc(x):
        def f(y):
            return x//y, x % y
        return f
    de_divmod(15,7) == divmodc(15)(7)
    
    eg.3
    def f1(x,y):
        return x // y

    def f1c(x):
        def g1(y):
            return x // y
        return g1
    f1(5,2) == f1c(5)(2)       


### decorator

    
