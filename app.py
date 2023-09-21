import pprint

from lib.common.inlet_factory import InletFactory
from lib.common.parser_utils import nmea_parser
from lib.common.plot_utils import plot_satellites_vs_time

def run(args):
    global satellite_data, ttff
    inlet = InletFactory.create_executor(args.inlet)
    for line in inlet.read():
        # add a until function with a timeout.
        if not line:
            break
        satellite_data, ttff = nmea_parser(line)

    pprint.pprint(satellite_data)

    if satellite_data:
        plot_satellites_vs_time(satellite_data)
        if ttff is not None:
            print(f"Time to First Fix (TTFF): {ttff} seconds")