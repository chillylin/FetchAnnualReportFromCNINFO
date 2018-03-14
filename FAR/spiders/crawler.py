
#!/usr/bin/python
# -*- coding: utf-8 -*-


import scrapy

#from scrapy_splash import SplashFormRequest

from scrapy_splash import SplashFormRequest

from bs4 import BeautifulSoup

import re

import urllib.request
import codecs


class fetchthereportsSpider(scrapy.Spider):
    name = 'fetchthereports'



    def start_requests(self):

        tickers = [
 			'600001',
            '000777',

        ]

        for ticker in tickers: # try all tickers one by one
            if ticker[0] == '0' :
                data = { # prepare for the requrest
                    'stock': ticker,
                    'searchkey': '年年度报告',
                    'category': 'category_ndbg_szsh',
                    'pageNum': '1',
                    'pageSize': '30',
                    'column': 'szse_main', # for Shenzhen stock exchange
                    'tabName': 'fulltext',
                    'sortName':'',
                    'sortType':'',
                    'limit': '',
                    'seDate': '',
                }
            elif ticker[0] == '6' :
                data = { # prepare for the requrest
                    'stock': ticker,
                    'searchkey': '年年度报告',
                    'category': 'category_ndbg_szsh',
                    'pageNum': '1',
                    'pageSize': '30',
                    'column': 'sse', # for Shanghai stock exchange
                    'tabName': 'fulltext',
                    'sortName':'',
                    'sortType':'',
                    'limit': '',
                    'seDate': '',
                }
            else:
                print  ("Wrong ticker")
                continue


            yield SplashFormRequest(
                url = 'http://www.cninfo.com.cn/cninfo-new/announcement/query',
                formdata= data,
                callback= self.parse,
            #   args={'wait': 2}
            )

    def parse(self, response):
# Uncomment the following part if you want to save the page of the list of reports.
#        
#        filename = str(re.findall(r'secCode":"(.*)","secName', record)[0]) + '%s.html'
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#        self.log('Saved file %s' % filename)


        records = re.split('\"id\":null',response.body.decode('UTF-8','strict')) #split the response body by each record's beginning
        records.pop(0) # remove the head of the file, which is not a record


        for record in records:

            file = str(re.findall(r'announcementTitle":"(.*)","announcementTime', record)[0]) #find filename

            if (file.find('摘要') == -1) & (file.find('取消') == -1) & \
                    ((not file.find('2007') == -1) or (not file.find('2015') == -1) ):
                # eliminate files which is a brief of a report and which is cancelled.
                # and select the years needed.

                filenamelocal = str(re.findall(r'secCode":"(.*)","secName', record)[0])+' ' + file + '.pdf'
                # split the url to find the real filename on server
                filenameServer = re.split('/', re.findall(r'adjunctUrl":"(.*)","adjunctSize', record)[0])[2]

                # add directory to the filename on server
                downloadurl = 'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/download/' + filenameServer
#                print(filenameServer)
#                print(filenamelocal)
#                print(downloadurl)

                # Download the file
                print ('Downloading',filenamelocal,' from:', downloadurl)
                urllib.request.urlretrieve(downloadurl, filenamelocal)

