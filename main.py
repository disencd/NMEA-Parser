import argparse
from os import environ
from argparse import HelpFormatter, Namespace
import pprint
import logging
import app
from lib import Inlets

log = logging.getLogger(__name__)


class SortingHelpFormatter(HelpFormatter):
    def add_arguments(self, actions):
        # following code is left there in case we prefer to use attrgetatter
        # actions = sorted(actions, key=attrgetter('option_strings'))
        i = 1
        if environ.get('ARGS_SORT', 'short') == 'long':
            i = 0

        actions = sorted(actions, key=lambda x: x.option_strings[i])
        super(SortingHelpFormatter, self).add_arguments(actions)


def parse_args() -> Namespace:
    description = ('A simple command line inlet for nvme parser module '
                   'to validate and pretty-print objects.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--inlet', '-i', default='uart', choices=list(Inlets()))
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
