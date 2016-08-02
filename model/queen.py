"""
Queen Ant
distribution of work
by Hao Wu
https://github.com/Leon-Wulfgang
"""
import ant
import worker
import conf.service_mapping
from scrapy.crawler import CrawlerProcess


# Queen ants manage work, create worker ant for services
class Queen(ant.Ant):
    name = 'queen'
    argv = None
    service_map = conf.service_mapping.global_service_map

    def __init__(self, argv):
        ant.Ant.__init__(self)
        self.argv = argv

    def work(self):
        service_name = self.argv[1]
        self.route(service_name)

    def route(self, service_name):
        try:
            fn = self.service_map[service_name]
            print('Running Service:',service_name)
        except StandardError:
            print 'Service Name: ', service_name, ' - Not Found.'
            exit(1)
        service = getattr(self, fn)
        service()

    def service_sis(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

        process.crawl(worker.Worker)
        process.start()  # the script will block here until the crawling is finished


