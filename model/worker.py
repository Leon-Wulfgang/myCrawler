"""
workers do the crawling
by Hao Wu
https://github.com/Leon-Wulfgang
"""
import ant
import scrapy


class Worker(ant.Ant):
    """
    Ant worker inheritance of scrapy.Spider
    """
    argv = None
    response = None
    cookies = {
        'cdb2_auth': 'XgQwAtk%2BUbP0YM%2FKE3jz58aMMwprQ7iAt96e11Z%2BzPOsjaNNeNYLTI93fDBh5oOiLw',
        'cdb2_cookietime': '2592000',
        'cdb2_isShowPMNotice': '0',
        'cdb2_sid': 'Qb1dcZ'
    }

    name = 'ant'
    allowed_domains = ['38.103.161.149']
    start_urls = [
        'http://38.103.161.149/bbs/logging.php?action=login',  # login
    ]

    def parse(self, response):
        """
        parse the login page and find ids for username and password
        :param response:
        :return:
        """
        self.write_page_to_file('result/login.html', response)
        login_name = response.selector.xpath('//*[@id="username"]/attribute::name').extract()
        login_password = response.selector.xpath('//*[@id="password"]/attribute::name').extract()

        return scrapy.FormRequest.from_response(
            response,
            formdata={login_name[0]: 'haowu0802', login_password[0]: 'wh9673'},
            callback=self.after_login
        )

    def parse_after_login(self, response):
        print 'Real Page'
        self.write_page_to_file('result/realPage.html', response)

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            self.write_page_to_file('result/afterLogin.html')
            return
        else:
            print 'After Login'
            self.write_page_to_file('result/afterLogin.html', response)
            return scrapy.Request(
                url="http://38.103.161.149/bbs/forum-277-1.html",
                callback=self.parse_after_login)

    def write_page_to_file(self, fn, response):
        with open(fn, 'wb') as fp:
            fp.write(response.body)

