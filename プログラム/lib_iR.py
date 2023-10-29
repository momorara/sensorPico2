"""
 2023/10/28
    リモコンの赤外線を感知すると反応します

"""

from machine import Pin
import utime

# 赤外線センサーの出力ピンをGP2に接続した場合
ir_sensor_pin = Pin(10, Pin.IN)

while True:
    if ir_sensor_pin.value() == 0:
        print("物体が検出されました")
    else:
        print("物体は検出されていません")
    utime.sleep(1)  # 1秒待つ


# import machine
# import time

# tilt = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
# led1 = machine.Pin(16, machine.Pin.OUT)
# led2 = machine.Pin(17, machine.Pin.OUT)

# def tilt_read():
#     return tilt.value()

# def main():

#     while True:
#         sense = tilt()
#         if sense == 1:
#             led1.on()
#             led2.off()
#         if sense == 0:
#             led2.on()
#             led1.off()           

#         print(sense)
#         time.sleep(0.1)

# if __name__=='__main__':
#     main()
