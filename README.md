# scrapySelenium

> Scrapy 框架整合 Selenium 练习项目
>
> 测试网站：https://spa5.scrape.center

### 核心

实现`SeleniumMiddleware`中间件，并返回一个`HtmlResponse`对象。

```python
class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        url = request.url
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(5)
        html = browser.page_source
        browser.close()
        return HtmlResponse(url=url, body=html, request=request, status=200, encoding='utf-8')
```

### 优化

使用`gerapy_selenium`库代替`selenium`库。

具体用法参见文档：[Gerapy/GerapySelenium](https://github.com/Gerapy/GerapySelenium)

### 运行

#### 安装依赖

```shell
pip install -r requirement.txt
```

#### 运行

```shell
scrapy crawl book
```

