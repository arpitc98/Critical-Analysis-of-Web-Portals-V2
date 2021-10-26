from NMAP import *
from SQLi import *
from XSSi import *
from Default import *
from LinkFinder import *
from SourceCodeAnalyser import *
from Report import *

class Controller:
  def malicious(self,url,selection):
    self.score=0
    if(selection=="sql injection"):
      sqlscore=0
      sqlobj= SQLAutomation()
      self.score=sqlobj.SQLInjection(url)#sqlscore
      
    elif(selection=="xss"):
      xssscore=0
      xssobj=XSS()
      #print("Xsss")
      xssscore=xssobj.XSSInjection(url)#return  value
      self.score=xssscore*100#because the value returned is in fractions
      
    elif(selection=="open port"):
      nmapscore=0
      #print("NMAP")      
      nmobj= NMAP()
      self.score=nmobj.NmapScan(url)*100#nmap
      #the result is in fractions
      
    elif(selection=="brute force"):
      dupscore=0
      defaultobj=Default(url)
      #self.score=defaultobj.timePass(1)
      #forms=defaultobj.usernamePassword(url)
      #defaultobj.find(forms,url)
      #usernamepassword(url)
      
    elif(selection=="link analyser"):
      lfobj=LinkFinder()
      self.score=lfobj.LF(url)
      
    elif(selection=="source code analyser"):
      scaobj=SourceAnalyser()
      #print(scaobj.sa(url))
      self.score=scaobj.sa(url)
    #print(type(self.score))
    #print("Value: ",self.score)
    reportobj= Report()
    reportobj.createPieChart(self.score,url,selection)

