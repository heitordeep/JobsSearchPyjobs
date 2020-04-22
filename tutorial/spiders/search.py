import scrapy

class PyjobsSpider(scrapy.Spider):
    name = 'jobs'

    start_urls = [
        # 'https://www.pyjobs.com.br/jobs/?title=&requirements=&state=24&salary_range=&job_level=2&remote=unknown',
        'https://www.pyjobs.com.br/jobs/?title=&requirements=&state=24&salary_range=&job_level=&remote=unknown'
    ]

    def parse(self, response):
        # See more details 
        page_links = response.css('div.vertical-center a::attr(href)')
        yield from response.follow_all(page_links, self.parse_jobs)

        # Pagination
        pagination_links = response.css('.page-item a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_jobs(self, response):
        yield {
            'name': response.css('div.container h2::text').get(),
            'company': response.css('.row li::text').get(),
        }
