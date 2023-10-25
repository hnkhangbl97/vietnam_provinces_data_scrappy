import scrapy
import json

class VietnamProvincesSpider(scrapy.Spider):
    name = "vietnam_provinces"
    allowed_domains = ["provinces.open-api.vn"]
    start_urls = ["https://provinces.open-api.vn/api/?depth=2"]

    def parse(self, response):
        provinces =response.json()
        for province in provinces:
            districts = list()
            for district in province.get('districts'):
                districts.append(district.get('codename'))
            yield {
                'name': province.get('name'),
                'code': province.get('code'),
                'phone_code': province.get('phone_code'),
                'districts': districts
            }

