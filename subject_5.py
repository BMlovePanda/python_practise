'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''
'''
解题思路：
0x0 将输入放到list中，直接sorted貌似就行
~~0x1 也可以挨个比较，毕竟就只有三个数~~
0x1 直接修改成输入任意数组进行排序
0x2 使用try判断输入，屡试不爽啊
'''
import os
def num_sort(input_number):
    try:
        input_list_format = map(int,input_number.split(','))
        return sorted(input_list_format)
    except:
        return None
if __name__ == "__main__":
    input_list = input("请输入需要排序的数字，格式为'a,b,c,....':")
    result = num_sort(input_list)
    if result != None:
        print(result)
    else:
        print("您输入的内容有误!")
