import argparse
from os import environ
from argparse import Namespace
import logging
import app
from lib import Inlets

log = logging.getLogger(__name__)


def parse_args() -> Namespace:
    description = ('A simple command line inlet for nvme parser module '
                   'to validate and pretty-print objects.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--inlet', '-i', default='log', choices=list(Inlets()))
    parser.add_argument('--from-env', '-e', action='append', type=str,
                        help='List of all the options that needs to be read from the OS environment.')
    args = parser.parse_args()

    if args.from_env:
        for param in args.from_env:
            _attr_name = param.replace('-', '_')
            _env_var = _attr_name.upper()
            _env_val = environ.get(_env_var)
            print(
                f'Getting {_env_var} from env to set cls.args.{_attr_name}={_env_val}')
            if _env_val:
                setattr(args, _attr_name, _env_val)

    return args


def main():
    args = parse_args()
    app.run(args)


if __name__ == '__main__':
    main()
