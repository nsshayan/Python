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
    https://public.etherpad-mozilla.org/p/Advanced_Python

"""

def calc_size(start_path):
    import os
    from itertools import repeat
    # Abuse of comprehensions - inefficient and un-readable
    return sum([sum([os.path.getsize(os.path.join(path, file))  \
                for path, file in zip(repeat(path), files)      \
                if os.path.isfile(os.path.join(path,file))])    \
                for path, dirs, files in os.walk(start_path)])

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("path",
                      help="Path to source directory")

    args = parser.parse_args()

    print(calc_size(args.path), "bytes")
