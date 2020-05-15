
from enum import Enum

class FunctionType(Enum):
    INSTANTANEOUS_VALUE = 0
    MAXIMUM_VALUE = 1
    MINIMUM_VALUE = 2
    ERROR_STATE_VALUE = 3
    SPECIAL_FUNCTION = 4
    SPECIAL_FUNCTION_FILL_BYTE = 5
    MORE_RECORDS_FOLLOW = 6

class helper(object):

    def _dataInformationBlock(self,data):
        print('dd',data)
      #  data = {}
        header = {}
        _EXTENSION_BIT_MASK = 0x80  # 1000 0000
        _FUNCTION_MASK = 0x30  # 0011 0000
        _DATA_FIELD_MASK = 0x0F  # 0000 1111
        _MORE_RECORDS_FOLLOW = 0x1F  # 0001 1111
        print(data[1] )


        header['FUNCTION'] = FunctionType((data[0] & _FUNCTION_MASK) >>4)
        header['DATASIZE'] = data[0] & _DATA_FIELD_MASK
        header['EXTENSION'] = data[0] & _EXTENSION_BIT_MASK
        _extension = data[1] & _EXTENSION_BIT_MASK
        _dive = []
        n = 1
        while _extension:
            _dive.append(data[n])
            _extension = data[n] & _EXTENSION_BIT_MASK
            n = n + 1
        header['DIVE'] = _dive

        header['VIF'] = data[n]
        _vife = []

        _extension = data[n] & _EXTENSION_BIT_MASK
        while _extension:
            _vife.append(data[n])

        header['VIFE'] = _vife

        _databyte = []
        for i in range(header['DATASIZE']):







        print('Header',header)