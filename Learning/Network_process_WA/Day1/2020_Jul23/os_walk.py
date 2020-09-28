import os
import sys

if len(sys.argv) < 2:
    print("usage: {} path.".format(sys.argv[0]))

start_path = sys.argv[1]

for path, dirs, files in os.walk(start_path):
    print("=" * 60)
    print("Path:", path)
    print("-" * 60)
    print("Directories:", dirs)
    print("-" * 60)
    print("Files:", files)
    print("*" * 60)
    input("Press enter to continue...")
