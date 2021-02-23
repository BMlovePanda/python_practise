'''
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
'''
解题思路:
0x0 提成区域分为六个区间
    (0,10w)
    (10w,20w)
    (20w,40w)
    (40w,60w)
    (60w,100w)
    (100w,)
0x1 根据输入，判断在哪个区几间，然后再将利润分别计算提成之后，相加
0x2 当然，还得写个判断输入正确的内容
    ~~判断输入是否为数字；
    ~~输入内容若为小数，则将输入分割之后判断小数点前后是否为数字
    ~~输入若为负数，好像就不用计算了。。。
    直接try float输入就好了，报错直接表示输入不正确
0x3 看了官方的程序，才写成现在这样，自己写的就奔着判断去了，果然不适合编程。。。。。。
'''
import os,string
def caculate_commission(INPUT):
    try:
        INPUT_float = float(INPUT)
    except:
        return None
    profit_array = [0,100000,200000,400000,600000,1000000]
    bonus_per = [0.1,0.075,0.05,0.03,0.015,0.01]
    commission = 0
    for i in range(len(profit_array)):
        commission += max(0,(INPUT_float - profit_array[::-1][i])) * bonus_per[::-1][i]
        INPUT_float -= max(0,(INPUT_float - profit_array[::-1][i]))
        #print(INPUT_float)
    return commission
if __name__ == "__main__":
    I = input("请输入您的利润总额:")
    result = caculate_commission(I)
    if result != None:
        print(f"您的提成共:{result}")
    else:
        print("您输入的金额有误")
