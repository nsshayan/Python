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

def calc_size(start_path):
    pass # TODO
    
if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("path",
                      help="Path to source directory")

    args = parser.parse_args()

    print(calc_size(args.path), "bytes")
