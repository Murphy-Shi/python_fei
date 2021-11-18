官网：https://docs.scrapy.org/en/latest/


scrapy startproject tutorial

tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py


scrapy crawl quotes

scrapy shell 'http://quotes.toscrape.com/page/1/'

response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

response.css('title::text').getall()
['Quotes to Scrape']

response.css('title').getall()
['<title>Quotes to Scrape</title>']

response.css('title::text').get()
'Quotes to Scrape'

response.css('title::text')[0].get()
'Quotes to Scrape'

正则表达
response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']

response.css('title::text').re(r'Q\w+')
['Quotes']

response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']

response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
response.xpath('//title/text()').get()
'Quotes to Scrape'

导出数据
scrapy crawl quotes -O quotes.json
scrapy crawl quotes -o quotes.jl
