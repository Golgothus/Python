import scrapy

class QuotesSpider(scrapy.Spider):
    name = "greg"

    def start_requests(self):
        urls = [
            'https://www.dhs.gov'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = input('Insert filename here...')
        #filename = 'quotes-{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file {}'.format(filename))
