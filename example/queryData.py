
from meterbus.meterbus import meterbus


class queryData(object):
    def __init__(self):
        self._mbus = None

    def connect(self):
        self._mbus = meterbus()
        self._mbus.connect('/dev/ttyUSB1', 2400)
    def get(self):
        self._mbus.readData(0x10)
        pass

if __name__ == "__main__":
    example = queryData()
    example.connect()
    example.get()