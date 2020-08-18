import board
import digitalio
import storage

def switch_filesystem():
    """Method to enable file IO on the internal storage of the microcontroller"""

    # Detect if the console is connected
    # NOTE: This is a bad indicator of if the filesystem should be readonly.
    # There is potential to lock the USB interface out disabling updates.
    # print("USB Status was: {0}".format(supervisor.runtime.serial_connected))

    # A more reliable method is to use a switch, I attached on to D2 input simply
    # because it was easy to solder in place and use the ground wire used for the
    # gyro sensor
    switch = digitalio.DigitalInOut(board.D2)
    switch.direction = digitalio.Direction.INPUT
    switch.pull = digitalio.Pull.UP

    # If the D2 switch is connected to ground with a wire
    try:
        if switch.value:
            print("Remounting Filesystem for readonly")
            storage.remount("/", readonly=True)
        else:
            print("Remounting Filesystem for write")
            storage.remount("/", readonly=False)
    except RuntimeError as e:
        print("No change to filesystem. {}".format(e))

    switch.deinit()

# At boot, call this method to configure the read/write access to the filesystem.
switch_filesystem()