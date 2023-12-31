#!/usr/bin/python                             
#-*- coding:utf-8 -*-               
import time
import concurrent.futures
import threading

import RPi.GPIO as GPIO               
          
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106


led=26                                #根据自己LED灯接的引脚配置
bim=16                                #根据自己蜂鸣器接的引脚配置
GPIO.setwarnings(False)               #禁用警告
GPIO.setmode(GPIO.BCM)                #使用BCM编码的引脚号
GPIO.setup(led,GPIO.OUT)              
GPIO.setup(bim,GPIO.OUT) 


serial = i2c(port=1, address=0x3C)    # 初始化设备，这里改ssd1306, ssd1325, ssd1331, sh1106
device = ssd1306(serial)

model_exit_flag=None

def Led(a):
    while not model_exit_flag.is_set():
       GPIO.output(led,GPIO.HIGH)
       time.sleep(a)
       if a != 0:
          GPIO.output(led,GPIO.LOW) 
          time.sleep(a)
    GPIO.output(led,GPIO.LOW) 
       
def Bim(a):
    while not model_exit_flag.is_set():
       GPIO.output(bim,GPIO.HIGH)
       time.sleep(a)
       if a != 0:
          GPIO.output(bim,GPIO.LOW) 
          time.sleep(a)
    GPIO.output(bim,GPIO.LOW)     

def main():
    global model_exit_flag
    print("系统开始自检：请注意状态是否正确")
    print("oled测试：")
    # 调用显示函数
    with canvas(device) as draw:
     draw.rectangle(device.bounding_box, outline="white", fill="black")
     draw.text((30, 20), "Hello World", fill="white")
    # 延时显示10s
    time.sleep(1)
    print("灯光测试")
    GPIO.output(led,GPIO.HIGH)     #引脚拉高
    time.sleep(1)                 #延时1s
    GPIO.output(led,GPIO.LOW)      #引脚拉低
    time.sleep(1)                 #延时1s
    print("蜂鸣器测试")
    GPIO.output(bim,GPIO.HIGH)     #引脚拉高
    time.sleep(1)                 #延时1s
    GPIO.output(bim,GPIO.LOW)      #引脚拉低
    time.sleep(1)                 #延时1s
    print("全部测试：")
    
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
       model_exit_flag = threading.Event()
       current_thread = None

       current_thread = executor.submit(Led,0.8)
       current_thread = executor.submit(Bim,0.5)    
       time.sleep(1)
       print("???")
       model_exit_flag.set()

if __name__ == '__main__':
    print("系统启动")
    main()







