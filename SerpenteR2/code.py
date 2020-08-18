import board
from digitalio import DigitalInOut, Direction
import time
import busio
import mpu9250
import log

# Setup the log file, max 1MB
data_log = log.FileHandler("/output.txt", 1000000)

def write_data(values):
    """
    This function controls the output using the log emitter, but as a fallback uses the console
    This also uses the LED as an indicator if it logging successfully
    :param values:
    :return:
    """
    # Split elements up separated by comma
    message = "{}".format(",".join(values))

    try:
        # Try to log them to file, normal operation
        data_log.emit(message + '\n')
        blink_color(board.LED_B)
    except OSError:
        # If the USB console is active, just display on console output
        print(message)
        blink_color(board.LED_R)


def blink_color(led_ref):
    """
    Function to control the LED and perform a simple blink
    Total delay = 1 second
    This encapsulates activating the pin and de-activating it to avoid color mashing
    :param led_ref:
    """
    led = DigitalInOut(led_ref)
    led.direction = Direction.OUTPUT
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    led.deinit()


def merge_tuples(*tuples):
    """
    Utility method to merge a number of tuples into a list.
    To aid output, this also converts numbers into strings for easy output
    :param tuples:
    :return: List[String]
    """
    return [str(j) for i in tuples for j in (i if isinstance(i, tuple) else (i,))]


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = mpu9250.MPU9250(i2c)

    while True:
        blink_color(board.LED_G)

        _acceleration = mpu.acceleration
        _gyro = mpu.gyro
        _temperature = mpu.temperature

        # Assemble all the data to capture
        # counter, accX, accY, accZ, gyroX, gyroY, gyroZ, temp
        # TODO Nicer to use a dictionary here and use that to print a header row
        payload = merge_tuples(
            str(time.monotonic()),
            _acceleration,
            _gyro,
            _temperature
        )

        write_data(payload)

if __name__ == "__main__":
    main()
