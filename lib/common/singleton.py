import os
import subprocess


class NMEASingleton:
    top_dir = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(NMEASingleton, cls).__new__(cls)
            _dir = subprocess.check_output(
                "git rev-parse --show-toplevel",
                shell=True,
                text=True).strip()

            # Add any other initialization here
            cls.top_dir = _dir
            cls.data_dir = f"{cls.top_dir}{os.sep}data"
            cls.config_dir = f"{cls.top_dir}{os.sep}config"
            cls.os_name = os.name

        return cls._instance

    def __str__(self):
        """
        String conversion of the singleton object
        """
        return f"{self.top_dir}"
