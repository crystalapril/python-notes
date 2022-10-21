# Note of Automate the Boring Stuff

### 1.Basic

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
   

### 2.Flow Control

    2.1 can't assign to keyword ，布尔值不可以被赋值， 错误： True = 2 + 2
    
    2.2 and, or, not  
    
    2.3 break, continue


### 3.Function

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
    
    3.5 variable-length number of arguments with *args and **kwargs
    f(*args) , 其实是 <expr>(*<expr-arg>)
    args 是表达式，可以是变量表达式，如 *xs，也可以是其他的expression，如 *xs[i]下标表达式等
    
    *args 会作为 tuple 被传入f中， * 的作用是将后面的 args 一一展平
    如 f(*(x1,x2,x3))== f(x1,x2,x3)
       f(*([x0] + [x1] + [x2]))  == f(x1,x2,x3)


### 4.List
    
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
        
    4.8 id()
    
    4.9 copy.copy(), copy.deepcopy()

    4.10 in
         错误： 1 or 2 in [4,5,6]
         正确： 1 in [4,5,6] or 2 in [4,5,6]
         
         留意：有些语言中 0 < x < 100 是不行的，必须 0 < x and x < 100 ，不过python没有这个问题
         
    
    
### 5.Dictionaries and Structuring Data

    5.1 unodered，字典是无序的
    相同的key-value pair, 不同的order, 字典的值相等
    
    5.2 python3.7之后，从dict里取出的key的list，保留原来的 'key' 的顺序
    >>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
    >>> list(eggs)
    ['name', 'species', 'age']
    
    5.3 d.keys(),d.values(),d.items() 返回dict_keys, dict_values, and dict_items （不是 list）
    可以用for loop，list()
    
    5.4 dict.get(key,defualt), dict.setdefualt(key,defualt)
    
    5.5 pprint.pprint()
 
 
 ### 6.Manipulating Strings

    6.1 escape character, raw string
    
    6.2 >>> '' in 'april'
        True
        
    6.3 f-string, % , format

    6.4 str.method   
        6.4.1 str.lower()    , str.upper()    不修改原str，返回新的
              str.isupper()  , str.islower()  至少有一个字母，所有的字母大写（小写），return True
              eg.   >>> '12345'.islower()     >>> '12345'.isupper()          >>> '12abc'.islower() 
                    False                     False                             True                     

        6.4.2 split(), partition()
        6.4.3 rjust(), ljust(), center() | rstrip(),lstrip(),strip()  除了删除两端的 space，也可以删除 character
     
    6.5 ord(), chr()
 
 
### 7.Pattern Matching with Regular Expressions

    7.1 re模块    
    7.1.1 re.compile()， 返回 Regex Objects 
    7.1.2 re.search() ，返回 Match object of the first matched text 
    7.1.3 re.group(), re.groups() 
    7.1.4 re.findall()， 返回 list of strings of every match
          string 没有 group的时候，返回 [s1,s2]；有group的时候，返回[(s1,s2),(s3,s4)]   
          re.finditer() , 返回 iterator
    7.1.5 re.sub(str1,str2) ，替换，str1 替换 str2 里面与 regex 匹配的内容
    7.1.6 re.DOTALL ，让 . (dot character)可以匹配一切字符，包括换行符
    7.1.7 re.IGNORECASE , re.I ，case-insensitive
    7.1.8 re.VERBOSE, 可用于多行，并且忽略注释&空格
          someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)  # 联合使用    
    
    7.2 escape characters \
    
    7.3 | pipe 表示 or ，A|B 等同于 A 或 B 都可以
    
        那么，想要表示 and怎么办，我们可以用 (?=A expr)(?=B expr) 
        non-consuming regular expression         
        (?=expr)
        means "match expr but after that continue matching at the original match-point."                    
    
    7.4 匹配符号    

        ?      matches 0 or 1 
        *      matches 0 or more 
        +      matches 1 or more 
        {n}    matches exactly n ; {n,} matches n or more ; {,m} matches 0 to m ; {n,m}  matches n ~ m
        {n,m}? or *? or +? performs a non-greedy match of the preceding group.
        ^      means the string must begin with spam. （脱字符 caret character）
        $      means the string must end with spam. 
        .      matches any character, except newline characters.
        [abc]  matches any character between the brackets (such as a, b, or c).
        [^abc] matches any character that isn’t between the brackets.
        
    7.5 greedy & non-greedy
        greedy: 默认的，最大匹配  ，             r'(Ha){3,5}' 匹配 'HaHaHaHaHa'中的 'HaHaHaHaHa'
        non-greedy（后面加？）： 最小程度匹配 ，  r'(Ha){3,5}?' 匹配 'HaHaHaHaHa'中的 'HaHaHa'  
        
        *?, +?, ??, or {m,n}? 这几个后面的？ 就是非贪婪，反之就是贪婪
        如果,想表达\d{2,3}的或有，就加括号， (\d{2,3})? 或有， \d{2,3}? 非贪婪
        
        
    7.6 Character Classes
        \d  [0-9]
        \D  [^0-9]
        \w  [a-zA-Z0-9_]
        \W  [^a-zA-Z0-9_]
        \s  [\n\t\space] 
        \S  [^\n\t\space]        
   
    7.7 https://regex101.com/
        我们可以把写好的 pattern 放到 regrex 校验的网址先去校验
        对于比较复杂的 pattern，可以引入变量，拆分来写
        
        本章作业 project1 eg. ：
        day = r'(([012]\d)|(3[01]))'
        month = r'((0\d)|(1[12]))'
        year = r'([12]\d{3})'
        rdate = re.compile(rf'({day}\/{month}\/{year})')  
        # 注意，正则表达式本身没有引入变量的功能，需要用到字符串中引入变量的做法，f-string，或者 format 等
        
        如何把 rdate 放到网址中进行校验呢
        可以在交互模式中 print(rdate)，得到的结果应该就是标准的正则表达式的形式，不含变量的，然后放入网站验证
        >>>print(rdate)
        re.compile('((([012]\\d)|(3[01]))\\/((0\\d)|(1[12]))\\/([12]\\d{3}))')
        
    7.8 zero width assertions 零宽断言
        Look ahead positive (?=)    : Find expression A where expression B follows  ，A(?=B) 
        Look ahead negative (?!)   ： Find expression A where expression B does not follow: A(?!B)
        Look behind positive (?<=) ： Find expression A where expression B precedes: (?<=B)A
        Look behind negative (?<!) ： Find expression A where expression B does not precede: (?<!B)A
        
        以 'foobarbarfoo' 为例:
        bar(?=bar)     finds the 1st bar ("bar" which has "bar" after it)
        bar(?!bar)     finds the 2nd bar ("bar" which does not have "bar" after it)
        (?<=foo)bar    finds the 1st bar ("bar" which has "foo" before it)
        (?<!foo)bar    finds the 2nd bar ("bar" which does not have "foo" before it)
        
        
### 8 Input Validation

    8.1 pip install pyinputplus
    
    8.2 pyinputplus 包含以下函数：
    
    inputStr() Is like the built-in input() function but has the general PyInputPlus features.     

    inputNum(), inputInt(), and inputFloat() 输入数字，如果输入错误会提示要求输入数字    
        
    可选参数：    
    - min,   max,     greaterThan, lessThan 
     
    - limit, timeout, default 
    eg. limit=2, default='N/A'
    eg. timeout=10
     
    - allowRegexes, blockRegexes (两个同时存在时，allowRegexes override blockRegexes)
    eg. allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'], blockRegexes=[r'[02468]$']

    inputChoice() Ensures the user enters one of the provided choices

    inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

    inputDatetime() Ensures the user enters a date and time 

    inputYesNo() 输入 yes\no（也可以输入y\n，甚至自己指定eg. yesVal='ok', noVal='no'，因此可以使用外语）

    inputBool() 输入 True/False

    inputEmail() Ensures the user enters a valid email address

    inputFilepath() Ensures the user enters a valid file path and filename, 
    and can optionally check that a file with that name exists

    inputPassword() Is like the built-in input(), but displays * characters as the user types so that passwords, 
    or other sensitive information, aren’t displayed on the screen
    
    
    inputCustom() ，to perform your own custom validation logic by passing the function to inputCustom()
    eg. 自己构造 addsUpToTen() 函数，调用 inputCustom(addsUpToTen) （注意里面没有括号）
    
    
### 9 reading and writing files

    9.1 pathlib module
    
    9.2 from pathlib import Path
    
    Path 有如下功能：
    
    9.2.1 Path('spam', 'bacon', 'eggs')  --> WindowsPath('spam/bacon/eggs')
          Path(r'C:\Users\Al', filename) --> C:\Users\Al\accounts.txt
          
          myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
          for filename in myFiles:
              print(Path(r'C:\Users\Al', filename))
    
    9.2.2 str(Path('spam', 'bacon', 'eggs')) --> 'spam\\bacon\\eggs'
    
    9.2.3 Path('spam') / 'bacon' / 'eggs'       --> WindowsPath('spam/bacon/eggs')
          Path('spam') / Path('bacon/eggs')     --> WindowsPath('spam/bacon/eggs')  
          Path('spam') / Path('bacon', 'eggs')  --> WindowsPath('spam/bacon/eggs')
    
    9.2.4 r'C:\Users\Al' + '\\' + 'spam'       --> 'C:\\Users\\Al\\spam'
          '\\'.join([r'C:\Users\Al', 'spam'])  --> 'C:\\Users\\Al\\spam'
          - 但是不推荐用这个办法，因为在windows和linux里面，使用'\\'可能会因不兼容出现bug
          
          Path('C:/Users/Al')/ Path('spam')       -->  WindowsPath('C:/Users/Al/spam') 
          str(Path('C:/Users/Al')/ Path('spam'))  --> 'C:\\Users\\Al\\spam'           
          - 使用Path() 和 / 的话，不用担心切换系统问题，尽量使用 / (forward slash)
          - 注意：通过 / 来连接，前后必须都是 Path object，如果是 str的话，python会报错
    
    9.2.5 Path.cwd()  # current working directory # 查看当前目录    
    
          os.chdir('C:\\Windows\\System32')       # 切换工作目录     
    
    9.2.6 Path(r'E:/python/boring4pycharm/test').mkdir()  # 创建文件夹
          os.makedirs(r'E:/python/boring4pycharm/test/test/test')  # 可以创建一系列的中间层级的文件夹，以保证地址存在
          
    9.2.7 Path.home()   --> WindowsPath('C:/Users/april')
    
    9.2.8 .\   # 本文件夹，一般来说 .\a.txt 与 a.txt 是一回事
          ..\  # 母文件夹，eg.  ..\a.txt
          
          Path.cwd().is_absolute()   --> True   # 查看是否是绝对路径
          
    9.2.9 Path.cwd()/Path('my/relative/path')   # 显示绝对路径（前面是当前目录）
          Path.home()/Path('my/relative/path')  # 显示绝对路径（前面是家目录）
          
    9.2.10 os.path.abspath(path)         # 返回参数 path的绝对路径
           os.path.isabs(path)           # 返回 True，如果参数path是绝对路径
           os.path.relpath(path,start)   # 返回相对路径，从start到path
    
    9.2.11 eg1. 
           p = Path('C:/Users/Al/spam.txt')
           p.anchor --> 'C:\\',  p.parent --> WindowsPath('C:/Users/Al') # This is a Path object, not a string.
           p.name --> 'spam.txt',  p.stem --> 'spam',  p.suffix --> '.txt',  p.drive --> 'C:'
           
           Path.cwd().parents[0] --> WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
           Path.cwd().parents[1] --> WindowsPath('C:/Users/Al/AppData/Local/Programs')
           
           eg2.
           cpath = 'C:\\Windows\\System32\\calc.exe'
           os.path.dirname(cpath)  --> 'calc.exe'
           os.path.basename(cpath) --> 'C:\\Windows\\System32'
           
           os.path.split(cpath) --> ('C:\\Windows\\System32', 'calc.exe')
           cpath.split(os.sep)  --> ['C:', 'Windows', 'System32', 'calc.exe']           
    
    9.2.12 os.path.getsize(path)  # 返回path文件大小
           os.listdir(path)       # 返回list，里面含path中的文件名
           os.path.join()             
   
    9.3 glob patterns
        eg.
        p = Path('C:/Users/april/Desktop')
        list(p.glob('*'))      list(p.glob('*.txt'))      list(p.glob('project?.docx')      list(p.glob('*.?x?')   
    
    9.4 p.exists()   # 当地址存在时，返回True，反之，返回False
        p.is_file()  # 当地址存在，且是一个文件时，返回True，反之，返回False
        p.is_dir()   # 当地址存在，且是一个目录时，返回True，反之，返回False
    
    9.5 shelve 
        eg.
        shelfFile = shelve.open('mydata')
        shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon']
        shelfFile.close()
        
        type(shelfFile)    shelfFile['cats']    list(shelfFile.keys())    list(shelfFile.values())        
    
    9.6 pprint
        eg.
        cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
        pprint.pformat(cats)
        fileObj = open('myCats.py', 'w')
        fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
        fileObj.close()
        
        import myCats
        myCats.cats    myCats.cats[0]    myCats.cats[0]['name']       
        
    
### 10 Organizing Files

    10.1 shutil module    
    10.1.1 shutil.copy(source, destination)   # 可以 copy 一个文件到另一个文件夹并，重命名
           
    10.1.2 shutil.copytree(source, destination)
           
    10.2 shutil.move(source, destination)   # 将一个文件移动到另一个位置
    
    10.3.1 os.unlink(path)      # 删除该path下的文件   
           os.rmdir(path)       # 删除该path的文件夹，但是文件夹必须为空
           shutil.rmtree(path)  # 删除该path下面的全部文件和文件夹，会不可逆的删除
    
    10.4 send2trash module   # 通过send2trash删除某文件更安全，如果误删，可以在回收站里还原
         pip install send2trash
    10.4.1 send2trash.send2trash(filename)   # 通过send2trash.send2trash() 把文件放入回收站
    
    10.5 os.walk()    # 遍历目录树
         eg.
         for folderName, subfolders, filenames in os.walk('C:\\delicious'):
         print('The current folder is ' + folderName)
         for subfolder in subfolders:
             print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
         for filename in filenames:
             print('FILE INSIDE ' + folderName + ': '+ filename)
    
    10.6 zipfile module
    10.6.1 zipfile.ZipFile('file.zip')
           eg.
           from pathlib import Path
           p = Path('E:/python/boring4pycharm')
           exampleZip = zipfile.ZipFile(p/'example.zip')  
           exampleZip.namelist()      # exampleZip下面包含的所有文件的文件名
           spamInfo = exampleZip.getinfo('spam.txt')  # 获取
           spamInfo.file_size         
           spamInfo.compress_size
           f'Compressed file is {round(spamInfo.file_size/spamInfo.compress_size,2)}x smaller!'
           exampleZip.close()
           
    10.6.2 exampleZip.extractall()     # 提取全部文件
           exampleZip.extractall('C:\\delicious')   # 放入指定文件夹
           
           exampleZip.extract('spam.txt')   # 从exampleZip 文档中提取一个spam文件
    
    10.6.3 zipfile.ZipFile('new.zip', 'w')  # 创建一个new.zip 打包文件，
           newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) # 向newzip文件里面写入需要打包的文件
           注意：write会覆盖new.zip之前存在的其他文件，只是添加可以用 zipfile.ZipFile('file.zip','a')               

### 11 Debugging

    11.1 raise Exception('This is the error message.')
         try...except Exception as err         
    
    11.2 traceback module
         traceback.format_exc()
    
    11.3 assert    # 仅供程序员调试使用，一般用户不会见到这个，assert不能用来替代raise exception，也不用于替代测试工作
         AssertionError         
    
    11.4 logging module
    11.4.1 logging.basicConfig()
           eg. logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s)         
           logging.debug()
           eg. logging.debug('End of factorial(%s%%)'  % (n))
           
    11.4.2 logging level
           DEBUG       logging.debug()        最低级别，用于打印信息
           INFO        logging.info()         用于记录某些事件，或确定工作节点运行正常
           WARNING     logging.warning()      给出警告，但暂不处理
           ERROR       logging.error()        记录错误
           CRITICAL    logging.critical()     最高级别，记录导致程序崩溃的错误
           
    11.4.3 logging.disable()
           eg. logging.disable(logging.CRITICAL)   # logging.disable()会让所有的报错失效，不仅仅是critical，包括error等
           
    11.4.4 logging.basicConfig(filename='filename.txt',...)  # 把错误信息输出到txt文件
           eg. logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
               %(asctime)s -  %(levelname)s -  %(message)s')
    
    11.5
    
    11.6
    

### 12
        

    

    

        

        
       

        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
              
        
        
        
        
          
          
       
    
    
    

