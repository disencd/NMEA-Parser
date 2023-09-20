from lib.common.inlet_factory import InletFactory
from lib.inlet import InletBot


@InletFactory.register('wifi')
class Wifi(InletBot):
    def __init__(self):
        super().__init__()
        self._config = self.config('wifi')

    def read(self):
        print("Wifi mode")
        raise NotImplementedError("TODO")
