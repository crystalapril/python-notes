# Note of Automate the Boring Stuff

### 1.basic


### 2.flow control


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

