from psutil import *
from time import sleep
# cpu_percent()可以获取cpu的使用率，参数interval是获取的间隔
print("CPU使用率：",cpu_percent())

# virtual_memory()可以获取内存使用情况，返回一个元组，其中第三个是内存的使用率
print("内存使用情况：",virtual_memory())

# virtual_memory()[2]可以获取内存的使用率
print("内存率：",virtual_memory()[2])
while   True:
    print("CPU使用率：",cpu_percent())
    print("内存率：",virtual_memory()[2])
    sleep(1)    
