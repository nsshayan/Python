data_to_extracted = """
<a class="package-snippet" href="/project/ttr-xml-csv2xml/">
    <h3 class="package-snippet__title">
        <span class="package-snippet__name">ttr.xml.csv2xml</span>
        <span class="package-snippet__version">0.1.2dev002</span>
    </h3>
    <p class="package-snippet__description">
    module, providing conversion of csv file into xml
    </p>
</a>
"""

regex = r"""
<a                   # <a class="package-snippet"
\s+
class\s*=\s*
"package-snippet"\s+
href\s*=\s*"
  (?P<url>.+?)              # Extract URL
"
.+?                         # Skip noise...
snippet__name">
(?P<title>.+?)              # Extract title
</span>
.+?
snippet__description">
(?P<description>.+?)       # Extract description
</p>.+?</a>
"""


def pypi_search(term):
    import requests
    response = requests.get("http://pypi.org/search/", params=dict(q=term))

    if response.ok:
        import re
        pattern = re.compile(regex, re.DOTALL | re.VERBOSE)
        for i, match in zip(range(1, 6), pattern.finditer(response.text)):
            yield dict(index=i, **match.groupdict())


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("search", help="Search for a specific term")

    args = parser.parse_args()

    results = pypi_search(args.search)
    output = """
    {index}. Package: {title}
       URL: {url}
       Description:
           {description}
    -------------------------------------------------------
    """

    for rec in results:
        print(output.format(**rec))
