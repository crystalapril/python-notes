# 字符串的函数及处理方法

###  字符串处理函数
      
|     函数及使用    |                 描述              |
| ---------------- | -------------------------------- |
| len(x)           | 返回字符串的长度                   |
| str(x)           | 任意类型x所对应的字符串形           |
| max(x)           | 返回字符串 x 中最大的字母           |
| min(x)           | 返回字符串 x 中最小的字母           |
| hex(x) 或 oct(x) | 整数x的十六进制或八进制小写形式字符串 |
| chr(x)           | x为Unicode编码，返回其对应的字符    |
| ord(x)           | x为字符，返回其对应的Unicode编码    |

    例 1.1：
    >> len('ab')      >> len('一二三456')
    2                 6
    >> str(12)        >> str([1,2])
    '12'              '[1,2]' 
    
    >> max('ab')
    'b'
    >> min('ab')
    'a'
    
    >> hex(425)
    '0x1a9'
    >> oct(425)
    '0o651' 
    
    
    chr(x),ord(x)
    
                chr(u)
              --------->
    Unicode                 单字符
              <---------
                 ord(x)         
    例 1.2：
    >> ord('A')
    65
    >> ord('中')
    20013
    >> chr(66)
    'B'
    >> chr(25991)
    '文'
    
    

 ###  字符串处理方法   

    “方法”特指<a>.<b>()风格中的函数<b>()
    
    -方法本身也是函数，但是与<a>有关，<a>.<b>()风格使用    
    -字符串或字符串变量是<a>，存在一些可用方法    
    
|                     |                     |      字符串的方法     |                     |                     | 
| --------------------|-------------------- | --------------------|---------------------|-------------------- |
| string.capitalize() | string.center()     | string.count()      | string.docode()     | string.encode()     | 
| string.endswith()   | string.expandtabs() | string.find()       | string.format()     | string.index()      |   
| string.isalnum()    | string.isalpha()    | string.isdecimal()  | string.isdigit()    | string.islower()    |
| string.isnumeric()  | string.isspace()    | string.istitle()    | string.isupper()    | string.join(seq)    |	
| string.ljust()      | string.lower()      | string.lstrip()     | string.maketrans()  | string.partition()  | 
| string.replace()    | string.rfind()      | string.rindex()     | string.rjust()      | string.rpartition() |
| string.rstrip()     | string.split()      | string.splitlines() | string.startswith() | string.strip()      |
| string.swapcase()   | string.title()      | string.translate()  | string.upper()      | string.zfill()      |


常用字符串方法

2.1 查找 string.find(),string.index(),string.rfind(),string.rindex() 
    
    2.1.1 string.find(str, beg=0, end=len(string))  
    
    检测 str 是否包含在string中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
    >> info = 'abca'
    >> info.find('bc')    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
    1
    >> info.find('a',1)   # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
    3
    >> info.find('3')    # 查找不到返回-1
    -1
    	
    2.1.2 string.index(str, beg=0, end=len(string))
    
    跟find()方法一样，只不过如果str不在字符串中会报一个异常
    >> str1 = "april is too diligent....wow!!!"
    >> str2 = "is"
    >> str1.index(str2)
    
    >> str1.index(str2, 10)
    Traceback (most recent call last):
	File "test.py", line 8, in <module>
	    print (str1.index(str2, 10))
	ValueError: substring not found
    
    2.1.3 string.rfind(),string.rindex() 分别与 string.find(),string.index() 类似，只是从右边开始查找。 

2.2 计数    string.count() 

    str.count(sub, start= 0,end=len(string))
    返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    >> "crystalapril".count('a')
    2
    
2.3 连接 string.join(sequence)

    以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    >> seq = ("c","r", "y", "s", "t", "a", "l") 
    >> '-'.join( seq )
    'c-r-y-s-t-a-l'
    >> ''.join( seq ))
    'crystal'
    
2.4 分隔 string.split(),string.splitlines(),string.partition(),string.rpartition()  
    
    2.4.1 str.split(str="", num=string.count(str))
    
    split()通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串
    >> str1 = "april is too diligent....wow!!!"
    >> str1.split( )      # 以空格为分隔符
    ['april', 'is', 'too', 'diligent....wow!!!']
    >> str1.split('p',1)  # 以 p 为分隔符，分隔 1次
    ['a', 'ril is too diligent....wow!!!']   # 分隔一次，得到2个字符串，注意分隔符 p 没有了，'april' --> 'a', 'ril'
    >> str.split('i')     # 以 i 为分隔符
    ['apr', 'l ', 's too d', 'l', 'gent....wow!!!']
    
    2.4.2 string.splitlines([keepends])
    
    splitlines() 按照行('\r','\r\n',\n')分隔，返回一个包含各行作为元素的列表。
    参数keepends默认为False，不包含换行符，如果keepends为True，则保留换行符。
    >> str1 = 'april is\n\neating peach\rhappily\r\n'
    str1.splitlines()
    ['april is', '', 'eating peach', 'happily']
    >> str2.splitlines(True)
    ['april is\n', '\n', 'eating peach\r', 'happily\r\n']
    
    2.4.3 string.partition(str)
    
    如果字符串包含指定的分隔符，则返回一个3元的元组：（分隔符左边的子串，分隔符本身，分隔符右边的子串）
    >> str1 = "crystal.april" 
    >> str1.partition(".")
    ('crystal', '.', 'april')
    
    2.4.4 str.rpartition(str) 是类似于 partition()函数,不过是从右边开始查找。
    
        
2.5 替换
    string.replace(),string.maketrans()，string.translate() 
    
    string.replace(old, new[, max])
    replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
    >> str1 = "my name is april"
    >> str1.replace("april", "crystal")
    'my name is crystal'
    >> str2 = "april is too diligent....wow!!!"
    >> str2.replace("il", "cc", 3)
    'aprcc is too dccigent....wow!!!'
    
    string.maketrans()，string.translate()通常结合起来使用
    str.maketrans(intab, outtab)方法用于创建字符映射的转换表，接受两个参数，intab是需要转换的字符，outtab是转换的目标
    str.translate(table)方法根据参数table (通过 maketrans() 方法创建) 转换字符串的字符    
    >> intab = "aeiou"
    >> outtab = "12345"
    >> trantab = str.maketrans(intab, outtab)
    >> str1 = "april is too diligent....wow!!!"
    >> str1.translate(trantab)
    '1pr3l 3s t44 d3l3g2nt....w4w!!!'
     
2.6.1 类型判断：字母、数字、空格

string.isnumeric(),string.isalnum() ,string.isdecimal(), string.isdigit(),string.isalpha(),string.isspace() 
    
    string.isalnum()  
    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
    >> "abc123".isalnum()        >> "abc...123".isalnum() 
    True                         False
    
    string.isdigit()，isdecimal()，string.isnumeric() 三个函数均为判断是否只包含数字字符，是则返回 True，否则返回 False
    三者的区别在于：     
    
    isdigit()                                                        
    True: Unicode数字，byte数字（单字节），全角数字（双字节），带圈数字    
    False: 罗马数字，汉字数字                                                    
    Error: 无                                                        
                                                                     
    isdecimal()                                                      
    True: Unicode数字，全角数字（双字节）                              
    False: 罗马数字，汉字数字，#带圈数字                                                   
    Error: byte数字（单字节）                                          
                                                                      
    isnumeric()                                                      
    True: Unicode数字，全角数字（双字节），罗马数字，汉字数字，带圈数字                
    False: 无                                                         
    Error: byte数字（单字节） 
    
    >> num = "1"  #unicode   >> num = "1" #全角    >> num = b"1" # byte
    >> isdigit()             >> isdigit()          >> isdigit()
    True                     True                  True
    >> isdecimal()           >> isdecimal()        >> isdecimal()
    True                     True                  'bytes' object has no attribute 'isdecimal'
    >> isnumeric()           >> isnumeric()        >> isnumeric()
    True                     True                  'bytes' object has no attribute 'isdecimal'
    
    >> num = 'Ⅲ' # 罗马数字  >> num ="②"  #带圈数字   >> num = "四" # 汉字
    >> isdigit()             >> isdigit()           >> isdigit()
    False                    True                   False
    >> isdecimal()           >> isdecimal()         >> isdecimal()
    False                    False                  False
    >> isnumeric()           >> isnumeric()         >> isnumeric()
    True                     True                   True
    
    string.isalpha()，如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
    >> 'cyrstalapril'.isalpha()        >> 'cyrstal.april'.isalpha()
    True                               False
    
    string.isspace() 如果字符串中只包含空格，则返回 True，否则返回 False.
    >> '  '.isspace()                  >> 'apr   il'.isspace() 
    True                               False    
    
    
    

2.7.1 判断是否大小写
    
string.swapcase(),string.lower() ,string.upper(),string.capitalize(),string.title()

    
2.7.2 变更大小写
    string.istitle() ,string.isupper() ,string.islower() 

2.8
    string.strip() ,string.rstrip() ,string.lstrip()  
    
2.9
    string.zfill(width),string.ljust() ,string.rjust()，center(width, fillchar) 	

    
2.10
    string.startswith()，string.endswith()
	
 ###  参考：Unicode编码
    
    python字符串的编码形式
    - 统一字符编码，即覆盖了几乎所有字符的编码方式，支持多个语言
    - 从0到1114111（0x10FFFF）空间，每个编码对应一个字符
    - python字符串中每个字符都是Unicode编码字符
    
    如果知道字符的整数编码，还可以用十六进制这么写str：
    >> '\u4e2d\u6587'
    '中文'

    由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
    如果要在网络上传输，或者保存到磁盘上，需要把str变为以字节为单位的bytes。
    Python对bytes类型的数据用带b前缀的单引号或双引号表示：    
    x = b'ABC'

    以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
    >> 'ABC'.encode('ascii')
    b'ABC'
    >> '中文'.encode('utf-8')
    b'\xe4\xb8\xad\xe6\x96\x87'
    >>> '中文'.encode('ascii')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
    纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
    含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
    在bytes中，无法显示为ASCII字符的字节，用\x##显示。

    反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，需要用decode()方法：
    >> b'ABC'.decode('ascii')
    'ABC'
    >> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
    '中文'

    如果bytes中包含无法解码的字节，decode()方法会报错：
    >>> b'\xe4\xb8\xad\xff'.decode('utf-8')
    Traceback (most recent call last):
      ...
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
    如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
    >>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
    '中'

 ### 附录
 
 https://www.runoob.com/python3/python3-string.html
 
 
  
