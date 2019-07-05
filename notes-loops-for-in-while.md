# 循环结构

  - 遍历循环
  - 无限循环
  - 循环保留字
  - 循环的高级用法
  
### 遍历循环

    1.1 遍历某个结构形成的循环运行方式
    
            <------------
            |           |
    for <循环变量> in <遍历结构>:
            |
        <语句块>
        
    - 从遍历结构中逐一提取元素，放在循环变量中
    - 由保留字for和in组成，完整遍历所有元素后结束
    - 每次循环，所获得的元素放入循环变量，并执行一次语句块
    - 包括：计数循环（N次）、计数循环（特定次）、字符串遍历循环、列表遍历循环、文件遍历循环
    
    
    1.2 计数循环（N次）
    
    for i in range(N):
    
        <语句块>
        
    - 遍历由range()函数产生的数字序列，产生循环
    
    >> for i in range(5):      >> for i in range(5):
           print(i)               print("hello:",i)
    0                          Hello:0
    1                          Hello:1
    2                          Hello:2
    3                          Hello:3
    4                          Hello:4
    
    
    1.3 计数循环（特定次）
    
    for i in range(M,N,K):
    
        <语句块>
        
    - 遍历由range()函数产生的数字序列，产生循环
    
    >> for i in range(1,6):      >> for i in range(1,6,2):
           print(i)                  print("hello:",i)
    0                            Hello:1
    1                            Hello:3
    2                            Hello:5
    3                         
    4                        
    5
    
    
    1.4 字符串遍历循环
    
    for x in s:
        
        <语句块>
        
    - s是字符串，遍历字符串每个字符，产生循环
    
    >> for c in "Python123":
          print(c,end=",")
    P,y,t,h,o,n,1,2,3
    
    
    1.5 列表遍历循环    
    
    for item in ls:
        
        <语句块>
        
    - ls是一个列表，遍历其每个元素，产生循环
    
    >> for item in [123,"PY",456]:
           print(item,end=",")
    123,PY,456
    
    1.6 文件遍历循环
    
    for line in fi:
    
        <语句块>
        
    - fi是一个文件标识符，遍历其每行，产生循环
    
    >> for line in fi:
           print(line)
    优美胜于丑陋
    简洁胜于复杂
  
  
### 遍历循环

    由条件控制的循环运行方式
    
    while <条件>：
            |
            <-- <语句块>
        
    - 反复执行语句块，直到条件不满足时结束
    
    无限循环的条件
    
    
    
    
    
     
    
    
    
    
    
    
    
