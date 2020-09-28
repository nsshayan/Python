#!/bin/sh
scrapy crawl wikipedia \
    -s CONCURRENT_REQUESTS_PER_DOMAIN=20 \
    -s CONCURRENT_REQUESTS=20
