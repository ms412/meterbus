
import serial
import time
from datetime import datetime



class serialIf(object):

    def __init__(self):

        self._if = None

    def _inter_byte_timeout(self,baudrate):
        definition = {
            300: 0.12,
            600: 0.60,
            1200: 0.4,
            2400: 0.2,
            4800: 0.2,
            9600: 0.1,
            19200: 0.1,
            38400: 0.1,
        }

        return definition.get(baudrate, None)

    def connect(self,device,baudrate):
        ibt = self._inter_byte_timeout(baudrate)
        try:
            self._if = serial.serial_for_url(device,baudrate,8,'E',1,inter_byte_timeout=ibt,timeout=1)

        except serial.serialutil.SerialExecption as e:
            print(e)

        return True

    def mbusWrite(self,data):
        self._if.write(bytearray(data))
        return True

    def mbusRead(self,size):
        frame = bytearray()

        while True:
            byte = self._if.read(size)
            frame.extend(byte)
            print(frame)
            if len(frame) == size:
                return frame

        return frame


        #   print(bytearray(_frame))
        self.mbusWrite(_frame)







if __name__ == '__main__':
    mbus = serialIf()
    mbus.connect('/dev/ttyUSB1',2400)
    #mbus.setTimeDate()
   # mbus.addressChange(0x03,0x10)
   # mbus.dateChange()
   # mbus.setConter()
    #mbus.readValue()
   # mbus.resetAppl()
    mbus.readCounter()