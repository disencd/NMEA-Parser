import serial


class NMEAMissingRegistryError(FileNotFoundError):
    pass


class NMEASerialException(serial.SerialException):
    pass


class NMEAValueError(ValueError):
    pass
