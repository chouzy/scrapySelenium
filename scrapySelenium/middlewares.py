# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import time

from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumMiddleware(object):
    """
    使用 selenium 爬取网页
    """

    def process_request(self, request, spider):
        """
        在请求发送到爬虫的时候，会调用此方法
        :param request:
        :param spider:
        :return:
        """
        url = request.url
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(5)
        html = browser.page_source
        browser.close()
        return HtmlResponse(url=url, body=html, request=request, status=200, encoding='utf-8')
