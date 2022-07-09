import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_top_250'
    start_urls = [
        'https://www.imdb.com/chart/top/?ref_=nv_mv_250',
    ]

    def parse(self, response):
        for movie in response.css('tbody.lister-list tr'):
            result = {
                'rank': movie.xpath('td[@class="posterColumn"]/span[@name="rk"]').attrib['data-value'],
                'name': movie.xpath('td[@class="titleColumn"]/a/text()').get(),
                'year': movie.xpath('td[@class="titleColumn"]/span/text()').get(),
                'rate': movie.xpath('td[@class="posterColumn"]/span[@name="ir"]').attrib['data-value']
            }
            yield result
        links = response.css('td.titleColumn a ::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.movie)

    def movie(self, response):
        result = {
            "director": response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[1]/div/ul/li/a/text()').get(),
            "stars": response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li[3]/div/ul/li/a/text()').getall()
        }
        yield result

        
