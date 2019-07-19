
    * R： reduce(lambda x,y: x+y, [1,2,3])
      W： list(reduce(lambda x,y: x+y, [1,2,3]))   # reduce 此处返回int不能加list
    
    * R： list(map1(abs,(-1,-2,3))) 
      W： list(map1(abs,(-1,-2,3))                 # 少写了括号
    
    * R： map(abs,(-1,-2,3))                       # python2
      W： list(map(abs,(-1,-2,3)))                 # python2 ，不需要list()
      
    * R: def map6(f,xs):
             l=[]
             xss = list(xs.items())
             i = 0
             while i < len(xs):
                 l.append(f(xss[i]))
                 i +=1
             return l      
      W: def map6(f,xs):                        # 忘记重要的功能map(f)，少了f      
             l=[]
             xss = list(xs.items())
             i = 0
             while i < len(xs):
                 l.append(xss[i])
                 i +=1
             return l
      
    * R:
      W:
      
    * R:
      W:
      
    * R:
      W: 
