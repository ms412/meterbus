
import time
import binascii
import datetime
from datetime import datetime
#from meterbus.api.bitoperation import bitoperation
from meterbus.api.dataframe import helper

class frame(object):

    def __init__(self):
        pass

    def _checksum(self,body):
        _temp = 0
        for item in body:
            _temp = _temp + item
      #  print('checksum',x)
        return _temp % 256

    def _statusByte(self,byte):
        _status = {}
        if (byte & 0x03):
            _status['ERROR'] = 'YES'
        else:
            _status['ERROR'] = 'NO'

        _statusList = []
        if (byte & 0x04):
            _statusList.append('power supply low')
        elif (byte & 0x08):
            _statusList.append('permanent error')
        elif (byte & 0x10):
            _statusList.append('temporary error')


        _status['STATUS'] = _statusList

        return(_status)


    def ACK(self):

        _timeout = time.time() + 5
        while time.time() < _timeout:
            _frame = self.mbusRead(1)
            if _frame[0] == 0xe5:
                print('OK')
                return True
            else:
                print('NOK')
                time.sleep(1)

        return False

    def SND_UD(self, body):
        _frame =[]
        _start = 0x68
        _stop = 0x16
        _size = len(body)
        _header =[_start, _size, _size, _start]
        print ('_header', _header)

        _frame = _header + body + [self._checksum(body)] + [_stop]
        print(_frame)

        self.mbusWrite(_frame)

        return True

    def REQ_UD2(self, body):
        _frame = []
        _start = 0x10
        _stop = 0x16
        _size = len(body)
        _header = [_start]
        print('_header', _header)

        _frame = _header + body + [self._checksum(body)] + [_stop]
        print(_frame)

        self.mbusWrite(_frame)

        return True

    def RSP_UD(self):

        print('ggg')
        _timeout = time.time() + 5
        while time.time() < _timeout:
            _frame = self.mbusRead(4)
            _size = _frame[1] + 2
            break

        _timeout = time.time() + 5
        while time.time() + _timeout:
            _frame2 = self.mbusRead(_size)
            if 0x16 == _frame2[-1]:
                print('Frame complete')
                break
       # y = 0
       # for x in _frame2:
       #     if y == 8:
       #         print(n)
       #         n = ' '
       #         y = 0

       #     y = y+ 1
        #    n = n + ',' + "".join('{:02x}'.format(x))
       # print(n)

        if _frame2[-2] == self._checksum(_frame2[0:-2]):
            print('Checksum OK')

        _result = {}

        _result['IdentNr']  = binascii.hexlify(bytearray(_frame2[3:7]))
        _result['Manufr'] = binascii.hexlify(bytearray(_frame2[7:9]))
        _result['Device'] = _frame2[9]
        _result['Medium'] = _frame2[10]
        _result['Status'] = self._statusByte(_frame2[11])
        #self._statusByte(_frame2[11])
        _result['Signatur'] = binascii.hexlify(bytearray(_frame2[12:15]))
        _result['Data'] = _frame2[15:-2]

        x =helper()
        xx = x._dataInformationBlock(_frame2[15:-2])
        print(xx)

        return _result



