# https://en.wikipedia.org/wiki/Melting_point
# https://en.wikipedia.org/wiki/Triple_point
# https://en.wikipedia.org/wiki/List_of_chemical_elements

#1.0 给定每个元素的熔点（开氏温度）
melting_point = [
  ('C'  , 3800   ),
  ('Al' ,  933.47),
  ('Fe' , 1811   ),
  ('Cu' , 1357.77),
  # ('Ag' , 1234.93),
  ('W'  , 3695   ),
  ('Pt' , 2041.4 ),
  # ('Au' , 1337.33),
  # ('Hg' ,  234.43),
]

# 2.1.1  获取元素符号的集合
def get_symbol(xs):
    l=[]
    for x in xs:
        l.append(x[0])
    return l

# 2.1.2 获取元素符号的集合
def get_symbol(xs):
    return list(map(lambda x:x[0],xs))
  
# 2.2.1 获取元素熔点的集合（开氏）
def get_melting_point(xs):
    l=[]
    for x in xs:
        l.append(x[1])
    return l
  
# 2.2.2 获取元素熔点的集合（开氏）
def get_melting_point(xs):
    return list(map(lambda x:x[1],xs))

# 2.3 获取集合输出结果 
get_symbol       (melting_point) == ['C' , 'Al'  , 'Fe', 'Cu'   , 'W' , 'Pt'  ]
get_melting_point(melting_point) == [3800, 933.47, 1811, 1357.77, 3695, 2041.4]


# 3.1.1 温度转换：开氏温度-摄氏度
def to_celsius(xs):
    l=[]
    for x in xs:
        l.append((x[0],x[1]-273.15))
    return l

# 3.1.2 温度转换：开氏温度-摄氏度
def to_celsius(xs):
    return list(map(lambda x:(x[0],x[1]-273.15),xs))

# 3.2 温度转换输出结果
to_celsius(melting_point) == [
  ('C' , 3526.85),
  ('Al',  660.32),
  ('Fe', 1537.85),
  ('Cu', 1084.62),
  # ('Ag',  961.78),
  ('W',  3421.85),
  ('Pt', 1768.25),
  # ('Au', 1064.18),
  # ('Hg',  -38.72),
]

# 4.1.1 获取低于y温度（开氏）的元素和温度集合
def below(xs, y):
    l=[]
    for x in xs:
        if x[1]<=y:
            l.append(x)
    return l

# 4.1.2 获取低于y温度（开氏）的元素和温度集合 
def below(xs, y):
    return list(filter(lambda x:x[1]<=y,xs))

# 4.2.1 获取高于y温度（开氏）的元素和温度集合  
def above(xs, y):
    l=[]
    for x in xs:
        if x[1]>=y:
            l.append(x)
    return l

# 4.2.2 获取高于y温度（开氏）的元素和温度集合  
def above(xs, y):
    return list(filter(lambda x:x[1]>=y,xs))
  
# 4.3.1 获取高于y温度（开氏），同时低于z温度（开氏）的元素和温度集合
def between(xs, y, z):
    l=[]
    for x in xs:
        if y <= x[1]<=z:
            l.append(x)
    return l

# 4.3.2 获取高于y温度（开氏），同时低于z温度（开氏）的元素和温度集合
def between(xs, y, z):
    return list(filter(lambda x: y <= x[1]<=z,xs))

# 4.4 输出结果  
below(melting_point, 1000) == [('Al', 933.47)]
below(melting_point, 1500) == [('Al', 933.47), ('Cu', 1357.77)]
below(melting_point, 2000) == [('Al', 933.47), ('Fe', 1811), ('Cu', 1357.77)]

above(melting_point, 3000) == [('C', 3800), ('W', 3695)]
above(melting_point, 2000) == [('C', 3800), ('W', 3695), ('Pt', 2041.4)]
above(melting_point, 1500) == [('C', 3800), ('Fe', 1811), ('W', 3695), ('Pt', 2041.4)]

between(melting_point, 1000, 1500) == [('Cu', 1357.77)]
between(melting_point, 1500, 2000) == [('Fe', 1811)]
between(melting_point, 2000, 3000) == [('Pt', 2041.4)]


# 5.1.1 获取低于y温度（开氏）的元素集合
def below_symbol(xs, y):
    l=[]
    for x in xs:
        if x[1]<=y:
            l.append(x[0])
    return l        

# 5.1.2 获取低于y温度（开氏）的元素集合
def below_symbol(xs, y):
    return list(map(lambda x:x[0],filter(lambda x:x[1]<=y,xs)))

# 5.2.1 获取高于y温度（开氏）的元素集合
def above_symbol(xs, y):
    l=[]
    for x in xs:
        if x[1]>=y:
            l.append(x[0])
    return l

# 5.2.2 获取高于y温度（开氏）的元素集合
def above_symbol(xs, y):
    return list(map(lambda x:x[0],filter(lambda x:x[1]>=y,xs)))

# 5.3.1 获取高于y温度（开氏），同时低于z温度（开氏）的元素集合
def between_symbol(xs, y, z):
    l=[]
    for x in xs:
        if y <= x[1]<=z:
            l.append(x[0])
    return l            

# 5.3.2 获取高于y温度（开氏），同时低于z温度（开氏）的元素集合
def between_symbol(xs, y, z):
    return list(map(lambda x:x[0],filter(lambda x:y <= x[1]<=z,xs)))

# 5.4 输出结果
below_symbol(melting_point, 1000) == ['Al']
below_symbol(melting_point, 1500) == ['Al', 'Cu']
below_symbol(melting_point, 2000) == ['Al', 'Fe', 'Cu']

above_symbol(melting_point, 3000) == ['C', 'W']
above_symbol(melting_point, 2000) == ['C', 'W', 'Pt']
above_symbol(melting_point, 1500) == ['C', 'Fe', 'W', 'Pt']

between_symbol(melting_point, 1000, 1500) == ['Cu']
between_symbol(melting_point, 1500, 2000) == ['Fe']
between_symbol(melting_point, 2000, 3000) == ['Pt']


# 6.1.1 获取低于y温度（摄氏度）的元素和温度（摄氏度）集合 输入是开氏温度，需转换
def to_celsius_below(xs, y):
    l=[]
    for x in xs:
        if x[1]-273.15 <=y:
            l.append((x[0],x[1]-273.15))
    return l

# 6.1.2 获取低于y温度（摄氏度）的元素和温度（摄氏度）集合 输入是开氏温度，需转换
def to_celsius_below(xs, y):
    return list(map(lambda x:(x[0],x[1]-273.15),filter(lambda x:x[1]-273.15<=y,xs)))

# 6.2.1 获取高于y温度（摄氏度）的元素和温度（摄氏度）集合 输入是开氏温度，需转换
def to_celsius_above(xs, y):
    l=[]
    for x in xs:
        if x[1]-273.15 >=y:
            l.append((x[0],x[1]-273.15))
    return l

# 6.2.2 获取高于y温度（摄氏度）的元素和温度（摄氏度）集合 输入是开氏温度，需转换
def to_celsius_above(xs, y):
    return list(map(lambda x:(x[0],x[1]-273.15),filter(lambda x:x[1]-273.15>=y,xs)))


# 6.3.1 获取高于y温度（摄氏度），同时低于z温度（摄氏度）的元素和温度（摄氏度）集合 输入是开氏温度，需转换
def to_celsius_between(xs, y, z):
    l=[]
    for x in xs:
        if y <= x[1]-273.15 <=z:
            l.append((x[0],x[1]-273.15))
    return l

# 6.3.2 获取高于y温度（摄氏度），同时低于z温度（摄氏度）的元素和温度（摄氏度）集合 输入是开氏温度，需转换
def to_celsius_between(xs, y, z):
    return list(map(lambda x:(x[0],x[1]-273.15),filter(lambda x:y <= x[1]-273.15 <= z,xs)))

# 6.4 输出结果
to_celsius_below(melting_point, 1000) == [('Al', 660.32)]
to_celsius_below(melting_point, 1500) == [('Al', 660.32), ('Cu', 1084.62)]
to_celsius_below(melting_point, 2000) == [('Al', 660.32), ('Fe', 1537.85), ('Cu', 1084.62), ('Pt', 1768.25)]

to_celsius_above(melting_point, 3000) == [('C', 3526.85), ('W', 3421.85)]
to_celsius_above(melting_point, 2000) == [('C', 3526.85), ('W', 3421.85)]
to_celsius_above(melting_point, 1500) == [('C', 3526.85), ('Fe', 1537.85), ('W', 3421.85), ('Pt', 1768.25)]

to_celsius_between(melting_point, 1000, 1500) == [('Cu', 1084.62)]
to_celsius_between(melting_point, 1500, 2000) == [('Fe', 1537.85), ('Pt', 1768.25)]
to_celsius_between(melting_point, 2000, 3000) == []
