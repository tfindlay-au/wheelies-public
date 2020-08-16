import storage
import supervisor

# Detect if the console is connected
usb_status = supervisor.runtime.serial_connected
print("USB Status: {0}".format(usb_status))

# Configure the filesystem for writing
if usb_status:
    print("Remounting Filesystem for readonly")
    storage.remount("/", False)
else:
    print("Remounting Filesystem for write")
    storage.remount("/", True)
