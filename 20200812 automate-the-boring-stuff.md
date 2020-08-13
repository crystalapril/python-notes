# Note of Automate the Boring Stuff

### 1.basic

    1.1 operator
    1.1.1 // , %
    1.1.2 * ，只能用于2数字，或str和一个整数， 错误： 'Alice' * 5.0
    
    1.2 assignment statement
    把变量想象成一个贴了标签的盒子，value的reference放在了盒子里
    
    1.3 variable name : 
    no hyphens (连字符)，不能以数字开头，不能有特殊符号如￥
    
    1.4 int function:     
    正确： int(99.99)
    正确： int('99')
    错误： int('99.99')
    
    1.5 数字前可以加0 ，正确： 42.0 == 0042.000
   

### 2.flow control

    2.1 can't assign to keyword ，布尔值不可以被赋值， 错误： True = 2 + 2
    
    2.2 and, or, not  
    
    2.3 break, continue


### 3.function

    3.1 print() returns None

    3.2 the Call Stack ： 
    stack-like structure 先进后出
    the current topic is always at the top of the stack

    3.3 local and global scope
    3.3.1 global scope : global variable
    3.3.2 global statement : global variable
    3.3.3 function and assignment statement: local variable 
    3.3.4 function and without assignment statement : global variable  
    
    3.4  sys.exit()


### 4.list
    
    4.1 index 必须整数，错误：alist[1.0]

    4.2 multiple assignment 个数必须一致
    正确： size, color, disposition = ['fat', 'gray', 'loud']  
    错误： size, color, disposition, name = ['fat', 'gray', 'loud']  
    
    4.3 random.choice(),random.shuffle()

    4.4 alist.sort()   
    4.4.1 默认情况下，Z(大写) 排在  a（小写） 前面
    4.4.2 alist.sort() : return None , 只用于list, sort list in place 当场修改原list
          sorted(list) ：return new list
    
    4.5 \ line continuation character 
    
    4.6 mutable: list , dict  ; immutable : integer, string, tuple
        
    4.7 overwritten ： 下面例子，没有修改eggs 这个list：
        >>> eggs = [1, 2, 3]
        >>> eggs = [4, 5, 6]
        
        modify： 下面这个例子，才是修改了eggs，这个list：
        >>> eggs = [1, 2, 3]
        >>> del eggs[2]     >>> del eggs[1]     >>> del eggs[0]
        >>> eggs.append(4)  >>> eggs.append(5)  >>> eggs.append(6)
        原因在于，我们赋值的时候，假设 variable是个盒子，这个盒子里，装的不是list本身，而是存放list的地址这个链接reference
        第一个例子，eggs 被装进了新的 reference，跟新的list关联上了，原有的list没有被修改，只是跟eggs取关

