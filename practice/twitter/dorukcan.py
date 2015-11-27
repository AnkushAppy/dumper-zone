import urllib2
import re
from BeautifulSoup import BeautifulSoup
from feedgen.feed import FeedGenerator

DIZI_TITLE = "Six Feet Under"
DIZI_MAIN_URL = "http://dizipub.com/dizi/six-feet-under-tum-bolumler-izle"
DIZI_LOGO = "http://images.popmatters.com/news_art/s/six-feet-under.jpg"

def downloadUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36')
    req.add_header('Host', 'dizipub.com')
    resp = urllib2.urlopen(req)
    return resp.read()

def fetch():
    #bolum adreslerini al
    html = downloadUrl(DIZI_MAIN_URL)
    soup = BeautifulSoup(html)

    DIZI_BOLUM_URLS = []
    for season in soup.findAll('div', attrs={"class":"list-table"}):
        for a in season.findAll("a"):
            print a["href"]
            DIZI_BOLUM_URLS.append(a["href"])

    print "\n##########################################################\n"

    #bolum adreslerinden iframe linklerini al
    EMBED_URLS = []
    TITLES = []
    for url in DIZI_BOLUM_URLS:
        html = downloadUrl(url)
        soup = BeautifulSoup(html)

        em = soup.find("div", attrs={"id": "embed-wrapper"}).iframe["src"]
        title = soup.find("title").text
        print title, em
        EMBED_URLS.append(em)
        TITLES.append(title)

    print "\n##########################################################\n"

    #iframe'lerin icinden video linklerini al
    VIDEO_URLS = []
    for url in EMBED_URLS:
        html = downloadUrl(url)

        try:
            soup = BeautifulSoup(html)
            script = soup.body.find("script")
            mp4 = re.search('{"file": "(.*?)", "label": "360"', str(script)).group(1)
            print mp4
            VIDEO_URLS.append(mp4)
        except:
            print "olmadi"
            VIDEO_URLS.append("")

    return VIDEO_URLS, TITLES

def createFeed(links, titles):
    #feed dosyasini olustur
    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.id("http://twitter.com/dorukcankisin")
    fg.title(DIZI_TITLE)
    fg.author({'name':'dorukcan kisin','email':'dckisin@gmail.com'})
    fg.link(href='http://twitter.com/dorukcankisin', rel='alternate')
    fg.logo(DIZI_LOGO)
    fg.subtitle(DIZI_TITLE + ' videocast')
    fg.language('en')

    for i, url in enumerate(links):
        fe = fg.add_entry()
        fe.id(url)
        fe.enclosure(url, 0, 'video/mp4')
        fe.title(titles[i])
        fe.description(titles[i])

    fg.rss_file('rss.xml')
    return fg.rss_str(pretty=True)

if __name__ == '__main__':
    links, titles = fetch()
    xmlData = createFeed(links, titles)
    #do something with the xmlData, maybe upload to dropbox
