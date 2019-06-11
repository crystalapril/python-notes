# example 1.1  摄氏度C和华氏度F之间相互转换
# C= （F-32）/1.8
# F= C*1.8 +32
TempStr = input("请输入带有符号的温度值：")
if TempStr [-1] in ['F','f']:
    C =(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) +32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
    
# example 2.1 绘制蟒蛇 
import tutle as t
t.setup(650,350,200,200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("purple")
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(16,180)
t.fd(40 * 2/3)
t.done()

#example 3.1 天天向上的力量
#每天进步1%的努力，一年之后的成长是 1.01 的 365次方=37.78

dayup=1.0
dayfactor= 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup= dayup*(1-0.01)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量：{:.2f}".format(dayup))   
#最后得到的结果是4.63，仅仅是工作日努力，比每一天都努力积累的效果要差

#example 3.2 天天向上的力量
# 如果要达到每天努力的效果，工作日需要进步的程度是多大才行
def dayUP(df):
    dayup=1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup= dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor= 0.01
while dayUP(dayfactor) < 37.37: 
    dayfactor +=0.001
    print("工作日的努力参数是：{:.3f}".format(dayfactor))  
# 最后求得是0.019

#example 4.1 文本进度条
import time
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale +1) :
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale )*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-')) 

# example 4.2  身体质量指数BMI
height,weight=eval(input("请输入身高（米）和体重（公斤）[逗号隔开]:"))
bmi = weight / pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who,nat ="",""
if bmi <18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    who,nat="正常","正常"
elif 24<=bmi<25:    
    who,nat="正常","偏胖"
elif 25<=bmi<28:
    who,nat="偏胖","偏胖"
elif 28<=bmi<30:
     who,nat="偏胖","肥胖"
else:
    who,nat="肥胖","肥胖"
print("BMI指标为：国际'{0}',国内'{1}''".format(who,nat))    
    
# exmaple 4.3 圆周率的计算
#4.3.1 利用数学公式
pi = 0
N =100
for k in range(N):
    pi +=1/pow(16,k)*( \
         4/(8*k+1)-2/(8*k+4) - \
         1/(8*k+5) -1/(8*k+6))
print("圆周率值是：{}".format(pi))

#4.3.2 蒙特卡洛模拟（散点）
from random import random
from time import perf_counter
DARTS =1000*1000
hits =0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist =pow(x**2+ y**2,0.5)
    if dist <=1.0:
        hits +=1
pi= 4 *(hits /DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))


