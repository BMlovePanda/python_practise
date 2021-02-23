'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
'''
解体思路:
0x0 题目没给出数字范围，所以如果用穷举的方式，等数字极大的时候，基本就GG了
0x1 设x，加100开方，再加168开放，可以用gmpy2库的iroot函数，计算是否可以被完全开方
0x2 官方的wp，是通过上面的要求列方程，然后穷举解方程，即完全使用标准库去做。
'''
import gmpy2
max_edge = 10000
a = 100
b = 168
result = []
for i in range(1,max_edge+1):
    if gmpy2.iroot((i + a),2)[1] and gmpy2.iroot((i + a + b),2)[1]:
        result.append(i)
if len(result) > 0:
    print(f"{max_edge}以内,符合要求的数共有{len(result)}个,分别为:{result}")

