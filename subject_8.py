'''
题目：输出 9*9 乘法口诀表。
'''
'''
解题思路：
0x0 遍历二维数组1-9；
0x1 计算两个数的乘积
0x2 如何比较好看的输出结果
    1*1=1
    2*1=2 2*2=4
    3*1=3 3*2=6 3*3=9
    .....
0x3 用到print的格式化输出，end参数
'''
import string,itertools
def multiplication_table():
    for x in range(1,10):
        for y in range(1,x+1):
            print(f"{x}x{y}={x*y}",end="\t")
        print()
    
if __name__ == "__main__":
    multiplication_table()