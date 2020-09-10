import json

import scrapy

"""
To Scrape:
In PyCharm Terminal, run:
  scrapy startproject scrape
  cd scrape
  scrapy crawl period -o period.json
  scrapy crawl calendar -o calendar.json
"""

home_url = 'https://registrar.northeastern.edu/group/calendar/'


class PeriodSpider(scrapy.Spider):
    name = 'period'
    start_urls = [
        home_url
    ]

    def parse(self, response, **kwargs):

        # Collect URLs for Current, Future, Past Calendars

        # response.css('a.__item '): list of current, future, past hyperlinks
        for time in response.css('a.__item '):
            if time.css('::text').get() != "Academic Calendars":
                detail = time.xpath('div/text()').get()
                if detail is None:
                    detail = ""
                else:
                    detail = " " + detail.strip().replace("–", "-")
                yield {
                    # ::text grabs the text for <a>
                    'period': time.css('::text').get(0).strip(),
                    # cmd: response.css('a.__item ')[0].css('::text').get()
                    'period_detail': detail,
                    'period_url': response.urljoin(time.css('::attr(href)').get())
                }


class CalendarSpider(scrapy.Spider):
    name = 'calendar'

    def start_requests(self):
        start_urls = []

        try:
            with open('period.json') as json_file:
                data = json.load(json_file)
            for time in data:
                start_urls.append(time["period_url"])
        except FileNotFoundError:
            pass
        return [scrapy.Request(url=start_url) for start_url in start_urls]

    def parse(self, response, **kwargs):
        period = response.css('h1.__title::text').get(0)
        if "Current" in period:
            for academic in response.xpath('//tbody/tr'):
                detail = academic.xpath('td/text()').get()
                if detail is None:
                    detail = ""
                else:
                    detail = " " + detail.strip()
                yield {
                    "period": period,
                    "audience": academic.xpath('td/strong/text()').get(0),
                    "audience_detail": detail,
                    "calendar_url": response.urljoin(academic.xpath('td/a/@href').get(0))
                }
        else:
            for academic in response.css('div#accordion').css('div.__item'):
                year = academic.xpath('div/div/text()').get(0).strip().replace("–", "-")
                for audience in academic.css('div.__copy').css('li'):
                    detail = audience.xpath('text()').get()
                    if detail is None:
                        detail = ""
                    else:
                        detail = " " + detail.strip()
                    yield {
                        "period": period,
                        "year": year,
                        "audience": audience.css('a::text').get(0).rstrip(),
                        "audience_detail": detail,
                        "calendar_url": response.urljoin(audience.xpath('a/@href').get(0))
                    }
