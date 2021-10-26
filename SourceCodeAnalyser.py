import requests
from bs4 import BeautifulSoup
import re #regular expressions module

class SourceAnalyser:
  def sa(self,url):
    score=0
    page = requests.get(url)
    #using beautifulsoup for form tag
    soup = BeautifulSoup(page.content, 'html.parser')
    formtag=soup.find_all('form')
    string =""
    for constr in formtag:
      string=string.lower() + str(constr) #converting it to string
        #   print(string.islower())
    #print(string) 
    #writing content to the file
    file=open("WebScraper.html","w")
    file.write(string)
    file.close()
    
    #reading content of file
    fileread=open("WebScraper.html","r")
    
    # SEPARATING EACH FORM TAG
    individualformtag=[] #blank array where content of multiple formtags will be stored
    string=""
    for line in fileread.readlines():#reading line by line
      #print(line)
      if( re.search("<form",line)): #if we find the starting of form tag *-*
        string=string+line+"\n" #\n will be used be us to figure out different lines
        #print("\n\nFORM TAG",string)
    
      elif(  re.search("</form",line.lower() ) ):#when we reach the end of form tag
        individualformtag.append(string) #adding string to array
        string=""#once we have appended into array then we reset the string
      
      else:
        string=string+line+"\n"#adding rest of the lines
      #print(string)
    flag=""
    for lines in individualformtag:
      #print(lines)
      splitline=lines.split("\n") #splitting the content of the retrieved set of form items#}
      #print("SPLITLINE: ",splitline)#*****
      for lineslower in splitline:
        #print("Lines Lower:",lineslower)
        if(lineslower==""): 
          print()#"-"
        else:
          print()#"*"
       
        if(re.search("method=",lineslower) ):#and re.search("get",lineslower)):#all possible variation of method=get will be added
          #print("check get")
          if(re.search("get",flag)):
            print()
          else:
            flag=flag+"get " #if we find get method then we need to add it to the flag variable
      

        if(re.search("type=",lineslower) and re.search("text",lineslower)):#and re.search("=\"\"",lineslower
          #print("check text")
          if(re.search("text",flag)):#if we don't find in flag variable
            print()
          else:
            flag=flag+"text "#figure out one more point that will be used to identify username


        if(re.search("type=",lineslower) and re.search("length",lineslower)and re.search("password",lineslower) ):
          #print("check password")
          if(re.search("password",flag)):
            print()
          else:
            flag=flag+"password "
    #from here our scoring code starts
    if(re.search("get",flag) and not(re.search("text",flag)) and  not(re.search("password",flag))  ):
      #print("\nGET")
      return 40
     
    elif(re.search("text",flag) and not(re.search("get",flag)) and not(re.search("password",flag))):
      #print("\nTEXT")
      return 25
  
    elif(re.search("password",flag) and not(re.search("text",flag)) and not(re.search("get",flag))):
      #print("\nPASSWORD")
      return 35
  
    elif(re.search("get",flag) and re.search("text",flag) and not(re.search("password",flag))):
      #print("GET & TEXT")
      return 80
  
    elif(re.search("get",flag) and re.search("password",flag) and not(re.search("text",flag))):
      #print("GET&PASSWORD")
      return 90
  
    elif(re.search("get",flag) and re.search("text",flag) and re.search("password",flag)):
      #print("GET, TEXT& PASSWORD")
      return 100
  
    elif(re.search("text",flag) and re.search("password",flag) and not(re.search("get",flag))):
     # print("TEXT & PASSWORD")
      return 30#if the request method is not get then it is post
      
    #return score
#obj=SourceAnalyser()
#score=obj.sa('http://testphp.vulnweb.com')
#print(score)
#return score

 
