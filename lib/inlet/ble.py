from lib.common.inlet_factory import InletFactory
from lib.inlet import InletBot


@InletFactory.register('ble')
class BLE(InletBot):
    def __init__(self):
        super().__init__()

    def read(self):
        print("Ble mode")
        raise NotImplementedError("Ble TODO")
