import scrapy


class QuotesSpider(scrapy.Spider):
    name = "icbc"

    start_urls = [
        'http://www.icbc.com.cn/ICBC/%E7%BA%AA%E5%BF%B5%E5%B8%81%E4%B8%93%E5%8C%BA/default.htm',
    ]

    def parse(self, response):
        for item in response.css('div.MidBox div table tr'):
            title = item.css('span a::text').get(default='').strip()
            url = "http://www.icbc.com.cn" + item.css('span a::attr(href)').get(default='').strip()

            if title == '':
                continue

            yield {
                "title": title,
                "url": url
            }
