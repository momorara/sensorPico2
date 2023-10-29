"""
 2023/10/29
    渡された引数(秒)buzzerを鳴らします。
   v1.0
"""
import machine
import time

buzz = machine.Pin(19, machine.Pin.OUT)

def buzzer(beep):
    buzz.on()
    time.sleep(beep)
    buzz.off()

def main():
    buzzer(0.3)
    # LED2onoff()
    # while True:
    #     LED1onoff()
    #     LED2onoff()
    #     if SW1.value() == 0:
    #         led1.on()
    #         led2.on()
    #         time.sleep(2)
    #     if SW2.value() == 0:
    #         for _ in range(8):
    #             led1.on()
    #             led2.on()
    #             time.sleep(0.1)
    #             led1.off()
    #             led2.off()
    #             time.sleep(0.1)

if __name__=='__main__':
    main()
