import scrapy


class PyjobsSpider(scrapy.Spider):
    name = 'jobs'

    start_urls = ['https://www.pyjobs.com.br/jobs/']

    def parse(self, response):
        # See more details
        page_links = response.css('.vertical-center a::attr(href)')
        yield from response.follow_all(page_links, self.parse_jobs)

        # Pagination
        pagination_links = response.css('.page-item a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_jobs(self, response):
        description = response.xpath(
            '//div[@class="container"]//div[@class="row"]//text()'
        )[44:].getall()
        
        description_sanitized = [
            i.strip() for i in description if i.strip()
        ]

        title = response.css(
            '.detalhes-vaga div.container div.row ul li::text'
        )[1:].getall()

        yield {
            'name': response.css('.container h2::text').get(),
            'company': response.css('.row li::text').get(),
            'salary': title[0],
            'state': title[1],
            'local': title[2],
            'level': title[3],
            'description': description_sanitized,
        }
