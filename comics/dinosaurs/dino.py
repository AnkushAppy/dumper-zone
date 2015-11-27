import urllib
base_url = 'http://www.qwantz.com/comics/comic2-'
for i in range (2850,2905):
        urllib.urlretrieve(base_url + str(i) + '.png','%s.png'%i)

