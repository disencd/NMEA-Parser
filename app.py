from lib.common.inlet_factory import InletFactory
from lib.common.parser import nmea_parser

def run(args):
    inlet = InletFactory.create_executor(args.inlet)
    for line in inlet.read():
        if not line:
            break
        satellite_data, ttff = nmea_parser(line)

    print(f"satellite_data : {satellite_data}")
    print(f"ttff : {ttff}")
