# map filter 

 - map
 - filter

 
 要点：
 1. python3 的map filter reduce ，返回的是迭代器，python2里返回的是list
 2. for all F(x),[F(x) for x in xs] == map(lambda x: F(x), xs)
    例如：
    [0 for x in xs]  == map(lambda x: 0, xs)
 3. for all P(x), [x for x in xs if P(x)] == filter(lambda x: P(x), xs)
 4. for all F(x) and P(x) , [F(x) for x in xs if P(x)]
 
