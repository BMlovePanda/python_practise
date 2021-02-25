'''
题目：斐波那契数列。
'''
'''
解题思路:
0x0 输入某个数值，然后输出这个数值长度的斐波那契数列
0x1 建立一个列表，前两个元素为0和1
0x2 根据输入的长度，循环，将前两个数相加得到新的数值并填到列表中
0x3 输出的列表，剔除首个元素0
0x4 根据assert判断输入的数据满足要求
'''
def fibonaci(INPUT):
    try:
        fibonaci_array_len = int(INPUT)
        assert(fibonaci_array_len >= 3)
    except:
        return None
    a = 0
    b = 1
    fibonaci_array = [a,b]
    for i in range(2,fibonaci_array_len+1):
        fibonaci_array.append(fibonaci_array[i-2] + fibonaci_array[i-1])
    return fibonaci_array[1:]
    
if __name__ == "__main__":
    INPUT = input("请输入斐波那契数列的长度，大于等于3:")
    result = fibonaci(INPUT)
    if result != None:
        print(f"斐波那契数列如下:\n{result}")
    else:
        print("您输入的长度有误！")