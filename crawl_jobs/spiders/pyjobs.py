import scrapy


class PyjobsSpider(scrapy.Spider):
    name = "jobs"

    start_urls = ["https://www.pyjobs.com.br/jobs/"]

    def parse(self, response):
        # See more details
        page_links = response.css("div.vertical-center a::attr(href)")
        yield from response.follow_all(page_links, self.parse_jobs)

        # Pagination
        pagination_links = response.css("div.page-item a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_jobs(self, response):
        description = response.xpath(
            '//div[@class="container"]//div[@class="row"]//text()'
        )[44:].getall()
        description_sanitized = [i.strip() for i in description if i.strip()]
        title = response.css(
                    ".detalhes-vaga div.container div.row ul li::text"
                )[1:].getall()
       
        yield {
            "name": response.css("div.container h2::text").get(),
            "company": response.css("div.row li::text").get(),
            "salary": title[1],
            "state": title[2],
            "local": title[3],
            "level": title[4],
            "description": description_sanitized
        }
