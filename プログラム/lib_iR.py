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
        print("信号が検出されました")
    #else:
    #    print("物体は検出されていません")
    utime.sleep( 0.1)  # 1秒待つ