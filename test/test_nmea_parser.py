import unittest

from common.parser_utils import nmea_parser
from lib import NMEASingleton
from lib.common.inlet_factory import InletFactory


class TestNMEAParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.singleton = NMEASingleton()

    def test_nmea_logfile(self):
        inlet = InletFactory.create_executor('log')
        self.assertIsNotNone(inlet.read(), "Unable to read log file")

    def test_nmea_uart(self):
        inlet = InletFactory.create_executor('uart')
        self.assertIsNotNone(inlet.read(), "Unable to UART")

    def test_nmea_log_parser(self):
        satellite_data = None
        ttff = None
        inlet = InletFactory.create_executor('log')
        for line in inlet.read():
            # add a until function with a timeout.
            if not line:
                break
            satellite_data, ttff = nmea_parser(line)

        self.assertIsNotNone(satellite_data, "Invalid satellite data")

if __name__ == '__main__':
    unittest.main()
