import sys

def recurse_files(start_path):
    from os import walk
    from os.path import join

    for path, dirs, files in walk(start_path):
        for f in files: yield join(path, f)
# return (join(path, f) for path, dirs, f in (x for x in walk(start_path)))

if len(sys.argv) < 2:
    print("usage: {} path.".format(sys.argv[0]))

start_path = sys.argv[1]

for f in recurse_files(start_path): print(f)
