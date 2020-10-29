# Currying & Decorator

### currying

    currying（科里化）
    是将多参数的函数，转化为只接受单参数函数的过程
    
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
        
    eg.2
    


### decorator
