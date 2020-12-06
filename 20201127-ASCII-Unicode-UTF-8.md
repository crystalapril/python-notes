# ASCII-Unicode-UTF-8

- ASCII
- GB2312 & GBK
- Unicode
- UTF-8

### ASCII

    byte 字节
    
    最早的时候, 人们用8个可以开合的晶体管来组合成不同的状态，表示世界万物。
    每个开关有 2 个状态，0，1，那么8个开关可以表示 256种状态（2的8次方）
    一个开关，0 或 1，是一个 bit ，binary digit
    一个字节 byte = 8 bit，例如 1000 0101
    
    于是，一个八位的字节，一共可以组合出256(2的8次方)种不同的状态       
    再后来，人们又做了一些可以处理这些字节的机器，用很多字节来组合出很多状态，状态开始变来变去，他们称这个机器为”计算机“。    
    
    ASCII
    
    最开始计算机只在美国使用
    
    人们把编号从0开始的32种状态分别规定了特殊的用途
    一但终端、打印机遇上约定好的这些字节被传过来时，就要做一些约定的动作：
    
    遇上0000 1010（十进制的 10）,line feed， 终端就换行；

    遇上0000 0111（十进制的 7）, bell，终端就向人们嘟嘟叫；
    
    他们看到这样很好，于是就把这些 0010 0000 （32）以下的字节状态称为”控制码”，Control characters
    控制码包括：
    LF（换行）、CR（回车）、FF（换页）、DEL（删除）、BS（退格)、BEL（响铃）
    SOH（文头）、EOT（文尾）、ACK（确认） 等等
    
    他们又把所有的空 格、标点符号、数字、大小写字母分别用连续的字节状态表示，一直编到了第127号
    这样计算机就可以用不同字节来存储英语的文字了
        
    大家都把这个方案叫做 ANSI 的 ASCII 编码（American Standard Code for Information Interchange，美国信息互换标准代码）
    当时世界上所有的计算机都用同样的ASCII方案来保存英文文字。
    
    32～126(共95个)是字符(32是空格），其中48～57为0到9十个阿拉伯数字。
    65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等，例如：            
    
|Bin(二进制) | Oct(八进制) | Dec(十进制) | Hex(十六进制) |      缩写/字符     |
|-----------|------------|------------|--------------|-------------------|
|0000 0000  |      00    |  0         |    0x00      |  NUL(null)空字符   |
|0000 0001  |      01    |  1         |    0x01      |  SOH(start of headline) 标题开始 |
|0000 1010  |      012   |  10        |    0x0A      |  LF (NL line feed, new line)  换行键 |    
|0010 0011  |      043   |  35        |    0x23      |  #  井号           |
|0011 0011  |      063   |  51        |    0x33      |  3  字符3          |
|0011 1101  |      075   |  61        |    0x3D      |  = 等号            |
|0100 0101  |     0105   |  69        |    0x45      |  E  大写字母E      |
|0110 1110  |     0156   |  110       |    0x6E      |  n 小写字母n       |   
具体参见：
https://en.wikipedia.org/wiki/ASCII
https://baike.baidu.com/item/ASCII/309296?fromtitle=ascii%E7%A0%81&fromid=99077&fr=aladdin


### GB2312 & GBK

    扩展字符集
    
    后来，世界各地都开始使用计算机，但是很多国家用的不是英文，他们的字母里有许多是ASCII里没有的
    为了可以在计算机保存他们的文字
    他们决定采用 127号之后的空位来表示这些新的字母、符号，还加入了很多画表格时需要用下到的横线、竖线、交叉等形状
    比如，法语中的é的编码为130（二进制10000010）
    
    一直把序号编到了最后一个状态255，从128 到255这一页的字符集被称”扩展字符集“
    
    GB2312
    
    等中国人们得到计算机时，已经没有可以利用的字节状态来表示汉字，况且有6000多个常用汉字需要保存
    我们把那些127号之后的奇异符号们直接取消掉, 规定：
    
    一个小于127的字符的意义与原来 ASCII 相同，但两个大于127的字符连在一起时，就表示一个汉字
    前面的一个字节（称之为高字节）从0xA1用到0xF7，后面一个字节（低字节）从0xA1到0xFE
    
    这样我们就可以组合出大约7000多个简体汉字了
    在这些编码里，我们还把数学符号、罗马希腊的字母、日文的假名们都编进去了
    连在 ASCII 里本来就有的数字、标点、字母都统统重新编了两个字节长的编码，这就是常说的”全角”字符，
    而原来在127号以下的那些就叫”半角”字符了
    这种汉字方案叫做 “GB2312“，GB2312 是对 ASCII 的中文扩展
    GB 2312标准共收录6763个汉字，其中一级汉字3755个，二级汉字3008个
    
    GBK
    
    GB 2312的出现，基本满足了汉字的计算机处理需要，它所收录的汉字已经覆盖中国大陆99.75%的使用频率
    对于人名、古汉语等方面出现的罕用字，GB 2312不能处理
    于是 GBK 出现了
    
    我们不再要求低字节一定是127号之后的内码，只要第一个字节是大于127就固定表示这是一个汉字的开始，不管后面跟的是不是扩展字符集里的内容。
    结果扩展之后的编码方案被称为 GBK 标准，GBK包括了GB2312 的所有内容，同时又增加了近20000个新的汉字（包括繁体字）和符号。       
    后来少数民族也要用电脑了，于是我们再扩展，又加了几千个新的少数民族的字，GBK扩成了 GB18030。
    
    GBK是采用单双字节变长编码，英文使用单字节编码，完全兼容ASCII字符编码
    中文部分采用双字节编码，“DBCS“（Double Byte Charecter Set 双字节字符集）
    因此，在DBCS系列标准里，最大的特点是两字节长的汉字字符和一字节长的英文字符并存于同一套编码方案里
    为了支持中文处理，中文程序员必须要注意字串里的每一个字节的值，如果这个值是大于127的，那么就认为一个双字节字符集里的字符出现了
    一个汉字算两个英文字符！   

### Unicode

    除了中国，日文和韩文等其他语言也有这个问题
    为了统一所有文字的编码，Unicode应运而生
    一个叫 ISO（国际标谁化组织）的国际组织，采用了一个方法：
    废了所有的地区性编码方案，重新搞一个包括了地球上所有文化、所有字母和符号的编码
    叫做 ”Universal Multiple-Octet Coded Character Set”，简称 UCS, 俗称 “unicode“    
    
    Unicode 规定必须用两个字节，也就是16位来统一表示所有的字符
    对于ASCII里的那些“半角”字符，unicode包持其原编码不变，只是将其长度由原来的8位扩展为16位
    由于”半角”英文符号只需要用到低8位，所以其高8位永远是0
    而其他文化和语言的字符则全部重新统一编码
    
    因此，在 Unicode 里，所有的汉字都是跟英文一样，16位来表示
    在unicode中，一个字符就是两个字节。一个汉字算两个英文字符（GBK里）的时代已经快过去了
    注意，”字符”和”字节”两个术语的不同，“字节”是一个8位的物理存贮单元，而“字符”则是一个文化相关的符号   
       

### UTF-8

    unicode同样也不完美，这里就有两个的问题：
    1.如何才能区别unicode和ascii？计算机怎么知道三个字节表示一个符号，而不是分别表示三个符号呢？
    2.英文字母只用一个字节表示就够了，如果unicode统一规定，每个符号用三个或四个字节表示，那么每个英文字母前都必然有二到三个字节是0
      这对于存储空间来说是极大的浪费，文本文件的大小会因此大出二三倍
      
    为解决unicode如何在网络上传输的问题，于是面向传输的众多 UTF（UCS Transfer Format）标准出现了
    UTF-8就是每次8个位传输数据，而UTF-16就是每次16个位
    
    UTF-8就是在互联网上使用最广的一种unicode的实现方式，这是为传输而设计的编码，而且可以显示全世界上所有文化的字符
    UTF-8最大的一个特点，就是它是一种变长的编码方式
    UTF-8使用1~4个字节表示一个符号，根据不同的符号而变化字节长度
    当字符在ASCII码的范围时，就用一个字节表示，保留了ASCII字符一个字节的编码做为它的一部分
    注意的是unicode一个中文字符占2个字节，而UTF-8一个中文字符占3个字节
    从unicode到utf-8并不是直接的对应，而是要过一些算法和规则来转换
    
    Unicode符号范围      |   UTF-8编码方式
    (十六进制)           |  （二进制）
    —————————————————————————————————————————————————————————
    0000 0000-0000 007F | 0xxxxxxx
    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
     
    


