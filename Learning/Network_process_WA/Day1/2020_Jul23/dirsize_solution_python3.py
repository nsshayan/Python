"""
Preliminary exercise:
=====================
Calculate and print the total size of all files
in a directory structure, by recursively traversing
and summing up the sizes of each file in the directory.

Example usage:
    $ python3 dirsize.py .
    556289 bytes

    $ python3 dirsize.py /usr/share
    581829804 bytes

Download this code snippet from the following URL:
    https://dhrona.net/p/apnpw

"""


def calc_size(start_path):
    from pathlib import Path
    return sum((path.stat().st_size for path in Path(start_path).glob("**/*")
                if path.is_file()))
    #totalsize = 0
    # for path in Path(start_path).glob('**/*'):
    #    if path.is_file():
    #        totalsize += path.stat().st_size
    # return totalsize


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path to source directory")

    args = parser.parse_args()

    print(calc_size(args.path), "bytes")
