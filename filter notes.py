'''
前两题来自于codewars
1.筛选出不包含在geese列表中的值
2.筛选出偶数

第三题是构造filter函数
'''

#1.Filter out the geese.py
#A1.1
def goose_filter(birds):
    a=[]
    for x in birds:
        if x not in geese:
            a.append(x)
return a
#A1.2
def goose_filter(birds):
    return list(filter(lambda x:x not in geese,birds))
  
  
#2.Find numbers which are divisible by given number.py
#A2.1
def divisible_by(numbers, divisor):       
    l=[]
    for i in numbers:
        if i % divisor ==0:
            l.append(i)
return l
#A2.2
def divisible_by(a,b):
    return list(filter(lambda x:x % b ==0,a))
    
#3.构造filter函数
def filter1(f,xs):
    l = []
    for x in xs:
        if f(x):
            l.append(x)
    return l

    

