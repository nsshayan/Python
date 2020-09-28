
def download_with_urllib2(url):
    import urllib2
    r = urllib2.urlopen(url)
    return r.geturl(), r.read()


def download_with_requests(url):
    import requests
    r = requests.get(url)
    if r.history and ('Location' in r.history[-1].headers):
        url = r.history[-1].headers['Location']
    return url, r.content


def parse_with_lxml(url, page):
    from lxml import html
    tree = html.fromstring(page)
    return url, tree.xpath("//h1")[0].text_content()


def parse_with_bs4(url, page):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")
    return url, soup.h1.get_text()

def run_crawl(crawl, parse, urls):
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging.INFO)

    logger.info("I'm a job using %s and %s running on %d urls" %
                (crawl, parse, len(urls)))

    for url in urls:

        logger.debug("Working on url: %s" % url)

        download_method = (download_with_urllib2
                           if crawl == "urllib2"
                           else download_with_requests)

        parse_method = (parse_with_lxml
                        if parse == "lxml"
                        else parse_with_bs4)

        url, page = download_method(url)

        url, title = parse_method(url, page)

        logger.info("url: %s, title: %s" % (url, title))


def call_with_threading(crawl, parse, nthreads, urls):
    import threading
    threads = []

    # Round-up the job length
    job_length = (len(urls)+nthreads-1)/nthreads

    for i in xrange(0, len(urls), job_length):
        urls_part = urls[i:i+job_length]
        t = threading.Thread(target=run_crawl,
                             args=[crawl, parse, urls_part])
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def get_urls():
    return ["https://en.wikipedia.org/wiki/Special:Random"
            for i in xrange(100)]

def main(crawl, parse, nthreads):
    import sys
    if nthreads < 0:
        sys.exit(1)
    elif nthreads == 0:
        run_crawl(crawl, parse, get_urls())
    else:
        call_with_threading(crawl, parse, nthreads, get_urls())


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument(
          '--crawl', choices=["urllib2", "requests"],
          default="urllib2",
          help='download method - urllib2 (default) or requests')

    parser.add_argument(
          '--parse', choices=["lxml", "beautifulsoup"],
          default="lxml",
          help='parse method - lxml (default) or beautifulsoup')

    parser.add_argument(
          '--nthreads', help='Number of threads (default 0)',
          type=int, default=0)

    args = parser.parse_args()

    main(**vars(args))


