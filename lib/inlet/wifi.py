from lib.common.inlet_factory import InletFactory
from lib.inlet import InletBot


@InletFactory.register('wifi')
class Wifi(InletBot):
    def __init__(self):
        super().__init__()

    def read(self):
        print("Wifi mode")
        raise NotImplementedError("TODO")
