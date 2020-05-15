
import time
import enum
import datetime
from meterbus.api.frame import frame

class application(object):

    def __init__(self):
        pass

    def resetApplication(self,nodeId):

        _body = [0x53, nodeId, 0x50]

        self.SND_UD(_body)
        if not self.ACK():
            print('FAILED')
            return False

        return True

    def setTimeDate(self,nodeId):
        #type F 4Byte
        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        y = datetime.now().year
        m = datetime.now().month
        d = datetime.now().day
        h = datetime.now().hour
        M = datetime.now().minute

        print(y, m, d, h, M)

        #minute
        int0 = M | 0x80

        #hour
        int1 = h | 0x80

        # highyear + month
        y = (y % 100) << 5
        highYear = ((y & 0xF00) >> 4)
        print(highYear,hex(highYear))
        int3 = highYear | m
        print(int3,hex(int3))

        #lowyear + day
        lowYear =  y & 0xff
        int2 = lowYear | d

        _body = [0x53, nodeId, 0x51, 0x04, 0x6d, int0, int1, int2, int3]

        self.SND_UD(_body)
        if not self.ACK():
            print('FAILED')
            return False

        return True

    def changeAddress(self,oldId,newId):

        _body = [0x53,oldId,0x51,0x01,0x7a,newId]

        self.SND_UD(_body)
        if not self.ACK():
            print('FAILED')
            return False







    def readData(self,nodeId):
        print('ddd',nodeId)
        _body = [0x7b, nodeId]

        self.REQ_UD2(_body)
        _result = self.RSP_UD()
        print(_result)

        return False