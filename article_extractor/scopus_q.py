import mechanize
#creating browser
from BeautifulSoup import BeautifulSoup 

br = mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent','Firefox')]

#opening webpage

url = 'http://www.scopus.com/record/display.url?eid=2-s2.0-84892604059&origin=inward&txGid=899337E07B856B803439C640F5B196E7.N5T5nM1aaTEF8rE6yKCR3A%3a1'

respone = br.open(url)

http://www.scopus.com/authid/detail.url?authorId=24361388100&amp;eid=2-s2.0-84892604059











