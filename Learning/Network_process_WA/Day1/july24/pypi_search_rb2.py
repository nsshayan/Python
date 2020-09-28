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
    # TODO: Populate result list with each record as a dictionary
    # searched result.
    result = []
    from robobrowser import RoboBrowser
    br = RoboBrowser(parser="lxml")
    br.open("https://pypi.org/")
    if not br.response.ok:
        raise ValueError("Failed at https://pypi.org/")
    form = br.get_form()
    form["q"] = term
    br.submit_form(form)
    if not br.response.ok:
        raise ValueError("Failed at form submit")

    links = br.select("a.package-snippet")[:5]
    for i, link in enumerate(links):
        rec = {}
        rec["index"] = i
        rec["href"] = link["href"]
        rec["name"] = link.span.text
        rec["description"] = link.p.text
        result.append(rec)

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
       URL: {href}
       Description:
           {description}
    -------------------------------------------------------
    """

    for rec in results:
        print(output.format(**rec))
