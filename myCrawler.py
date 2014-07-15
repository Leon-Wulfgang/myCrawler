import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print 'ScriptCharset:',sys.getdefaultencoding()

import time
#from selenium import webdriver

#driver = webdriver.PhantomJS()
#driver.get('www.baidu.com')
#data = driver.find_element_by_id('bottom_container').text
#print data

#browser = webdriver.Firefox()
#browser.get('http://baidu.com/')
#import urllib2,re,os,time
#import chardet
#import cookielib,httplib,urllib
#from bs4 import BeautifulSoup
from ghost import Ghost

#url = "http://www.baidu.com"
#url = "http://hotel.qunar.com/city/beijing_city/dt-274/?tag=beijing_city#fromDate=2014-07-16&toDate=2014-07-17&q=&from=IHot2.4&filterid=fc17ba8d-17dd-4a37-9bd7-ae7760d5e404_A&showMap=0&qptype=&QHFP=ZSS_A60380BD&QHPR=1_1_1_0"
ghost = Ghost()
ghost.wait_timeout = 40
print 'Ghost.wait_timeout:' , ghost.wait_timeout
#ghost.open('http://zanadu.cn')
#page, resources = ghost.open('http://qunar.com')
#page, resources = ghost.open(url)
page, resources = ghost.open("http://hotel.qunar.com/city/beijing_city/dt-274/?tag=beijing_city#fromDate=2014-07-16&toDate=2014-07-17&q=&from=IHot2.4&filterid=fc17ba8d-17dd-4a37-9bd7-ae7760d5e404_A&showMap=0&qptype=&QHFP=ZSS_A60380BD&QHPR=1_1_1_0")
#page, resources = ghost.open('http://www.openstreetmap.org/')
#page, resources = ghost.open('http://zanadu.cn')
#page, resources = ghost.open('http://zanadu.cn/hotel/242/ametis-villa.html')
#assert page.http_status==200 and 'qunar' in ghost.content
#result, resources = ghost.wait_for_selector("final_price")
#result, resources = ghost.wait_for_selector("final_price")
#ghost.wait_for_selector('#q_header_main')
##q_header_main
#result, resources = ghost.wait_for_selector('input[name=query]')
#page, resources = ghost.wait_for_page_loaded()
#page, resources = ghost.wait_for_page_loaded()
#print page.headers
#q-ra-11363
#q-ra-9962
#final-price
#result, resources = ghost.evaluate(
#    "document.getElementById('keysearch').getAttribute('value');")
#result, resources = ghost.evaluate(
#    "alert('123wh');")
#ghost.click('a.btn_openPrc')
#print ghost.wait_for_selector('.q_header_logo')
#ghost.click('.q_header_logo')
#print ghost.click('.rom-abstract')
#reg = ghost.region_for_selector('.q_header_logo')
#reg = ghost.region_for_selector('.tbl-roomtype')
#print reg

#document.querySelectorAll(".btn_openPrc b")[0].id; 
#eleClassName = ".btn_openPrc"
idSelectorJs = """(function () {
                var element = document.querySelectorAll(".btn_openPrc b"); 
                var idAry = [];
                for(var i=0, len=element.length; i<len; i++)
                {
                    idAry.push(element[i].id);
                }                    
                return idAry;
            })();"""

result, resources = ghost.evaluate(idSelectorJs);
#print result
#ghost.show()
#time.sleep(5)
print type(result)
print type(resources)
print result
#exit(0)

for i in result: 
    if (i == result[0]):
        continue
    eleId = "#"+i
    print eleId
    ghost.click(str(eleId))

pageContent = ghost.content
#pageContent = str(result)

#'final-price '

#print resources
#print result
fileName = "testwhqn09-00.html"
fp = open(fileName,'w')
fp.write(pageContent)
fp.close()

print "Written to file:",fileName

#result, resources = ghost.evaluate(
#    "document.getElementById('my-input').getAttribute('value');")

#page, extra_resources = ghost.open("http://xiaorui.cc")
#assert page.http_status==200 and 'xiaorui' in ghost.content
