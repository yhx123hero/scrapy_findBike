# from scrapy.crawler import  CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# process =  CrawlerProcess(get_project_settings())
#
# process.crawl('quotes')
# process.start()
import datetime
from scrapy import cmdline
import pickle
import re
def run_spider(path):
    cmdline.execute(("scrapy crawl baike -a path="+path).split())

if __name__ == '__main__':
    # 相对于findBaike路径
    run_spider("entity_v2.txt")
    # run_spider("item.txt")
    # f = open("item1.txt", "rb")
    # f1 = open("item_result.txt", "wb")
    # d_past = pickle.load(f)
    # while True:
    #     try:
    #         d_last = pickle.load(f)
    #         p = "http://www.baike.com"
    #         if re.search(p, str(d_last)):
    #             pickle.dump(d_last, f1)
    #         else:
    #             pickle.dump(d_past, f1)
    #             d_past = d_last
    #     except:
    #         break
    # f = open("test.txt",encoding="utf-8")
    # f = open("entity_v2.txt", encoding="utf-8")
    # while True:
    #     phrase = f.readline()
    #     print(phrase)
    #     if not phrase:
    #         break

