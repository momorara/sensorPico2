"""
 2023/10/29
    渡された引数(秒)buzzerを鳴らします。
   v1.0
"""
from machine import Pin, time_pulse_us
import utime

# トリガーピンとエコーピンのピン番号
trigger_pin = Pin(12, Pin.OUT)
echo_pin = Pin(11, Pin.IN)

def measure_distance():
    # トリガーピンを10μsのパルスでHIGHにする
    trigger_pin.high()
    utime.sleep_us(10)
    trigger_pin.low()
    # エコーピンがHIGHになるまでの時間を測定
    pulse_duration = time_pulse_us(echo_pin, 1, 1000000)
    # 距離を計算（音速は約340m/s）
    distance = int((pulse_duration / 2) * 0.034 *10)/10
    return distance

def main():
    for _ in range(5):
        # 距離を測定
        dist = measure_distance()
        print(f"距離: {dist} cm")
        utime.sleep(1)  # 1秒待つ

if __name__=='__main__':
    main()
