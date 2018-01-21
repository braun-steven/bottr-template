import argparse
from argparse import Namespace


def parse_arg() -> Namespace:
    """Parse commandline arguments
    :return: argument dict
    """
    parser = argparse.ArgumentParser('Reddit UnitConvertBot')
    parser.add_argument('--log', '-l', default='log.out', type=str,
                        help='Log file.')
    parser.add_argument('--log-level', '-ll', default='INFO', type=str,
                        help='Log file.', choices=['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'])
    parser.add_argument('--depth', '-d', default=1, type=int, help='Allowed comment depth.')
    parser.add_argument('--debug', default=False, action='store_true',
                        help='Enable debug mode')
    parser.add_argument('--test-comment', '-tc', default=None, type=str,
                        help='Test commend ID.')
    parser.add_argument('--test-submission', '-ts', default=None, type=str,
                        help='Test submission ID.')
    opts = parser.parse_args()
    return opts
