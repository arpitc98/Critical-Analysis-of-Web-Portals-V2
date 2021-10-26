import requests
import time
import sys
class XSS:
  def XSSInjection(self, url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    pog = 'g'
    #print (pog)
    lineexe=0#number of malicious queries
    queryexe=0#no of queries executed
    if pog == "g" :
      try:
        site=url
        #site = input("URL : ")
        r = requests.post(site, headers=header)
        time.sleep(1)
        print()
        #print("The site respond !" )
      except:
        print()
        #print('does the script respond...')
        time.sleep(3)
        print()
        #print("The Site doesn't respond, try again. (with https:// or http:// ...)")
        sys.exit(0)
        print()
      try:
        payload = open("xss.txt", "r")#reading the file
      except FileNotFoundError:#if we don't find the file
        print()
        #print("The file doesn't exists, try again !")
        sys.exit(0)
      print()
      #print("Test in progress... \n")
      time.sleep(1)
      f = open("xss.txt","r")
      l = 1
      file=open("saveresult.txt","w")
      for line in f:
        lineexe=lineexe+1
        print()
        #print("Testing payload " + str(line))
        if line in requests.get(site + line, headers=header).text:
          queryexe=queryexe+1
          file.write(line)#adding the query to the file
          #print("XSS FOUND HERE : \n"+ line)
          #print(requests.get(site + line, headers=header).url)
        else:
          #print(" The payload" + str(line) + "does not trigger the XSS Filter." )
          print()
          l == 1
      return(queryexe/lineexe)
    else:
      #print("unknown answer ")
      sys.exit(0)

#obj=XSS()
#obj.XSSInjection('http://leettime.net/xsslab1/sta_ge2.php?name=abc')
