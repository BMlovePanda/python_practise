'''
题目：暂停一秒输出。
'''
'''
解题思路：
0x0 python中time模块的使用
0x1 用time的localtime输出一个时间戳，没有格式化，凑合能看就行
'''
import time
pause_time = 1
print(f"[{time.localtime()[:6]}] 程序运行开始，将在{pause_time}秒后输出新一行内容!")
time.sleep(pause_time)
print(f"[{time.localtime()[:6]}] 暂停后的新内容...")
print(f"[{time.localtime()[:6]}] 程序结束")