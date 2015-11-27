from lxml import html,etree
import csv
import urllib2
from xml.dom import minidom
from xml.dom.minidom import parseString
import re


class Espacenet(object):
    def __init__(self,array):
        if array:
            self.datain=csv.reader(open(array,'rU'))
            self.dataou=open('Espace_output.csv','wb')
            self.dataout=csv.writer(self.dataou)
            self.errors=csv.writer(open('Errors.csv','wb'))
            self.pattern = re.compile(r'<.*?>')
            self.list2=['Input_no','Espacenet_no']
            self.Baseurl="http://ops.epo.org/3.1/rest-services/published-data/search/abstract/?q="
            self.dataout.writerow(self.list2)
            
    def Espacedata(self):
        for index,data in enumerate(self.datain):
            if index==0:
                continue
            else:
                #print index
                list2=[]
                url=self.Baseurl+data[0]
                list2.append(data[0])
                main_page=urllib2.urlopen(url)
                xmldoc = minidom.parse(main_page)
                
                itemlist = xmldoc.getElementsByTagName('exchange-document')
                
                for item in itemlist:
                    try:
                        list1=[]
                        xmlTag1=item.getElementsByTagName('document-id')[0].toxml()
                        country=item.getElementsByTagName('country')[0].toxml()
                        list1.append(self.pattern.sub('', country))
                        pub_number=item.getElementsByTagName('doc-number')[0].toxml()
                        list1.append(self.pattern.sub('', pub_number))
                        Kind=item.getElementsByTagName('kind')[0].toxml()
                        list1.append(self.pattern.sub('', Kind))
                        Publication_Number="".join(list1)
                        list2.append(Publication_Number)
                        break
                    except:
                        list2.append("Error Message")
                        break
                   

                self.dataout.writerow([unicode(s).encode("utf-8") for s in list2])
        print "Done"
        self.dataou.close()
              
if __name__=="__main__":

    obj=Espacenet('EP1.csv')
    obj.Espacedata()
