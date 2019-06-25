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

2.1 查找：  string.find(),  string.index(),  string.rfind(),  string.rindex() 
    
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
    
    2.1.3 string.rfind(), string.rindex() 分别与 string.find(), string.index() 类似，只是从右边开始查找。 

2.2 计数：  string.count() 

    str.count(sub, start= 0,end=len(string))
    
    返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    >> "crystalapril".count('a')
    2
    
2.3 连接：  string.join(sequence)

    以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    >> seq = ("c","r", "y", "s", "t", "a", "l") 
    >> '-'.join( seq )
    'c-r-y-s-t-a-l'
    >> ''.join( seq ))
    'crystal'
    
2.4 分隔： string.split(),  string.splitlines(),  string.partition(),  string.rpartition()  
    
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
    
        
2.5 替换：  string.replace(),  string.maketrans(),  string.translate() 
    
    2.5.1 string.replace(old, new[, max])
    
    replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
    >> str1 = "my name is april"
    >> str1.replace("april", "crystal")
    'my name is crystal'
    >> str2 = "april is too diligent....wow!!!"
    >> str2.replace("il", "cc", 3)
    'aprcc is too dccigent....wow!!!'
    
    2.5.2 string.maketrans()，string.translate()通常结合起来使用
    
    str.maketrans(intab, outtab)方法用于创建字符映射的转换表，接受两个参数，intab是需要转换的字符，outtab是转换的目标
    str.translate(table)方法根据参数table (通过 maketrans() 方法创建) 转换字符串的字符    
    >> intab = "aeiou"
    >> outtab = "12345"
    >> trantab = str.maketrans(intab, outtab)
    >> str1 = "april is too diligent....wow!!!"
    >> str1.translate(trantab)
    '1pr3l 3s t44 d3l3g2nt....w4w!!!'
     
2.6 类型判断： 字母、数字、空格

string.isnumeric(),  string.isalnum(),  string.isdecimal(),  string.isdigit(),  string.isalpha(),  string.isspace() 
    
    2.6.1 string.isalnum() 
    
    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
    >> "abc123".isalnum()        >> "abc...123".isalnum() 
    True                         False
    
    2.6.2 string.isdigit()，isdecimal()，string.isnumeric() 
    
    三个函数均为判断是否只包含数字字符，是则返回 True，否则返回 False
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
    
    2.6.3 string.isalpha()
    
    如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
    >> 'cyrstalapril'.isalpha()        >> 'cyrstal.april'.isalpha()
    True                               False
    
    2.6.4 string.isspace() 
    
    如果字符串中只包含空格，则返回 True，否则返回 False.
    >> '  '.isspace()                  >> 'apr   il'.isspace() 
    True                               False    
    
2.7.1 判断大小写：   string.istitle(),  string.isupper(),  string.islower() 

    string.istitle()     
    字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False
    >> 'April Is Eating Apple.'.istitle()     >> 'april is eating Apple.'.istitle()
    True                                      False
    
    string.isupper()
    字符串中(区分大小写的)字符都是大写，则返回 True，否则返回 False
    >> 'APRIL123'.isupper()                   >> 'April'.isupper()
    True                                      False
    
    string.islower() 
    字符串中(区分大小写的)字符都是小写，则返回 True，否则返回 False
    >> 'april123'.islower()                   >> 'April'.islower()
    True                                      False

2.7.2 更改大小写：   string.lower(),  string.upper(),  string.title(),  string.capitalize(),  string.swapcase()

    string.lower()    
    转换字符串中所有大写字符为小写
    >> 'APRIL'.lower()                 >> 'april is EATING APPLE'.lower()
    'april'                            'april is eating apple'             
    
    string.upper() 
    转换字符串中所有大写字符为大写
    >> 'april'.upper()                 >> 'april is EATING APPLE'.upper()
    'APRIL'                            'APRIL IS EATING APPLE'
    
    string.title()
    把字符串中所有单词的首个字母转化为大写，其余字母均为小写
    >> 'april'.title()                 >> 'april is EATING APPLE'.title()
    'April'                            'April Is Eating Apple'         
    
    string.capitalize()
    将字符串的第一个字母变成大写,其他字母变小写
    >> 'april'.capitalize()            >> 'april is EATING APPLE'.capitalize()
    'April'                            'April is eating apple'   
    
    string.swapcase()
    对字符串的大小写字母进行转换
    >> 'april'.swapcase()              >> 'april is EATING APPLE'.swapcase()
    'APRIL'                            'APRIL IS eating apple'
    
2.8 删除指定字符：   string.strip(),  string.lstrip(),  string.rstrip()

    2.8.1 string.strip([chars]) 
    
    用于移除字符串头尾指定的字符（默认为空格）或字符序列，只能删除开头或是结尾，不能删除中间的字符
    >> '  apri l '.strip()       >> '123april321'.strip('12')       >> '****april**is EATING*** APPLE***'.strip('*')
    'apri l'                     '3april3'                          'april**is EATING*** APPLE'  
           
    2.8.2 string.lstrip() 
    
    用于截掉字符串左边的空格或指定字符.
    >> '  apri l '.lstrip()      >> '123april321'.lstrip('12')      >> '****april**is EATING*** APPLE***'.lstrip('*')
    'apri l '                    '3april321'                        'april**is EATING*** APPLE***'    
    
    2.8.3 string.rstrip('')
    
    删除 string 字符串末尾的指定字符（默认为空格）
    >> '  apri l '.rstrip()      >> '123april321'.rstrip('12')      >> '****april**is EATING*** APPLE***'.rstrip('*')
    '  apri l'                   '123april3'                        '****april**is EATING*** APPLE'      
 
 
2.9 对齐补充：   string.ljust(),  string.rjust(),  string.center(),  string.zfill()	

    2.9.1 string.ljust(width[, fillchar])  左对齐    
          width -- 指定填充指定字符后中字符串的总长度.
          fillchar -- 填充的字符，默认为空格。
    
    返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
    >> "april is too diligent....wow!!!".ljust(40,'*')    >> "april is too diligent....wow!!!".ljust(10,'*')
    'april is too diligent....wow!!!*********'            "april is too diligent....wow!!!"
    
    2.9.2 string.rjust(width[, fillchar])  右对齐
    
    返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
    >> "april is too diligent....wow!!!".rjust(40,'*')    >> "april is too diligent....wow!!!".rjust(10,'*')
    '*********april is too diligent....wow!!!'            "april is too diligent....wow!!!"
        
    2.9.3 string.center(width[, fillchar])  字符居中
    
    返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
    >> 'april is cute'.center(30,'~')             >> 'april is cute'.center(10,'~')
    '~~~~~~~~april is cute~~~~~~~~~'              'april is cute'
    
    2.9.4 string.zfill(width)    右对齐，填充0
    
    返回指定长度的字符串，原字符串右对齐，前面填充0
    >> 'april is cute'.zfill(20)             >> 'april is cute'.zfill(10)
    '0000000april is cute'                   'april is cute'
    
    
2.10 判断前缀、后缀：   string.startswith()，string.endswith()

    2.10.1 str.startswith(substr, beg=0,end=len(string))      
	    str -- 检测的字符串。
	    substr -- 指定的子字符串。
	    strbeg -- 可选参数用于设置字符串检测的起始位置。
	    strend -- 可选参数用于设置字符串检测的结束位置。

    用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
    >> str1 = "april is too diligent....wow!!!"
    >> str1.startswith('april')      # 字符串是否以 april 开头   
    True
    >> str1.startswith('is',6)       # 从第6个字符开始的字符串是否以 is 开头
    True
    >> str1.startswith('april',2,4)     # # 从第2个字符开始到第4个字符结束的字符串是否以 april 开头
    False
    
    2.10.2 string.endswith(suffix[, start[, end]])
    	    suffix -- 该参数可以是一个字符串或者是一个元素。
	    start -- 字符串中的开始位置。
	    end -- 字符中结束位置。

    用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False
    >> str1 = "april is too diligent....wow!!!"
    >> str1.endswith('!!')
    True
    >> str1.endswith('!!',20)
    True
    >> str1.endswith('april')
    False
    >> str1.endswith('april', 0, 19)
    False
    

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
 
 
  
