'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
'''
解题思路:
0x0 如果可以用非标准函数，应该直接可以求出来，不知道datetime或者time函数能不能变相实现该功能
0x1 先算出某日在当月的第几天，再加上前面月份的天数
0x2 需要考虑输入日期的年份是否为闰年
0x3 通过time函数校验输入数据，并且可以将输入分割成年，月，日，即可判断闰年，又可根据月份天数列表快速计算出所在天数
'''
import time
def caculate_date(DATE):
    try:
        DATE_FORMAT = time.strptime(DATE,"%Y-%m-%d")
    except:
        return None
    Month_day_counts_array = [31,28,31,30,31,30,31,31,30,31,30,31]
    #print(sum(Month_day_counts_array))
    if ((DATE_FORMAT[0] % 4 == 0) and (DATE_FORMAT[0] % 100 != 0)) or (DATE_FORMAT[0] % 400 == 0):
        Month_day_counts_array[1] = 29
    date_count = sum(Month_day_counts_array[:DATE_FORMAT[1]-1]) + DATE_FORMAT[2]
    return date_count
if __name__ == "__main__":
    DATE = input("请输入日期，格式yyyy-mm-dd:")
    result = caculate_date(DATE)
    if result != None:
        print(f"您输入的日期是所在年份的第{result}天")
    else:
        print("您输入的日期有误")