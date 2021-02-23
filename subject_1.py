'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
'''
解题思路：
0x0 四选三，然后剔除数字重读的的组合即可
0x1 四选三可以用到itertools库，但是itertools貌似不是标准库
0x2 如果有重复去重的话，长度就小于3
0x3 去重可以用list的set方法，这个方法貌似不是list特有，元组，字符串都可以用
'''
import os,itertools
orgin_list = ['1','2','3','4']
answer_list = []
for i in itertools.permutations(orgin_list,3):
    if len(set(i)) == 3:
        answer_list.append("".join(i))
print(f"答案共:{len(answer_list)}个")
print(answer_list)