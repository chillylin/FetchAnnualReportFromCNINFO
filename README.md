# FetchAnnualReportFromCNINFO
The crawler is designed to fetch annual reports of listed companies on main board of Shanghai and Shenzhen Stock Exchanges via www.cninfo.com.cn

Use this crawler:

Download all files
1. Install scrapy and scrapy-splash.
2. Install other pacakge needed in crawler.py
3. Install splash on a computer, record it's IP.
4. Edit the settings.py file 
    find the line "SPLASH_URL = 'http://IPofyoursplashserver:8050'"
    change the IPofyoursplashserver to the IP of your splash server in step 3.
5. Edit crawler.py
    fill      

        tickers = ['600001','000777',]
    with the stock tickers you need. (remember to delete the example: 600001 and 000777)
    
6. Edit crawler.py 
   change 
   
        ((not file.find('2007') == -1) or (not file.find('2015') == -1) )
   
   to the year you want. 
   
   for example, if you want three years 2002,2005 and 2008, it should be 
   
        ((not file.find('2002') == -1) or (not file.find('2005') == -1) ) or (not file.find('2008') == -1) )
    
5. Locate the FAR dirctory via commandline.
6. Run 


       scrapy crawl fetchthereports
