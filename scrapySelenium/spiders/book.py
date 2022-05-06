from gerapy_selenium import SeleniumRequest
from scrapy import Spider

from scrapySelenium.items import BookItem
from scrapySelenium.settings import MAX_PAGE


class BookSpider(Spider):
    name = 'book'
    allowed_domains = ['spa5.scrape.center']
    base_url = 'https://spa5.scrape.center'

    def start_requests(self):
        """
        在爬虫启动时自动发起请求
        :return:
        """
        start_url = ''
        for i in range(1, MAX_PAGE + 1):
            start_url = f'{self.base_url}/page/{i}'
        # yield Request(start_url, callback=self.parse_index)
        # use SeleniumRequest
        yield SeleniumRequest(start_url, callback=self.parse_index, wait_for='.item .name')

    def parse_index(self, response):
        """
        解析首页
        :param response:
        :return:
        """
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            # yield Request(detail_url, callback=self.parse_detail)
            # use SeleniumRequest
            yield SeleniumRequest(detail_url, callback=self.parse_detail, priority=2, wait_for='.item .name')

    def parse_detail(self, response):
        """
        解析详情页
        :param response:
        :return:
        """
        name = response.css('.name::text').extract_first()
        tags = response.css('.tags button span::text').extract()
        score = response.css('.score::text').extract_first()
        price = response.css('.price span::text').extract_first()
        cover = response.css('.cover::attr(src)').extract_first()
        tags = [tags.strip() for tags in tags] if tags else []
        score = score.strip() if score else ''
        item = BookItem(name=name, tags=tags, score=score, price=price, cover=cover)
        yield item
