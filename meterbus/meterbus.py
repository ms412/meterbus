
from meterbus.api.application import application
from meterbus.api.frame import frame
from meterbus.api.pysicalIf import serialIf
#from meterbus.api.bitoperation import bitoperation


class meterbus(application,
               frame,
               serialIf):
#               bitoperation):

    pass
