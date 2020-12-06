# Virtual memory management


### Virtual memory management
    
    虚拟内存管理 Virtual memory management
    利用内存空间和外部存储空间相结合，构成一个远远大于实际内存空间的虚拟存储空间
    就是任务管理器里的进程用的内存，加起来比电脑的内存多
    
    举个例子
    打开 py，然后 open，read，一次性读完一整个大文件
    再打开另一个 py，重复 open，read
    再打开新的 py，一直重复，开很多 py 把内存占着
    是可以超出电脑的内存总量的
    计算机的内存是交叉使用的，不是一个用完了另一个用，是一个进程用一会儿
    
    假设要计算一个大文件，例如 20g 的电影，用 read()
    那么 python 就会找 windows 要内存，一直要，不够了就从其他进程里抢内存
    但是计算机的内存一共就 8g 
    
    
