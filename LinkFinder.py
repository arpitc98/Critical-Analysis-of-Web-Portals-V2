from bs4 import BeautifulSoup
import re # the regex module which eases the search
import requests #request module

class LinkFinder:
  def LF(self, url):
    page=requests.get(url)
    #using beautifulsoup tag for 'a' tag
    soup=BeautifulSoup(page.content,'html.parser')
    atag=soup.find_all('a')#finding all the a tag

    file=open("links.txt","w")#opening file in read mode

    alllinks=[]

    for line in atag:
      file.write(line.get('href'))
      file.write('\n')
      alllinks.append(line.get('href'))
    file.close()


    countline=0
    httpcount=0
    ftpsite=0
    file=open("saveresult.txt","w")
    for line in alllinks:
      countline=countline+1
      if(re.search("http:",line)):
         httpcount=httpcount+1
         file.write("\nHTTP Link:")
         file.write(line)
         #print("HTTP:",line)

      if(re.search("ftp:",line)):
         ftpcount=ftpcount+1
         file.write("\n FTP Link:")
         file.write(line)
         print("FTP: ",line)
    file.close()#closing the file
    return((httpcount+ftpsite)/countline)#returning the score

#lfobj=LinkFinder()
#lfobj.LF('http://testphp.vulnweb.com/')

  
