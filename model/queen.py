"""
Queen Ant
distribution of work
by Hao Wu
https://github.com/Leon-Wulfgang
"""
import sys, ant, worker
from scrapy.crawler import CrawlerProcess


class Queen(ant.Ant):
    name = 'queen'
    argv = None
    service_map = {
            'sis': 'service_sis',
        }

    def __init__(self, argv):
        ant.Ant.__init__(self)
        self.argv = argv

    def work(self):
        service_name = self.argv[1]
        self.route(service_name)

    def route(self, service_name):
        print locals()
        #self.service_sis()

    def service_sis(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(worker.Worker)
        process.start()  # the script will block here until the crawling is finished


