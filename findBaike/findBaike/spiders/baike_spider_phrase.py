import scrapy
import json
from lxml import etree
import re
from urllib import parse
import findBaike.items
import datetime
import time
#import requests

class QuotesSpider(scrapy.Spider):
    # 能传参的spider
    name = 'baike'
    # def start_requests(self):
    #     url = "https://www.baidu.com"
    #     self.count = 0
    #     yield scrapy.Request(url = url,callback=self.parse)

    def start_requests(self):

        urls = []
        f = open(self.path, encoding="utf-8")
        while True:
            phrase = f.readline()

            if not phrase:
                break
            urls.append(phrase.strip("\n"))

        for url in urls:

            # count += 10
            # time.sleep(2)
            request = scrapy.Request(url='https://baike.baidu.com/item/%s' % parse.quote(url),callback=self.parse_data1,dont_filter=True)
            request.meta['url'] = url
            yield request
            # for i in range(2):
            #     page = str(i)
            #     yield scrapy.FormRequest(url = url,
            #                              formdata={'limit': '24','timeout': '3000','filterTags':[],'tagId': '76607',
            #                                               'fromLemma': 'false','contentLength': '40','page': page},
            #                              callback=self.parse)
    # 百度百科页面
    def parse_data1(self, response):
        p = re.compile('\s+')
        p1 = re.compile('\[\d+]')
        p2 = re.compile('\[(.*)-(.*)]')
        tree = etree.HTML(response.text)
        if tree.xpath("//div[@class='lemma-summary']"):
            str = ""
            title = tree.xpath('//h1')

            summary = tree.xpath("//div[@class='lemma-summary']")[0]
            basebox_dt = tree.xpath("//div[contains(@class,'basic-info')]//dt")
            basebox_dd = tree.xpath("//div[contains(@class,'basic-info')]//dd")

            item = findBaike.items.FindbaikeItem()
            item['title'] = response.meta['url'].replace("\n", "")
            for i in title:
                if i.text.replace("\n", "") != item['title']:
                    item["#同义词#"] = i.text.replace("\n", "")


            for i in summary:

                str += (i.xpath('string(.)').replace("\n","").replace("\xa0",""))
                str += "\n"
                # print(i.xpath('string(.)'))
                value = re.sub(p1, "", str).strip("\n")
                item['简介'] =  re.sub(p2, "", value)

            # print(item.keys())
            for i,j in zip(basebox_dt,basebox_dd):
                key = re.sub(p, "", i.xpath('string(.)'))
                key = re.sub(p1, "", key)
                value = re.sub(p, "", j.xpath('string(.)'))
                value = re.sub(p1, "", value)
                value = re.sub(p2, "", value)
                item[key] = value
                # str += (re.sub(p,"",i.text),re.sub(p,"",j.xpath('string(.)'))+"\n")

            item["link"] = 'https://baike.baidu.com/item/%s' % parse.quote(item["title"])
            yield item

        # else:
        #     # yield scrapy.Request(url='http://www.baike.com/wiki/%s&prd=button_doc_entry'% parse.quote(url))
        #     url =response.meta['url']
        #     # response = 'http://www.baike.com/wiki/%s&prd=button_doc_entry' %parse.quote(url)
        #     request = scrapy.Request(url='http://www.baike.com/wiki/%s&prd=button_doc_entry' %parse.quote(url),callback=self.parse_data2,dont_filter=True)
        #     request.meta['url'] = url
        #     yield request

    # 互动百科页面
    # def parse_data2(self, response):
    #     p = re.compile('\s+')
    #     p1 = re.compile('\[\d+]')
    #     p2 = re.compile('\[(.*)-(.*)]')
    #     tree = etree.HTML(response.text)
    #     if tree.xpath("//div[contains(@class, 'l') and contains(@class, 'w-640')]"):
    #         str = ""
    #         title = tree.xpath('//h1')
    #
    #         summary = tree.xpath("//div[@class='summary']/p")
    #         basebox_dt = tree.xpath("//div[contains(@class,'module')]//td/strong")
    #         basebox_dd = tree.xpath("//div[contains(@class,'module')]//td/span")
    #
    #         item = findBaike.items.FindbaikeItem()
    #         item['title'] = response.meta['url'].replace("\n", "")
    #         for i in title:
    #             if i.text.replace("\n", "") != item['title']:
    #                 item["#同义词#"] = i.text.replace("\n", "")
    #         for i in title:
    #             item['title'] = i.text.replace("\n", "")
    #         for i in summary:
    #             str += (i.xpath('string(.)').replace("\n", "").replace("\xa0", ""))
    #             str += "\n"
    #             # print(i.xpath('string(.)'))
    #         item['简介'] = re.sub(p1, "", str).strip("\n")
    #         # print(item.keys())
    #         for i, j in zip(basebox_dt, basebox_dd):
    #             key = re.sub(p, "", i.text[:-1])
    #             key = re.sub(p1, "", key)
    #             value = re.sub(p, "", j.xpath('string(.)'))
    #             value = re.sub(p1, "", value)
    #             value = re.sub(p2, "", value)
    #             item[key] = value
    #             # str += (re.sub(p,"",i.text),re.sub(p,"",j.xpath('string(.)'))+"\n")
    #
    #         item["link"] = 'http://www.baike.com/wiki/%s&prd=button_doc_entry' % parse.quote(response.meta['url'])
    #
    #     else:
    #         item = findBaike.items.FindbaikeItem()
    #     yield item
