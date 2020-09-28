#!/usr/bin/env python
"""
Exercise:
=========
Write a program to list top 5 hits for a search query
on http://pypi.python.org/

Example usage:
--------------
    $ ./pypi_search.py rest

       1. Package: django-modelstats 0.1.1
           Weight: 10
           Description:
               Simple stats generation API for django models
        -------------------------------------------------------


        2. Package: django-server-guardian-api 0.1.2
           Weight: 10
           Description:
               API offering health metrics for the ``django-server-guardian`` app.
        -------------------------------------------------------

        3. Package: admindjango-ckeditor-blog 2.0
           Weight: 9
           Description:
               django-blogs app to provide you facility to craete a blogs in admin panel
        -------------------------------------------------------


        4. Package: alauda-django-oauth 0.9.0
           Weight: 9
           Description:
               OAuth2 goodies for Django
        -------------------------------------------------------


        5. Package: alpaca-django 0.3.0
           Weight: 9
           Description:
               Alpaca error logger for Django applications.
        -------------------------------------------------------
"""

"""
 <a class="package-snippet" href="/project/lightflow-rest/">
    <h3 class="package-snippet__title">
      <span class="package-snippet__name">Lightflow-Rest</span>
      <span class="package-snippet__version">1.1.0</span>

    </h3>
    <p class="package-snippet__description">A REST extension for Lightflow.</p>
  </a>

"""

def pypi_search(term):
    regex = r'''
    <a \s+ class="package-snippet" \s+ href="
    (?P<url>.+?)"> \s*

    <h3 \s+ class="package-snippet__title"> \s*
        <span \s+ class="package-snippet__name">
        (?P<name>.+?)</span> .+?
        <p \s+ class="package-snippet__description">
        (?P<description>.+?)</p>
    '''


    import requests
    #response = requests.get(f"http://pypi.org/search/?q={term}")
    response = requests.get("http://pypi.org/search/", params={"q": term})

    if not response.ok:
        raise ValueError("Failed to initiate request")

    import re
    pattern = re.compile(regex, re.MULTILINE | re.DOTALL | re.VERBOSE)
#    result = []
#    for i, match in zip(range(1,6), pattern.finditer(response.text)):
#        rec = dict(index=i)
#        rec.update(match.groupdict())
#        result.append(rec)

    result = [ dict(**match.groupdict(), index=i) \
               for i, match in zip(range(1,6),       \
                   pattern.finditer(response.text)) ]

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
       Weight: {url}
       Description:
           {description}
    -------------------------------------------------------
    """

    for rec in results:
        print(output.format(**rec))
