"""
 2023/10/28
   傾きセンサーの状態でLED1,LED2 を点灯、消灯させる。
   玉が離れたら1、付いたら0
"""
import machine
import time

tilt = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
led1 = machine.Pin(16, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)

def tilt_read():
    return tilt.value()

def main():

    while True:
        sense = tilt()
        if sense == 1:
            led1.on()
            led2.off()
        if sense == 0:
            led2.on()
            led1.off()           

        print(sense)
        time.sleep(0.1)

if __name__=='__main__':
    main()
