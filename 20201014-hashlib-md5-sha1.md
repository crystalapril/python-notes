# hashlib - md5 & sha1

### method

    users 从网站下载程序的安装文件之后，需要验证，防止文件盗版，被篡改，或者不完整    
    验证方式主要有计算：md5, sha1, sha256 等
    
    linux 里面有软件仓库，一般认为可以放心使用
    同时，md5sum, sha1sum, sha256sum这些也是仓库的标配， 可以直接计算
    
    windows 没有软件仓库，需要自己计算
    
    计算方法：
    
    1.如果网站有提供 sha1，sha256，可以将文件下载下来，用 7zip 或 win自带的 CRC SHA 去计算，看是否一致
    
    2.如果网站只提供了 md5， 7zip 无法计算，可以找一个受信任的，可以计算 md5 的软件，来校验
     
      比如用已安装的 python 的 hashlib 模块计算出 md5 
      （windows 自带的 powershell 也能计算 md5，但是不太好用）
    

### python calculate

    >>> import hashlib
    
    >>> m5 = hashlib.md5(open(r'C:\Users\Desktop\python-3.9.0-amd64.exe','rb').read()).hexdigest()
    >>> pm5 = 'b61a33dc28f13b561452f3089c87eb63'  # from official website
    >>> print(True) if m5 == pm5 else print(False)
    True
    
    >>> sh1 = hashlib.sha1(open(r'C:\Users\Desktop\python-3.9.0-amd64.exe','rb').read()).hexdigest().upper()
    >>> psh1 = '5F29E7B435E0A08830B350F7388337D8B761BF72'  # from win 7zip
    >>> print(True) if sh1 == psh1 else print(False)
    True
    
    
### md5 & sha1 etc.
    
    md5
    MD5信息摘要算法 (MD5 Message-Digest Algorithm)    
    md5 就是一段信息的摘要，具体来说，就是一串字节 byte 的摘要，任何字节都可以计算出其 md5
    
    hashlib.md5()   返回一个 md5 加密算法对象，是 hash 对象
    hash.digest()   计算 hash 对象的摘要, 里面是 bytes object
    hash.hexdigest()  类似 digest() ,也是 hash 对象的摘要，是十六进制的
    
    >>> import hashlib
    >>> hashlib.md5(b'python').hexdigest()   
    '23eeeb4347bdd26bfc6b7ee9a3b755dd'   # md5 码一般 32 位
    >>> hashlib.md5(b'').hexdigest()
    'd41d8cd98f00b204e9800998ecf8427e'
    
    SHA-1
    英语：Secure Hash Algorithm 1，中文名：安全散列算法1
    其实 sha1 也是一堆字节的摘要
    >>> hashlib.sha1(b'').hexdigest()
    'da39a3ee5e6b4b0d3255bfef95601890afd80709'  # sha1 码一般 40 位

    而可执行文件的内容，比如python.exe 的内容也是 byte，自然就可以计算 md5，sha1 等，得到一段摘要，又或者叫 指纹
    通过比对2个文件的摘要，来推测，文件是否一样
    注意， 计算 md5 的输入是文件的内容，而不是文件名，文件名不管怎么变换，内容不变，得到的 md5 是同一个
    

### getattr

    也可以用 getattr 函数来获取 md5 & sha1 码
    注: getattr() 函数用于返回一个对象属性值
    
    >>> getattr(hashlib,'sha1')(b'').hexdigest()
    'da39a3ee5e6b4b0d3255bfef95601890afd80709'
    
    那么可以把上面的程序，改写成为可以用 命令行灵活调用的 md5_sha1.py 文件
    
    >>> import hashlib,sys
    >>> addr = sys.argv[1]
    >>> code = sys.argv[2]

    # verify md5, sha1 ,etc.
    >>> def co_type(code):
            if len(code)== 32: return 'md5'
            elif len(code) == 40: return 'sha1'
            elif len(code) == 64: return 'sha256'
    >>> def cal(addr,code):
            # getattr(hashlib,co_type) = hashlib.co_type, 如 hashlib.md5 得到一个计算 md5 的函数
            ca_code = getattr(hashlib,co_type(code))(open(addr,'rb').read()).hexdigest()
            print(ca_code.lower() == code.lower())

    >>> cal(addr,code)
    
### hash.update

    如果需要运算 md5 、sha1 的文件特别大怎么办，可能读取的时候，就没办法一口气读完
    
    update() 可以接收分批传过来的数据
    m.update(a); m.update(b) is equivalent to m.update(a+b)
    
    例如：
    >>>md = hashlib.md5()       
    >>>md.update(b'calculate ')    # 先传入一部分 data
    >>>md.update(b'hashlib md5')
    >>>md5_1 = md.hexdigest()
    >>>md5_2 = hashlib.md5(b'calculate hashlib md5').hexdigest()  # 一次性传入data
    >>>md5_1 == md5_2            # 分批传入和 一次性传入计算出来的 md5 是一样的    
    True
    
    那么我们改进一下计算 sha1 的程序 sha.py
    
    import sys,pyperclip,hashlib,os
    # get sha code from outside
    whole = pyperclip.paste()         # 用 pyperclip 来获取外部的 sha1
    whole_split = whole.split(' ')    # 外部的数据 大概长这个样子 SHA1:K234FA...JLUA23F，所以需要只取后半部分
    sha_paste = whole_split[1].strip().lower()
    # calculate sha code of file
    addr = sys.argv[1]                # 获取文件地址
    file = open(addr, 'rb')           # 把文件传给 file 对象，注意，只要不read()，就不会产生大的内存消耗
    sha = hashlib.sha1()              # 创建一个计算 sha1 的hash 对象
    size = os.stat(addr).st_size      # 通过 os.stat() 获取文件的内容，包括创建时间等，这里 st_size 就是文件的大小
    while data := file.read(1024):    # 注意read()，是可以分批读取的，这样可以降低内存的使用，data 读取完之后就没有了，就剩 b''           
        sha.update(data)              # 分批接收 read() 传过来的数据，并且累加，但是不会占太多内存 
    sha_calcu = sha.hexdigest().lower()     # 最后计算 update() 收到的所有的 bytes，计算 sha1 的摘要
    # compare
    addr_split = addr.split('\\')
    print(addr_split[-1]+' sha1'+ ':'+ sha_calcu)
    print(sha_paste)
    print(sha_paste == sha_calcu)  
    
    
### ：= Assignment expressions
    
    我们看到上面 sha.py 中的 while data := file.read(1024): 这个句
    表达的意思是，将 file.read(1024) 赋值给data ，然后判断 data 是否为真，如果是，while True: 运行下面的代码
        
    :=  是 Assignment expressions（赋值表达式），又叫做海象运算符
    python3.8 以后发布的
    以前的 python ，赋值就必须是单独的一句，不能跟其他表达式混合
    如 ，data = file.read(1024)
    赋值后的 data 再带入到 while data:  ，然后进行条件判断    
    有了赋值表达式之后，while data := file.read(1024)，一句话完成了赋值和条件判断，要简洁很多
        
    while data := file.read(1024):
        sha.update(data)
    
    把上面的 while 语句，改成 for 的话，也可以写成：
    for data in iter(lambda: read.(size),b''):
        sha.update(data)
        
    这个 for 语句等价于：
    iterable = iter(lambda: file.read(size), b'')      # 例如 list是 iterable
    iterator = iter(iterable)                          # 通过 iter() 将list 转换成 iterator, 就可以使用 next() 了
    try:
        while True:
            data = next(iterator)
            sha.update(data)
    except StopIteration:
        pass
        
    注意这里 lambda: read.(size) 就相当于一个无参数的函数，等同于：
    def g():
        return read.(size)
    
    
### os.stat

    sha.py 中出现了一个 os.stat(addr).st_size  
    
    os模块是 operating system 的缩写
    os.stat() 用于获取文件的内容
    eg.
    >>>import os
    >>>os.stat(r'E:\python\ideal\sha.py')
    os.stat_result(st_mode=33206, st_ino=844424930144477, st_dev=2023566340, st_nlink=1, st_uid=0, \
    st_gid=0, st_size=927, st_atime=1606699983, st_mtime=1606896282, st_ctime=1606806140)
    这里st_atime， st_mtime 都是表示时间的属性，比如某个时间到创建文档这个期间的秒数，需要换算一下，得到创建时间

    
    
    
    
    
