import scrapy
from scrapy.selector import Selector

class UserSpider(scrapy.Spider):
    name = 'user'
    start_urls = []

    def __init__(self):
        url = 'https://www.cardmarket.com/en/Magic/Users/Rawcast/Offers/Singles?site='

        for page in range(1, 15):
            self.start_urls.append(url + str(page))

    def parse(self, response):
        l1 = []

        cards = response.xpath('//*[@id="UserOffersTable"]/div[2]').get()
        for i in Selector(text=cards).css("div.row.no-gutters.article-row").getall():
            name = Selector(text=i).css("div.col-seller.col-12.col-lg-auto").get().replace(" ", "-").replace(">", " ").replace("<", " ").split()[2].replace("-", " ")
            price = Selector(text=i).css("span.font-weight-bold.color-primary.small.text-right.text-nowrap::text").get()
            quantity = Selector(text=i).css("span.item-count.small.text-right::text").get()
            l1.append([name, price, quantity])

        with open("cardsfrom-{}.txt".format("User"), "a") as f:
            f.write(str(l1))
