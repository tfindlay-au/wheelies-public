import os

# Super Simple Logger for file io
# See also adafruit_logging
class FileLogger:

    def __init__(self, filename, size_limit):
        """Create an instance.

        :param filename: the name of the file to which to write messages

        """
        self._filename = filename
        self._size_limit = size_limit

    def _space_check(self):
        """Internal Utility to retrieve the size of a file on the filesystem.

        :return: numeric size in bytes of the file
        """
        result = os.stat(self._filename)

        # result = (32768, 0, 0, 0, 0, 0, 209, 946684836, 946684836, 946684836)
        # Size of file was 206 bytes

        return result[6]

    def _get_overwrite_mode(self):
        """Internal Method to evaluate if the configured file size limit has been reached/exceeded

        :return: Access mode "w" overwrites the file, "a+" appends to the file
        """
        # TODO Seems expensive to check the size of the file every time a line is written
        if self._space_check() > self._size_limit:
            # TODO Is there a better way to retain the history without truncating the file ?
            return "w"
        else:
            return "a+"

    def emit(self, msg):
        """Generate the message and write it to the UART.

        :param msg: The core message
        """
        with open(self._filename, self._get_overwrite_mode()) as fp:
            fp.write(msg)
            fp.flush()
