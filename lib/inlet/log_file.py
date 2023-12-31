from lib.common.inlet_factory import InletFactory
from lib.inlet import InletBot
from lib.config import CONFIG


@InletFactory.register('log')
class LogFile(InletBot):
    def __init__(self):
        super().__init__()
        self.data = CONFIG['log']

    def read(self):
        print(f"Log file mode {self.data['file']}")
        # Open the file for reading
        with open(self.data['file'], 'r') as nmea_file:
            while True:
                yield nmea_file.readline()
