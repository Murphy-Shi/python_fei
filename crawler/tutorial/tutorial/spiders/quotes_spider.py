import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {filename}')

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # next_page = response.css('li.next a::attr(href)').get()
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
        # if next_page is not None:
        #     1
        # next_page = response.urljoin(next_page)
        # yield scrapy.Request(next_page, callback=self.parse)

        # 2
        # yield response.follow(next_page, callback=self.parse)
        # 3
        # for a in response.css('ul.pager a'):
        #     yield response.follow(a, callback=self.parse)
        # 4
        # yield from response.follow_all(css='ul.pager a', callback=self.parse)