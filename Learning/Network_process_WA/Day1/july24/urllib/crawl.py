#!/usr/bin/env python
import sys
import urllib
import urllib2
import re

visited_urls = []
broken_urls = []

def fetch_url_list(url_string):
    try:
        web_request  = urllib2.urlopen(url_string)
        web_page     = web_request.read()
    except urllib2.HTTPError, e:
        return None
    except urllib2.URLError, e:
        return None
    
    href_pattern = re.compile("<\s*a\s+.*?href\s*=\s*['\"](.*?)['\"](\s*>|\s)")
    url_tuple     = href_pattern.findall(web_page)
    url_list = []
    for (i, j) in url_tuple:
        url_list.append(urllib.basejoin(url_string, i))
        
    return url_list
    

def crawl(start_url):
    print "Crawling: ", start_url
    
    url_list = fetch_url_list(start_url)

    if url_list == None:
        if start_url in visited_urls:
            visited_urls.remove(start_url)
        if start_url not in broken_urls:
            broken_urls.append(start_url)
        return None
    
    for url in url_list:
        if url not in visited_urls:
            visited_urls.append(url)
            print "---------------"
            print visited_urls
            print "---------------"
#            raw_input("Enter to continue")
#            crawl(url)

            

if len(sys.argv) < 2:
    print "usage: %s URL" % sys.argv[0]
    sys.exit(-1)

crawl(sys.argv[1])

print "Crawled URLs:"
for i in visited_urls:
    print i

print "--------------------"
print "Broken URLs:"
for i in broken_urls:
    print i

