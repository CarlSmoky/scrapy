import scrapy


class JobpostSpider(scrapy.Spider):
    name = "jobposts"
    start_urls = [
        "https://hnhiring.com/may-2023"
    ]

    def parse(self, response):
        
        for jobpost in response.css("li.job"):

            description = " ".join(jobpost.css("div.body p::text").getall())

            links = ", ".join(jobpost.css("div.body p a::attr(href)").getall())
            
            if not description == "[flagged]" and not description == "[dead]":
                
                yield {
                    "title": "",
                    "company": "",
                    "description": description,
                    "application_link": links,
                    "date": jobpost.css("div.user span.type-info::text").get()
                }
