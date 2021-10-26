import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import time
from fpdf import FPDF
import socket
from datetime import datetime

class Report:
  window=None
  score=0
  url=""
  selection=""
  def createPieChart(self, score,url,selection):
    self.score=score
    self.url=url
    print(type(score))
    self.selection=selection
    labels = 'Vulnerable', 'Non-Vulnerable'
    
    negatescore=100-score
    sizes = [self.score,negatescore] 
    colors = ['red', 'green']
    explode = (0.4, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=15)
    plt.axis('equal')
    plt.savefig('result.png',bbox_inches='tight',dpi=100)
    plt.show()
    #plt.close(fig=
    self.createWindow(score,url,selection)

  def createWindow(self,score,url,selection):
    self.window=Tk()#creating window
    self.window.geometry("1536x864")
    self.window.resizable(True,True)
    self.window.title('Report')
    self.window.configure(bg='black')

    label1=Label(self.window,text=selection, bg='black',fg='white', font='helvetica 28 bold')
    label1.place(x=668,y=10, height=50,width=100)

    photo=PhotoImage(file="result.png")#the image
    label2=Label(self.window,image=photo)
    label2.place(x=500, y=100, height=400, width=500)

    button1=Button(self.window, text='Save', bg='green', fg='black', font='helvetica 14',command=self.handler)
    button1.place(x=600,y=600,  height=50,width=100)

    button2=Button(self.window, text='Exit', bg='red', fg='black', font='helvetica 14',command=self.closeWindow)
    button2.place(x=750,y=600,  height=50,width=100)
  
    self.window.mainloop()
  def closeWindow(self):
    messagebox.showinfo("Close","Thanks for using")#creating the exit window
    self.window.destroy()
  def handler(self):
    messagebox.showwarning("WARNING !!", " Make Sure Report.pdf is closed and no such file name is present on Desktop")
    self.createReport()#calling the create report function
    
    messagebox.showinfo("Save","File Saved on Desktop")
    #msgbox=messagebox.askquestion("Exit","Are you sure you wan't to exit")
    self.window.destroy()
    #if(msgbox=='yes'):
      
    #else:
     # messagebox.showinfo('Return','Returning to the Application')

  def getIP(self):
    hostname=socket.gethostname()
    ip_add=socket.gethostbyname(hostname)
    return ip_add

  def createReport(self):
    pdf=FPDF()#creating object
    pdf.add_page()#adding a page to pdf

    #Creating header
    pdf.set_font('Arial',style='B', size=12)
    pdf.cell(0,5," Critical Analysis of Web Portals",0,1,'C')

    #the main content
    pdf.set_font("Arial",style='B',size=16)#setting the font
    pdf.cell(0,10,self.selection.upper(),'B',1,'C')#heading
    
    pdf.set_font("Arial",style='',size=12)
    pdf.cell(0,10,"Site:\t \t"+self.url,0,1)#,0,0,'L'
    
    testsysip=self.getIP()#printing the testsystem IP
    pdf.cell(0,10,"Test System IP: \t"+testsysip,'',1)
    
    pdf.cell(0,10,"Test System Hostname: \t"+socket.gethostname(),0 ,1)

    pdf.cell(0,10,"Report Created ON: "+ str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")),'B',1)
 
    #displaying TEST RESULT
    pdf.set_font("Arial",style='B',size=14)#setting the test result
    pdf.cell(0,10,"TEST RESULT",'B',1,'C')

    pdf.image('result.png',50,85,w=125,h=100)
    pdf.cell(0,130," ",'',1,'C')#text not overwrite image
    
    #getting the records from stored file
    if(self.selection.lower()=="source code analyser"):
      file=open("WebScraper.html","r")#the result of Source Analyser is stored in html
    else:
      file=open("saveresult.txt","r")
    linecount=1

    #adding the value of file to the pdf
    pdf.set_font("Arial", size=10)
    for line in file:
      pdf.cell(0,10,str(linecount)+"    "+line,0,1,'L')
      linecount=linecount+1

    #setting footer
    #pdf.set_y(-10)
    #pdf.cell(0,10,"CopyRight DigitalEmbark.com"+ '/{nb}',0,1,'C')

    file.close()
    loop=1
    while(loop):
      try:
        pdf.output(r'C:\Users\arpit\Desktop\Report.pdf','F')
        loop=0
      except PermissionError:
        messagebox.showwarning("File Open","Report.PDF is already open")
    
    

#obj=Report()
#obj.createPieChart(15.6,"https://www.google.com","Source Analyser")
