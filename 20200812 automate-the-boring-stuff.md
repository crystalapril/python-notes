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
    
    11.5 debug  # 可以用pycharm的debug功能 ，不同的编译器处理会有细微的差别
         step in       一行行往下走，如果进入子函数，从子行数第一行开始，一行行的运行
         step over     一行行往下走，进入子函数，如果子函数无断点，则把子函数当做一步，如果子函数有断点，从断点处开始执行
         step out      跳出子函数，如果无断点，直接跳出子函数，如果有断点，执行完断点后再跳出子函数
         breakpoints   设置断点            

### 12 Web Scraping

    12.1 webbrowser module 
         webbrower.open('https://www.google.com')
    
    12.2 requests module 
         request.get() 
         eg. res = requests.get('https://automatetheboringstuff.com/files/rj.txt')  # 下载网页上的文本信息等
             res.raise_for_status()   # 查看是否成功获取网页信息
             res.status_code   # status_code 200表示正常
             len(res.text)     # 查看获取的文本信息长度              
        
         open(), write()
         res.iter_content()    
         eg. playFile = open('RomeoAndJuliet.txt', 'wb')   # 创建一个txt文件
             # 注意这里必须要用wb（write binary）二进制模式来写入，为了保持Unicode encoding
             for chunk in res.iter_content(100000):  # 用for 循环，iter_content()返回一块块内容，chunks都是 bytes 类型
                playFile.write(chunk)    
             playFile.close()

    12.3 HTML
    12.3.1 text is surrounded by tags, enclosed by angle brackets
           eg. <strong>Hello</strong>, world!   # <strong> 是给hello加粗
               Al's free <a href="https://inventwithpython.com">Python books</a>.  # <a> 表示里面有个link，href是引用link
               <h1 id="myHeader">   
    12.3.2 view page source   # 鼠标右键点击view page source ，可以查看网页源代码    
    12.3.3 developer tools
    12.3.4 copy-CSS selector

    12.4 bs4 module # Beautiful Soup version 4， 用于提取 HTML 页面的信息
    12.4.1 bs4.BeautifulSoup() 
    12.4.2 BeautifulSoup object的 select() 方法，可以传递一个CSS-selector的参数，去查找    
           eg. soup.select('div')          # 查找所有名字为 div 的元素
               soup.select('#author')      # 查找 id="author" 元素
               soup.select('.notice')      # 所有使用class属性，名为notice的元素
               soup.select('div span')     # 所有名为 <span> 的元素，且被<div>包含 
               soup.select('div > span')   # 所有名为 <span> 的元素，且被<div>直接包含，中间没有其他元素 
               soup.select('input[name]')  # 所有名为 <input> 的元素，含有name这个属性，name可以有任意值
               soup.select('input[type="button"]') # 所有名为<input>的元素，有type这个属性，type的值为button
    
           eg. >>> exampleFile = open('example.html')
               >>> exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
               >>> elems = exampleSoup.select('#author')
               >>> type(elems[0])
               <class 'bs4.element.Tag'>
               >>> str(elems[0]) # The Tag object as a string.
               '<span id="author">Al Sweigart</span>'
               >>> elems[0].getText()
               'Al Sweigart'
               >>> elems[0].attrs
               {'id': 'author'}
               
           eg. >>> pElems = exampleSoup.select('p')
               >>> str(pElems[0])
               '<p>Download my <strong>Python</strong> book from <a href="https://inventwithpython.com">my website</a>.</p>'
               >>> pElems[0].getText()
               'Download my Python book from my website.'
               >>> str(pElems[1])
               '<p class="slogan">Learn Python the easy way!</p>'
               >>> pElems[1].getText()
               'Learn Python the easy way!'
    12.4.3 BeautifulSoup object的get()方法
           eg. >>> soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
               >>> spanElem = soup.select('span')[0]
               >>> str(spanElem)
               '<span id="author">Al Sweigart</span>'
               >>> spanElem.get('id')
               'author'
               >>> spanElem.get('some_nonexistent_addr') == None
               True   
    
    12.5 selenium module  # web 自动化工具
    12.5.1  from selenium import webdriver
            browser = webdriver.Firefox()    # 使用火狐来打开网页
            type(browser)
            browser.get('https://inventwithpython.com')   # 打开该网页
            try:
                elem = browser.find_element('name',' cover-thumb')   # 查找name= cover-thumb
                print('Found <%s> element with that class name!' % (elem.tag_name))
            except:
                print('was not able to find an element with that name.')

            linkElem = browser.find_element('link text','Read Online for Free')  # 查找link text = Read Online for Free
            type(linkElem)
            linkElem.click()  # 类似与鼠标点击开了该页面
    
    12.5.2  browser.get('https://login.metafilter.com')
            userElem = browser.find_element('id','user_name')  # 查找 id =user_name
            userElem.send_keys('your_real_username_here')      # 输入用户名
            passwordElem = browser.find_element('id','user_pass')
            passwordElem.send_keys('your_real_password_here')   # 输入密码
            passwordElem.submit()         # 提交
    
    12.5.3  from selenium.webdriver.common.keys import Keys
            browser = webdriver.Firefox()
            browser.get('https://nostarch.com')
            htmlElem = browser.find_element('tag name','html')
            htmlElem.send_keys(Keys.END)   # 到页面的底部
            htmlElem.send_keys(Keys.HOME)  # 回到主页
    
    12.5.4  browser.back()
            browser.forward()
            browser.refresh()   # 刷新浏览器
            browser.quit()      # 退出浏览器

### 13 Working with Excel Speadsheets

    openpyxl module
    13.1 spreadSheet
         >>> wb = openpyxl.load_workbook('example.xlsx')
         >>> type(wb)
         <class 'openpyxl.workbook.workbook.Workbook'>    
         >>> wb.sheetnames # The workbook's sheets' names.
         ['Sheet1', 'Sheet2', 'Sheet3']
         >>> sheet = wb['Sheet3']   # Get a sheet from the workbook.
         >>> sheet
         <Worksheet "Sheet3">
         >>> type(sheet)
         <class 'openpyxl.worksheet.worksheet.Worksheet'>
         >>> sheet.title   # Get the sheet's title as a string.
         'Sheet3'
         >>> anotherSheet = wb.active   # Get the active sheet.
         >>> anotherSheet
         <Worksheet "Sheet1">

    13.2 cell
        >>> sheet = wb['Sheet1'] # Get a sheet from the workbook.
        >>> sheet['A1'] # Get a cell from the sheet.
        <Cell 'Sheet1'.A1>
        >>> sheet['A1'].value # Get the value from the cell.
        datetime.datetime(2015, 4, 5, 13, 34, 2)
        >>> c = sheet['B1'] # Get another cell from the sheet.
        >>> c.value
        'Apples'
        >>> 'Row %s, Column %s is %s' % (c.row, c.column, c.value)
        'Row 1, Column B is Apples'
        >>> 'Cell %s is %s' % (c.coordinate, c.value)
        'Cell B1 is Apples'
        
        >>> sheet.cell(row=1, column=2).value
        'Apples'
        >>> for i in range(1, 8, 2): # Go through every other row:
        ...     print(i, sheet.cell(row=i, column=2).value)
        ...
        1 Apples
        3 Pears
        5 Apples
        7 Strawberries
    
    13.3 max_row, get_column_letter, column_index_from_string
        >>> sheet.max_row # Get the highest row number.
        7
        >>> sheet.max_column # Get the highest column number.
        >>> from openpyxl.utils import get_column_letter, column_index_from_string
        >>> get_column_letter(1) # Translate column 1 to a letter.
        'A'
        >>> get_column_letter(sheet.max_column)
        'C'
        >>> column_index_from_string('A') # Get A's number.
        1
    
    13.4 sheet['A1':'C3']
        >>> tuple(sheet['A1':'C3']) # Get all cells from A1 to C3.
       ((<Cell 'Sheet1'.A1>,<Cell 'Sheet1'.B1>,<Cell 'Sheet1'.C1>)...(<Cell 'Sheet1'.A3>,<Cell 'Sheet1'.B3>,<Cell 'Sheet1'.C3>))
       >>> for rowOfCellObjects in sheet['A1':'C3']:
       ...     for cellObj in rowOfCellObjects:
       ...         print(cellObj.coordinate, cellObj.value)
       
       A1 2015-04-05 13:34:02
       B1 Apples
       C1 73
       ....
    
    13.5 list(sheet.columns)[1], 
        >>> list(sheet.columns)[1] # Get second column's cells.
        (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2> ... <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
        >>> for cellObj in list(sheet.columns)[1]:
                print(cellObj.value)
        Apples
        Cherries
        Pears
        ...   

    13.6 sheet.title, wb.sheetnames
        >>> wb = openpyxl.Workbook() # Create a blank workbook.
        >>> wb.sheetnames # It starts with one sheet.
        ['Sheet']
        >>> sheet.title = 'Spam Bacon Eggs Sheet' # Change title.
        >>> wb.sheetnames
        ['Spam Bacon Eggs Sheet']
        >>> wb.save('example_copy.xlsx') # Save the workbook.

    13.7 wb.create_sheet(), del wb['Sheet1'], sheet['A1'] = 'Hello, world!'
        >>> wb.create_sheet() # Add a new sheet.
        <Worksheet "Sheet1">
        >>> wb.create_sheet(index=0, title='First Sheet') # Create a new sheet at index 0.
        <Worksheet "First Sheet">
        >>> wb.sheetnames
        ['First Sheet', 'Sheet', 'Sheet1']        
        >>> del wb['Sheet1']
        >>> wb.sheetnames
        ['First Sheet', 'Sheet']
        >>> sheet = wb['Sheet']
        >>> sheet['A1'] = 'Hello, world!' # Edit the cell's value.
        >>> sheet['A1'].value
        'Hello, world!'
    
    13.8 Font object
        >>> from openpyxl.styles import Font 
        >>> fontObj1 = Font(name='Times New Roman', bold=True)  # Create a font object
        >>> sheet['A1'].font = fontObj1
        >>> sheet['A1'] = 'Bold Times New Roman'
        >>> fontObj2 = Font(size=24, italic=True)
        >>> sheet['B3'].font = fontObj2
        >>> sheet['B3'] = '24 pt Italic'
    
    13.9 formulas
        >>> sheet['A1'] = 200
        >>> sheet['A2'] = 300
        >>> sheet['A3'] = '=SUM(A1:A2)' # Set the formula.
    
    13.10 sheet.row_dimensions, sheet.column_dimensions
        >>> sheet.row_dimensions[1].height = 70  # 当height=0 或 width=0的时候，就被隐藏了
        >>> sheet.column_dimensions['B'].width = 20
        >>> wb.save('dimensions.xlsx')
    
    13.11 sheet.merge_cells(), sheet.unmerge_cells()
        >>> sheet.merge_cells('A1:D3') # Merge all these cells.
        >>> sheet['A1'] = 'Twelve cells merged together.'
        >>> sheet.merge_cells('C5:D5') # Merge these two cells.
        >>> sheet['C5'] = 'Two merged cells.'
        >>> wb.save('merged.xlsx')

        >>> sheet.unmerge_cells('A1:D3') # Split these cells up.
        >>> sheet.unmerge_cells('C5:D5')
    
    13.12 freeze_panes 
        >>> wb = openpyxl.load_workbook('produceSales.xlsx')
        >>> sheet = wb.active
        >>> sheet.freeze_panes = 'A2' # Freeze the rows above A2.
        >>> sheet.freeze_panes = None  # 解冻
    
    13.13 openpyxl.chart  # 制作图表
        >>> sheet = wb.active
        >>> for i in range(1, 11): # create some data in column A
        ...     sheet['A' + str(i)] = i
        >>> refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
        >>> seriesObj = openpyxl.chart.Series(refObj, title='First series')

        >>> chartObj = openpyxl.chart.BarChart()
        >>> chartObj.title = 'My Chart'
        >>> chartObj.append(seriesObj)

        >>> sheet.add_chart(chartObj, 'C5')
        >>> wb.save('sampleChart.xlsx')

### 14 Working with Google Spreadsheets

### 15 Working with PDF and Word Documents

    15.1 PyPDF2 module
    15.1.1 open('m.pdf','rb'), PyPDF2.PdfFileReader(pdfFileObj) ,pdfReader.getPage(0), pageObj.extractText()
        >>> import PyPDF2
        >>> pdfFileObj = open('meetingminutes.pdf', 'rb')   # 从pdf里面提取的二进制文件被写入到 pdfFileObj
        >>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)    # 转成 PdfFileReader object，并储存在变量 pdfReader里
        >>> pdfReader.numPages       # 页面数
        19
        >>> pageObj = pdfReader.getPage(0)    # 通过getPage() 获得第一页，page object
        >>> pageObj.extractText()             # 提取页面内容，字符串
    
    15.1.2 pdfReader.isEncrypted,pdfReader.decrypt('password')   
        >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
        >>> pdfReader.isEncrypted
           True
        >>> pdfReader.getPage(0)
        Traceback (most recent call last):
               raise utils.PdfReadError("file has not been decrypted")
           PyPDF2.utils.PdfReadError: file has not been decrypted
           
        >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))  # 这里必须重新打开一次，
        >>> pdfReader.decrypt('rosebud')
        1               # 密码输入正确，返回1，输入错误，返回0
        
    15.1.3 PyPDF2.PdfFileWriter(), addPage()   
           eg. 合并pdf    # PyPDF2不能单纯的复制页面，需要先创建一个新的pdf，然后复制页面到新pdf去
           >>> pdf1File = open('meetingminutes.pdf', 'rb')
           >>> pdf2File = open('meetingminutes2.pdf', 'rb')
           >>> pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
           >>> pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
           >>> pdfWriter = PyPDF2.PdfFileWriter()    
           >>> for pageNum in range(pdf1Reader.numPages):
                   pageObj = pdf1Reader.getPage(pageNum)
                   pdfWriter.addPage(pageObj)
           >>> for pageNum in range(pdf2Reader.numPages):
                   pageObj = pdf2Reader.getPage(pageNum)   # 页面的复制无法从中间复制，只能在末尾处开始复制
                   pdfWriter.addPage(pageObj)
           >>> pdfOutputFile = open('combinedminutes.pdf', 'wb')  # 这里也是wb，用二进制的模式写入
           >>> pdfWriter.write(pdfOutputFile)  
    
    15.1.4 rotateClockwise(),rotateCounterClockwise()
        >>> minutesFile = open('meetingminutes.pdf', 'rb')
        >>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
        >>> page = pdfReader.getPage(0)
        >>> page.rotateClockwise(90)    # 顺时针旋转90度
        >>> pdfWriter = PyPDF2.PdfFileWriter()
        >>> pdfWriter.addPage(page)
        >>> resultPdfFile = open('rotatedPage.pdf', 'wb')
        >>> pdfWriter.write(resultPdfFile)    
    
    15.1.5 Page.mergePage(page1)
        >>> minutesFile = open('meetingminutes.pdf', 'rb')
        >>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
        >>> minutesFirstPage = pdfReader.getPage(0)
        >>> pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
        >>> minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))   # 将 watermark的水印添加到 minutesFirstPage去

    15.1.6 pdfWriter.encrypt('password')
       >>> pdfWriter = PyPDF2.PdfFileWriter()
       >>> pdfWriter.encrypt('swordfish')     # 给pdf文件设置密码
       >>> resultPdf = open('encryptedminutes.pdf', 'wb')
       >>> pdfWriter.write(resultPdf)


    15.2 python-docx module (import docx)
    
    15.2.1 docx.Document('demo.docx'), doc.paragraphs
        >>> import docx
        >>> doc = docx.Document('demo.docx')  # 通过 docx.Document() 读取docx文件
        >>> len(doc.paragraphs)               # doc.paragraphs返回一个list，说明该文件中有7段 paragraph
           7
        >>> doc.paragraphs[0].text            # 第一段 paragraph 的文本内容
           'Document Title'
        >>> doc.paragraphs[1].text
           'A plain paragraph with some bold and some italic'
        >>> len(doc.paragraphs[1].runs)       # 第二段 paragraph 里面包含 4 个run，runs也是返回一个list
           4
        >>> doc.paragraphs[1].runs[0].text    # 第二段 paragraph 的第一个 run 的文本
           'A plain paragraph with some '
        >>> doc.paragraphs[1].runs[1].text    # 每个 run 的区别主要为格式不同
           'bold'
        >>> doc.paragraphs[1].runs[2].text
           ' and some '
        >>> doc.paragraphs[1].runs[3].text
           'italic'
           
        eg2.
        def getText(filename):
            doc = docx.Document(filename)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
            return '\n'.join(fullText)

    15.2.2 Styling Paragraph and Run Objects
    eg. paragraphObj.style = 'Quote'
        runObj.style = 'Quote Char'    
    
    15.2.3 text attributes: doc.paragraphs[0].style, doc.paragraphs[1].runs[0].style 
    >>> doc = docx.Document('demo.docx')
    >>> doc.paragraphs[0].style # The exact id may be different:
    _ParagraphStyle('Title') id: 3095631007984
    >>> doc.paragraphs[0].style = 'Normal'             # 格式为 normal
    >>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
    >>> doc.paragraphs[1].runs[1].underline = True     # 添加下划线
    >>> doc.save('restyled.docx')
    
    15.2.4 Writing Word Documents: doc.add_paragraph('Hello, world!'), save() 
    >>> doc = docx.Document()
    >>> doc.add_paragraph('Hello, world!', 'Title')       # 第二个参数格式是可选的，可以有，可以没有
    <docx.text.Paragraph object at 0x000000000366AD30>    # 返回 Paragraph object
    >>> paraObj1 = doc.add_paragraph('This is a second paragraph.')   # 接 hello world 后面，下一行
    >>> paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
    >>> paraObj1.add_run(' This text is being added to the second paragraph.')  # 接在 paraObj1 的后面，同一行
    <docx.text.Run object at 0x0000000003A2C860>          # 返回 Run object
    >>> doc.save('multipleParagraphs.docx')
    
    15.2.5 Adding Headings
    >>> doc.add_heading('Header 0', 0)      # 一共有5级header，从0-4，依次变小，0默认为title
    <docx.text.Paragraph object at 0x00000000036CB3C8>
    >>> doc.add_heading('Header 1', 1)
    <docx.text.Paragraph object at 0x00000000036CB630>
    >>> doc.add_heading('Header 2', 2)
    <docx.text.Paragraph object at 0x00000000036CB828>
    >>> doc.save('headings.docx')
    
    15.2.6 Adding Line and Page Breaks
       >>> doc = docx.Document()
       >>> doc.add_paragraph('This is on the first page!')
       <docx.text.Paragraph object at 0x0000000003785518>
       >>> doc.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)    # add_break()出现了分页的效果
       >>> doc.add_paragraph('This is on the second page!')        # 显示在了第二页
       <docx.text.Paragraph object at 0x00000000037855F8>
       >>> doc.save('twoPage.docx')
    
    15.2.7 Adding Pictures
    >>> doc.add_picture('zophie.png', width=docx.shared.Inches(1), height=docx.shared.Cm(4))
    <docx.shape.InlineShape object at 0x00000000036C7D30>

    15.2.8 Creating PDFs from Word Documents
    pip install --user -U pywin32==224


### 16 Working with CSV Files and JSON Data

    16.1 csv module    
    16.1.1 reader Objects, csv.reader(exampleFile)
         >>> import csv
         >>> exampleFile = open('example.csv')
         >>> exampleReader = csv.reader(exampleFile)    # 返回 reader object
         >>> exampleData = list(exampleReader)
         >>> exampleData
           [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
           ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52']]
         
         >>> for row in exampleReader:    # exampleReader只能读取或循环一次，第二次提取需要再次调用 csv.reader(file)
                 print('Row #' + str(exampleReader.line_num) + ' ' + str(row))   
           Row #1 ['4/5/2015 13:34', 'Apples', '73']      # exampleReader.line_num 为当前行数，从 1 开始
           Row #2 ['4/5/2015 3:41', 'Cherries', '85']           
    
    16.1.2 writer Objects
       >>> outputFile = open('output.csv', 'w', newline='')   # 如果没有 newline=''，每行之间会间隔一行
       >>> outputWriter = csv.writer(outputFile)
       >>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
       21
       >>> outputWriter.writerow([1, 2, 3.141592, 4])
       16
       >>> outputFile.close()
    
    16.1.3 The delimiter and lineterminator Keyword Arguments
       >>> csvFile = open('example.tsv', 'w', newline='')
       >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
       >>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
       24
       >>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
       32
    
    16.1.4 DictReader and DictWriter CSV Objects  
        >>> exampleFile = open('exampleWithHeader.csv')
        >>> exampleDictReader = csv.DictReader(exampleFile)
        >>> for row in exampleDictReader:
        ...     print(row['Timestamp'], row['Fruit'], row['Quantity'])   # 可以用字典的形式读取
        
        >>> exampleFile = open('example.csv')   
        >>> exampleDictReader = csv.DictReader(exampleFile, ['time', 'name','amount'])
        >>> for row in exampleDictReader:   # 如果原始文件没有header行（没有字典的key），也可以自定义，然后来调取
        ...     print(row['time'], row['name'], row['amount'])
        
        >>> outputFile = open('output.csv', 'w', newline='')
        >>> outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
        >>> outputDictWriter.writeheader()   # 可以把['Name', 'Pet', 'Phone']作为header写入csv
        >>> outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
        20
        >>> outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'}) #可以打乱顺序，或者空着某个key
        15
    
    16.2 json module
    16.2.1 Reading JSON with the loads() Function
        >>> stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
        >>> import json
        >>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
        >>> jsonDataAsPythonValue
        {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
    
    16.2.2 Writing JSON with the dumps() Function
        >>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
        >>> stringOfJsonData = json.dumps(pythonValue)
        >>> stringOfJsonData    # 注意：json 格式里面是双引号
        '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'      


### 17 Keeping Time, Scheduling Tasks, and Launching Programs

    17.1 time module    
    17.1.1 time.time(),time.ctime(), time.sleep()
        >>> import time
        >>> time.time()
        1543813875.3518236  # 这个是从unix epoch 到现在经历的秒数
        >>> time.ctime()    # time.ctime() 也可以接受参数，eg.time.ctime(time.time()) 
        'Mon Jun 15 14:00:38 2020'
        >>> time.sleep(5)
    
    17.2 datetime module    
    17.2.1 datetime.datetime.now(), datetime.datetime()
        >>> import datetime
        >>> datetime.datetime.now()
        datetime.datetime(2022, 11, 28, 21, 51, 24, 795553)
        >>> dt = datetime.datetime(2022, 11, 28, 21, 51, 24)
        >>> dt.year,dt.month,dt.day
        (2022, 11, 28)
        >>> dt.hour,dt.minute,dt.second
        (21, 51, 24)
    
    17.2.2 datetime.datetime.fromtimestamp()
        >>> datetime.datetime.fromtimestamp(1000000)
        datetime.datetime(1970, 1, 12, 21, 46, 40)
        >>> datetime.datetime.fromtimestamp(time.time())   # 跟 datetime.datetime.now() 实现的功能一样
        datetime.datetime(2022, 11, 28, 21, 57, 58, 122447)
        >>> halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
        >>> newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
        >>> newyears2020 > halloween2019    # datetime object 之间可以比较大小，比较新的日期较大
        True
    
    17.2.3 datetime.timedelta()    
        >>> dt
        datetime.datetime(2018, 12, 2, 18, 38, 50, 636181)
        >>> thousandDays = datetime.timedelta(days=1000)  # datetime.timedelta() 返回一段期间，而不是一个时点
        >>> dt + thousandDays
        datetime.datetime(2021, 8, 28, 18, 38, 50, 636181)
        >>> dt - (thousandDays*2)     # datetime.timedelta() 的返回值，可以被用于加减乘除        
    
    17.2.4 strftime() : Converting datetime Objects into Strings
        >>> oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
        >>> oct21st.strftime('%Y/%m/%d %H:%M:%S')   # 注意：strftime() 的调用，前面没有 datetime.datetime
        '2019/10/21 16:29:00'
        >>> oct21st.strftime('%I:%M %p')
        '04:29 PM'
        >>> oct21st.strftime("%B of '%y")
        "October of '19"

    17.2.5 datetime.datetime.strptime(): Converting Strings into datetime Objects
       >>> datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
       datetime.datetime(2019, 10, 21, 16, 29)
       >>> datetime.datetime.strptime("October of '19", "%B of '%y")
       datetime.datetime(2019, 10, 1, 0, 0)    
    
    17.2.6 
    
    17.2.7 
    
    17.2.8 
    
    
    
    17.3 threading module
    
    17.4

### 18 Sending Email and Text Messages

### 19 Manipulating Images

### 20 Controlling the Keyboard and Mouse with GUI Automation


      

    

    

        

        
       

        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
              
        
        
        
        
          
          
       
    
    
    

