"""A tool for cloning repos matching a search query.

Usage:
  clones <query> [-u <user> | --user <user>] [-d | --dry-run]

Options:
  -u <user>, --user <user>   Specify the user to authenticate with.
  -d, --dry-run              Only print repositories that would be cloned.

"""
from docopt import docopt
from clonesearch.clonesearch import main


def entry():
    args = docopt(__doc__, version='clonesearch 1.0')
    main(args)


if __name__ == '__main__':
    entry()
