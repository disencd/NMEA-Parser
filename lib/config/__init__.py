import os

from lib.common.singleton import NMEASingleton

singleton = NMEASingleton()

CONFIG = {
    "uart": {
        "port": "9600",
        "timeout": "1"
    },
    "log": {
        "file": f"{singleton.data_dir}{os.sep}stce_nmea_log.txt"
    },
    "ble": {
        # TODO
    },
    "wifi": {
        # TODO
    }
}
