'''
买水果
选食材
机场大吧人数
普通巴士人数
账单 有无初始值
理财 有无初始值
len
reverse string list
min
frequency
reduce
'''

from functools import reduce

# answer1： sum of fruit you buying 每个类别中的子类别（梨：香梨、鸭梨）都买一个
apple=2   #苹果种类有2个
banana=3
pear=4
cherry=5
alist=[apple,banana,pear,cherry]
#A1.1
def total1(alist):
  t=0
  for x in alist:
    t +=x
  return t
#A1.2
total1=reduce(lambda x ,y :x+y,alist)
#A1.3
total1=reduce(lambda x ,y :x+y,alist[1:],apple) 

# answer2：sum of food material you choose (each kind choose one) 每个类别选一个
ginger =2  #生姜有两种
onion =3
egg = 4
tomato = 5
blist = [apple,banana,pear,cherry]
#A2.1
def total2(blist):
    t=1
    for x in blist:
        t *= x
    return t
#A2.2
total2=reduce(lambda x ,y :x*y,blist)
#A2.3
total2=reduce(lambda x,y :x*y ,blist[1:],ginger)

# answer3 : number of remaining passengaer on airport bus 每站剩余乘客人数(只下不上）
jiangbei_station= 20   # (江北机场站上车 20 人）
central_park_station = 5   #（中央公园站下车 5 人）
guanyinqiao_station =  6   #（观音桥站下车 6 人）
jiefangbei_station = 9    #（解放碑站下车 9 人，全部下车）
clist=[central_park_station,guanyinqiao_station,jiefangbei_station]
#A3.1
def passenger1(jiangbei_station,clist):
    p=jiangbei_station
    for x in clist:
        p -= x
    return p
#A3.2
passenger1 = reduce(lambda x ,y: x-y,clist,jiangbei_station)
#注意这里x-y的顺序，不能是y-x，因为x代表着初始值 jiangbei_station

# answer4: number of passenger on  bus 每站乘客人数(假设初始值为0）
jiefangxilu_station = 10
niujiaotuo_station = -6
shangqingsi_station = 18
honghuxilu_station = -20
dlist=[jiefangxilu_station,niujiaotuo_station,shangqingsi_station,honghuxilu_station]
#A4.1
def passenger2(dlist):
    p = 0
    for x in dlist:
        p += x
    return p
#A4.2
passenger2 = reduce(lambda x,y :x+y ,dlist)

#answer5 : ali bills 每月账单
income = 9000
meal_fee = -1500
travelling_expense = -600
telephone_fee = -200
elist=[income,meal_fee,travelling_expense,telephone_fee]
#A5.1
def bill(elist):
    b = 0
    # 上期余额（如有）
    #b = 2000  
    for x  in elist:
        b += x
    return b
#A5.2
bill=reduce(lambda x,y:x+y,elist)
#5.3
bill=reduce(lambda x,y:x+y,elist,2000)

#answer6:  financial product yield 理财产品收益率
Q1 = 1.01
Q2 = 0.99
Q3 = 0.98
Q4 = 1.03
flist=[Q1,Q2,Q3,Q4]
#A6.1
def yield1(flist):
    y=1
    # 初始值为1.04
    # y = 1.04
    for x in flist:
        y *= x
    return y   
#A6.2
yield1= reduce(lambda x,y: x*y,flist)
#A6.3
yield1= reduce(lambda x,y: x*y,flist,1.04)

#answer7 : 构造len函数
glist=['a','b','c','d']
#A7.1
def len1(glist):  
    a =0
    for x in glist:
        a +=1
    return a
#A7.2
len1=reduce(lambda x,y: x+1 ,glist,0)
#注意，reduce里面的y没有被用到（因为lambda函数中没有y，只有x+1），但是y不能去除，因为reduce必须接受2个参数

#answer8 : 构造 reverse 函数
#A8.1
rlist=['a','b','c','d']
def reverse1(rlist):
    r=[]
    for x in rlist:
        r = [x]+r
    return r 
#A8.2
rlist2=reduce(lambda x,y:[y]+x,rlist,[])
#注意： 1.[y]是对y构造成list，直接用list（y），可能会造成y的拆分，如list('ab')=['a','b'],而['ab']则不会
#      2.reduce函数不仅仅可以返回一个值，也可以返回一个序列
#A8.3
str1='abcd'
def reverse1(str1):
    a=''
    for x in str1:        
        a = x+a
    return a
#A8.4
str2=reduce(lambda x,y:y+x,str1,'')

#answer9 : 构造最小值函数
mlist=[1,2,3,4,5,6]
#A9.1
def minimum1(xs):
    current_minimum = xs[-1]
    for x in xs[:-1]:        
        current_minimum = x if current_minimum > x else current_minimum
    return current_minimum
#A9.2
minimum2=reduce(lambda x,y:x if y>x else y  ,mlist[:-1],mlist[-1])
#A9.3
minimum3=reduce(lambda x,y:x if y>x else y  ,mlist[1:],mlist[0])
#注意： reduce接收的函数中也可以有条件分支语句，与其他函数相同

#answer10 : 构造 frequency 函数
flist = ['a','a','b','b','b','c']
#应返回 [('a',2),('b',3),('c',1')]
#A10.1
def frequency1(a):
    b=list(set(a))
    c=sorted(b,key=a.index)
    d=[]
    for x in c:
        d += [tuple((x,a.count(x)))]
    return d
#A10.2
frequency2 = reduce(lambda x,y:x+[tuple((y,flist.count(y)))],sorted(list(set(flist)),key=flist.index),[])

#answer11 : 构造 reduce 函数
def r_reduce(f1,rrlist,rr=0):
    for x in rrlist:
        rr = f1(rr,x)
return rr
