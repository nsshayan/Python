def create_shelve(filename, shelve_file):
    import shelve
    s = shelve.open(shelve_file)
    for i, line in enumerate(open(filename)): s[str(i)] = line

