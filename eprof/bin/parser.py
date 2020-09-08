import argparse
import shlex
from eprof.meta import version

parser = argparse.ArgumentParser(
    "Executable to convert outputs eprof libraries into a kvhf file.")

parser.add_argument('-V', '--version', action='version', version=version)

parser.add_argument(
    'paths',
    metavar='PATHS',
    nargs='+',
    help="The paths to eprof dirs. Will merge the resulted kvhf into one.")

parser.add_argument('--sep-key', type=str, default=':',
                    help='Character separating the key and the values of the kvhf output')
parser.add_argument('--sep-val', type=str, default=',',
                    help='Character separating the values of the kvhf output')

parser.add_argument('-o', '--out-path', required=True,
                    help='Path of the created kvhf file.')


def getArgs(string=None):  # we allow string for testing purpose
    if string:
        args = parser.parse_args(shlex.split(string))
    else:
        args = parser.parse_args()
    args = vars(args)

    return args
