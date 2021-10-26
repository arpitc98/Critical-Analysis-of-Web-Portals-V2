import socket
import re

class NMAP:
  def NmapScan(self,url):
    #print("NMAP")
    #                         Scoring System
    openportcount=0
    closedportcount=0
    urlstrip=url
    
    #striping the http part because the code works on that
    if(re.search("https://www.",url)):
       urlstrip=url.strip("https://www.")
       
    elif(re.search("http://www.",url)):
      urlstrip=url.strip("http://www.")
      
    elif(re.search("https://",url)):
      urlstrip=url.strip("https://")
      
    elif(re.search("http://",url)):
      urlstrip=url.strip("http://www.")
    
    #print(urlstrip)
    ports=[80,25,443,20,21,23,143,3389,22,53,67,68,110,]
    
    file=open("saveresult.txt",'w')#opening file
    file.write("Open Ports")
    
    for port in ports:
      ip=socket.gethostbyname(urlstrip)
      result=self.portscan(port,ip)#calling the function
      
      if(result): #open port found
        file.write("\n")
        file.write(str(port))
        openportcount=openportcount+1
        
      else:
        closedportcount=closedportcount+1
        
    file.close()#closing the file
    return openportcount/(openportcount+closedportcount)


  def portscan(self, port,ip):
    try:
      sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      #print(sock)
      sock.connect((ip,port))
      return True #in case it connects    
    except :
      return False

