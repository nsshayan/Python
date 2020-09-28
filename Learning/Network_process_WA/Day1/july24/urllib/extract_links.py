import re

def extract_links(contents):

    pattern = r"""
        (href|src)       # match href or src
        \s*              # followed by 0 or more spaces
        =                # followed by = 
        \s*              # followed by 0 or more spaces
        (?P<quote>['"])           # either ' or "
        (.*?)            # contents (the link)
        (?(quote)(?P=quote)|)               # ending with either ' or "
    """

    for match in re.finditer(pattern, contents, re.VERBOSE | re.IGNORECASE):
        yield match.group(3)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print >>sys.stderr, "usage: %s filename.\n" % sys.argv[0]
        exit(1)

    contents = open(sys.argv[1]).read()
    for link in extract_links(contents): print link



