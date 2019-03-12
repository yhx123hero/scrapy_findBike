# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pickle

class FindbaikePipeline(object):
    def __init__(self):
        self.file = open('item_result.txt','wb')

    def process_item(self, item, spider):
        # print(item)
        item = dict(item)
        pickle.dump(item,self.file)
        # print(item)
        # file1 = open('item1.txt','w+',encoding='utf-8')
        # for i,j in item.items():
        #     file1.write(i+j+"\n")


        # line = json.dumps(dict(item))+"\n"
        # self.file.write(line)
        return item
