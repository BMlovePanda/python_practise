'''
题目：暂停一秒输出，并格式化当前时间。
'''
'''
解题思路：
0x0 与上一道题目一样，只不过格式化一下输出时间而已
0x1 把上一道题目的输出时间用time.strftime格式化就行
'''
import time
pause_time = 1
print(f"{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))} 当前时间")
time.sleep(pause_time)
print(f"{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))} 一秒后，程序结束")