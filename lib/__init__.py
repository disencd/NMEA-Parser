from lib.common.exceptions import NMEAMissingRegistryError, NMEAValueError, NMEASerialException

from lib.inlet.uart import UART
from lib.inlet.wifi import Wifi
from lib.inlet.ble import BLE
from lib.inlet.log_file import LogFile
from lib.common.singleton import NMEASingleton

class Inlets:
    """
    It encapsulates a supported list of inlets.
    """
    uart = 'uart'
    ble = 'ble'
    wifi = 'wifi'
    log = 'log'

    def __iter__(self):
        for attr in dir(self):
            if callable(getattr(self, attr)):
                continue

            if not attr.startswith("__"):
                yield attr

    @classmethod
    def lookup(cls, s):
        """takes a string and returns inlets type."""
        try:
            return getattr(cls, s)
        except KeyError:
            # this is important for masking python throw ugly exception to catch
            # and then instead raise ValueError
            raise ValueError(f"'{s}' is not a supported type")