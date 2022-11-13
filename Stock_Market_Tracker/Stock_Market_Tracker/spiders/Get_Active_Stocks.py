from datetime import date
import scrapy
import csv


class GetActiveStocksSpider(scrapy.Spider):
    name = 'Get_Active-Stocks'
    allowed_domains = ['https://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php?index=FNO']
    start_urls = ['http://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php?index=FNO']

    def parse(self, response):

        Data = []
        Stock_Name = response.xpath('//div[@class="bsr_table hist_tbl_hm"]/table/tbody/tr/td[@class="PR"]/h3[@class="gld13 disin"]/a/text()').extract()
        Stock_Price = response.xpath('//div[@class="bsr_table hist_tbl_hm"]/table/tbody/tr/td[@align="right"]/text()').extract()

        file = open("Most_Active_Stocks.csv","a")
        write = csv.writer(file)
        Date = []
        t_date = date.today()
        t_date = t_date.strftime("%B %d, %Y")
        Date.append(t_date) 
        write.writerow(Date)
        Init_data = ['Company Name','Highest','Lowest']
        write.writerow(Init_data)

        for i in range(len(Stock_Name)):
            Data_row = []
            Data_row.append(Stock_Name[i])
            Data_row.append(Stock_Price[i*16])
            Data_row.append(Stock_Price[i*16+1])
            Data.append(Data_row)

        write.writerows(Data)

        file.close()
