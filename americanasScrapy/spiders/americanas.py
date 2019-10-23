import scrapy


class AmericanasSpyder(scrapy.Spider):
    name = 'americanas'
    start_urls = ['https://www.americanas.com.br/produto/134186808']

    def parse(self, response):
        id = response.css("span.TextUI-sc-12tokcy-0.hdQYf::text").getall()[1]
        name = response.css('h1[id="product-name-default"]::text').get()
        breadcrumb = response.css("span.TextUI-ohhfq9-5::text").getall()
        img = response.css("img.ImageUI-sc-13c8s2j-1::attr(src)").get()
        seller = response.css("span.seller-00776574000660::text").get()
        price = response.css("span.sales-price::text").get()

        yield {
            "id": id,
            "name": name,
            "breadcrumb": breadcrumb,
            "img": img,
            "seller": seller,
            "price": price
        }
