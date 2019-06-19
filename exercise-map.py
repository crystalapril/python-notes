1.摄氏度转华氏度，华氏度转摄氏度，开氏温标（绝对零度 ）（华氏度跟开氏温标之间免了）
输入：数组，输出：数组
celsius_to_kelvin([0,1,2]) == [273.15, 274.15, 275.15]
写这四个函数
celsius_to_kelvin
kelvin_to_celsius
celsius_to_fahrenheit
fahrenheit_to_celsius


2.物质的熔点 （开氏温标）
输入
melting_point =[ ('C'  , 3800   )
, ('Al' ,  933.47)
, ('Fe' , 1811   )
, ('Cu' , 1357.77)
, ('Ag' , 1234.93)
, ('W'  , 3695   )
, ('Pt' , 2041.4 )
, ('Au' , 1337.33)
, ('Hg' ,  234.43)
]

2.1 输出 ['C','Al',....'Hg']  取出包含的化学元素
2.2 输出[('C', 3526.85), ... , ('Hg', -38.72)] 转成摄氏度


3  f3(melting_point, 200) == []
f3(melting_point, 300) == [('Hg' ,  234.43)]
f3(melting_point, 1000) == [('Al' ,  933.47), ('Hg' ,  234.43)]
取出melting_point<200,300的数组  （不做温度的转换，都是开氏温度）

4 
f4(melting_point, 100, 200) == []
f4(melting_point, 200, 300) == [('Hg' ,  234.43)]
f4(melting_point, 200, 1000) == [('Al' ,  933.47), ('Hg' ,  234.43)]
f4(melting_point, 300, 1000) == [('Al' ,  933.47)]
取出熔点在100-200之间的（开氏温度）

5
f5(melting_point, 200) == []
f5(melting_point, 300) == ['Hg']
f5(melting_point, 1000) == ['Al', 'Hg']
取出melting_point<200,300的元素（类似题3，但是输出里不包含熔点）







