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


def pypi_search(term):
    from requests_html import HTMLSession
    session = HTMLSession()
    response = session.get(f"http://pypi.org/search/?q={term}")
    
    result = [dict(index=i,
                   name=d.a.text,
                   url=d.a["href"],
                   description=d.p.text)
              for i, d in enumerate(response.html.find("div.package-snippet")[:5], 1)]
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
       URL: {url}
       Description:
           {description}
    -------------------------------------------------------
    """

    for rec in results:
        print(output.format(**rec))
