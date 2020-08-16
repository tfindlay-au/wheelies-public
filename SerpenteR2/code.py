import board
from digitalio import DigitalInOut, Direction
import time
import busio
import mpu9250

def write_data(value):
    try:
        with open("/output.txt", "a") as fp:
            fp.write("{}".format(value))
            fp.flush()

            blink_color(board.LED_B)

    except OSError as e:
        print("OS Error: {0}".format(e.strerror))
        blink_color(board.LED_R)


def blink_color(led_ref):
    led = DigitalInOut(led_ref)
    led.direction = Direction.OUTPUT
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    led.deinit()


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = mpu9250.MPU9250(i2c)

    while True:
        blink_color(board.LED_G)

        _acceleration = mpu.acceleration
        _gyro = mpu.gyro
        _temperature = mpu.temperature

        print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s" % _acceleration)
        print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s" % _gyro)
        print("Temperature: %.2f C" % _temperature)

        write_data(_acceleration)

if __name__ == "__main__":
    main()
