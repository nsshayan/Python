#!/usr/bin/env python
"""
Exercise:
=========
Write a program to list top 5 hits for a search query
on http://pypi.python.org/

Example usage:
--------------
    $ ./pypi_search.py rest
    1. Package: django-restricted-sessions 0.2.0
       Weight: 10
       Description:
           Restrict Django sessions to IP and/or user agent.

    2. Package: Rest 0.1
       Weight: 10
       Description:
           Rest is a rest client for python that makes it
           easy to make authenticated rest calls.

    3. ...

"""

def pypi_search(term):
    result = []

    import requests
    response = requests.get("http://pypi.python.org/")
    if response.status_code != 200:
        raise ValueError("Failed to initiate request...")

    response = requests.get("http://pypi.python.org/pypi",
                         {":action" : "search",
                         "term" : term,
                         "submit" : "search"},
                        cookies=response.cookies)
    result.append(response)

    return result

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
            "search",
            help="Search for a specific term")

    args = parser.parse_args()

    results = pypi_search(args.search)
    output = """
    {index}. Package: {name}
       Weight: {weight}
       Description: {description}
    """

    for rec in results:
        print(output.format(**rec))


