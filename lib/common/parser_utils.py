import re

satellite_data = {'Timestamp': [], 'Satellites Tracked': []}


def parse_nmea_sentence(nmea_sentence):
    """Parse a single NMEA sentence and extract satellite information."""
    if nmea_sentence.startswith('GPGSA'):
        num_satellites = int(nmea_sentence.split(',')[2])
        return num_satellites
    return None


def parse_timestamp(timestamp):
    return int(timestamp.split('=')[1].strip(',')[0])


def nmea_parser(line):
    ttff = None
    match = re.match(r'(.*?)\$\s*(.*)', line)
    if match:
        timestamp, nmea_sentence = match.groups()
        num_satellites = parse_nmea_sentence(nmea_sentence)
        ts = parse_timestamp(timestamp)
        if num_satellites is not None:
            satellite_data['Timestamp'].append(int(ts))
            satellite_data['Satellites Tracked'].append(num_satellites)
        elif 'GPGSA' in nmea_sentence and ttff is None:
            ttff = int(ts)

    return satellite_data, ttff
