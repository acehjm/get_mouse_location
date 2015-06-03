#encoding=utf-8
from ctypes import *
#import win32api, win32con
import time
#装载windows dll
User32dll = windll.User32
#print windll.User32
"""
获取鼠标在屏幕中的位置
python byref关键字,送数据结构指针空间的关键字
windows api:
GetCursorPos(x,y)
SetCursorPos(x,y)
"""
class POINT(Structure):
        _fields_ = [
                ("x", c_ulong),
                ("y", c_ulong)
                ]

def timer_Tick():
        point = POINT()
        User32dll.GetCursorPos(byref(point))
        print ('current Pos:', point.x, point.y)

if __name__ == '__main__':
        i = 0
        maxcount = 20
        while i < maxcount:
              timer_Tick()
              time.sleep(2)
              i += 1
