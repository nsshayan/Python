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

"""
import os
def calc_size_legacy(path):
    total = 0
    for path, subdirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(path, file)
            file_size = os.path.getsize(file_path)
            total += file_size
    return total
    
def calc_size(path):
    from pathlib import Path
    return sum(p.stat().st_size for p in Path(".").glob("**/*"))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("path",
                      help="Path to source directory")

    args = parser.parse_args()

    print(calc_size(args.path), "bytes")