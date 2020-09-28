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
    from robobrowser import RoboBrowser
    browser = RoboBrowser(parser="lxml")
    browser.open("http://pypi.python.org/")
    search_form = browser.get_form()
    search_form["term"] = term
    browser.submit_form(search_form)
    if not browser.response.ok: 
        print("failed...")
        return
    
    table = browser.parsed.find("table")
    row = table.find("tr")
    
    result = []
    for i in range(1, 6):
        row = row.find_next("tr")
        name, weight, description = [ x.text for x in list(row.children)[1::2] ]
        rec = dict(index=i, name=name, weight=weight, description=description)
        result.append(rec)

    # Implement the logic here!
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
       Description:
           {description}
    -------------------------------------------------------
    """

    for rec in results:
        print(output.format(**rec))
