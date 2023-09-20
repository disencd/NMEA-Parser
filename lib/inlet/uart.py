"""
### Deliverable 2:
This stream of NMEA sentences comes in over UART at 9600N1. How would you think about
writing a program that parses a live stream of NMEA data? What modules would you use? How
would you determine the start/end of a GPS scan?
"""
from lib.common.inlet_factory import InletFactory
from lib.inlet import InletBot
from lib import NMEAValueError, NMEASerialException
import serial
import config
import logging

log = logging.getLogger(__name__)


@InletFactory.register('uart')
class UART(InletBot):

    def __init__(self):
        super().__init__()
        self.data = config.CONFIG['log']

    def read(self):
        print("UART mode")
        _port = int(self.data.get('port'))
        _timeout = int(self.data.get('timeout'))
        try:
            serial_port = serial.Serial('COMx', baudrate=_port, timeout=_timeout)
            while True:
                yield serial_port.readline().decode('utf-8')

        except NMEASerialException as e:
            raise RuntimeError(f"Possible Reasons: Device can not be found or configured!!!! - {e}")
        except NMEAValueError as e:
            raise RuntimeError(f"Possible Reasons: Baud rate or Data bits are out of range!!!! - {e}")