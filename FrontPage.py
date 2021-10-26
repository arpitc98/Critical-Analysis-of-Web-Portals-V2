from tkinter import *
from PIL import ImageTk,Image
from Controller import *
#from controller import * # this is the controller file that will be calling other modules

#creating a window for placing all the items
window=Tk()

#declaring all the variables here
url=""
dropvalue=StringVar(window)

window.geometry("1536x864")#setting the Initial Size
window.resizable(True,True)#setting the window to be resizable
window.title("Website Analyser")

#creating button properties
def on_enter(e):
    button1['background'] = 'black'
    button1['foreground']='green'

def on_leave(e):
    button1['foreground'] = 'black'
    button1['background']='green'

def checkURL(url):
    if(re.search('https://www.',url)):
        return 0
    elif(re.search('https://',url)):
        return 0
    elif(re.search('http://www/',url)):
        return 0
    elif(re.search('http://',url)):
        return 0
    else:
        messagebox.showwarning('Incorrect URL','Please Check the URL and try again')
        return 1

#creating button handler 
def buttonHandler():#function that will be used to handle button
  obj=Controller()
  url=entry1.get().lower()#getting the value and converting it to a lower form
  selection=dropvalue.get().lower()#get & convert Lower
  #print("URL: ",url, "\tDropValue:",selection)
  retvalue=checkURL(url)
  if(retvalue==0):
      window.destroy()
      obj.malicious(url,selection)
  else:
     print()



#setting the background Image
bcgimage=PhotoImage(file="background.png")
background_label = Label(window, image=bcgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



"""photo= PhotoImage(file="logo.png")
logo=Label(window, image=photo)
logo.photo=photo
logo.place(x=1100 ,y=100, height=200, width=200)"""


#Creating URL Lable
label = Label(window, text='URL:', bg='black', fg='white',font='helvetica 14 bold')
#label.config(font=('helvetica', 10))
label.place(x=950, y=350, height=45, width=50)


#Creating Input Box for URL
entry1 = Entry (window) ##url textbox you will get value here,textvariable=url
entry1.config( font='helvetica 14 ')
entry1.place(x=1000, y=350,height=45, width=440)


#creating the dropdown list
options=["SQL INJECTION","XSS","OPEN PORT","BRUTE FORCE","LINK ANALYSER","SOURCE CODE ANALYSER"]
#dropvalue=StringVar(window)
dropvalue.set("Select An Option:")# this will be the default text appearing on the dropdown

drop=OptionMenu(window,dropvalue,*options)#, font='helvetica 14 bold'
drop.config( bg='black', fg='white', font='helvetica 14 bold',highlightbackground='green')
drop.pack()
drop.place(x=1040,y=410,height=45,width=350) ##dropdown menu you will get value here




#creating button
button1 = Button(window,text='Calculate',bg='green',fg='black', command=buttonHandler, font="helvetica 14 bold")
button1.place(x=1150 ,y=470, height=45, width=100)
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)



label2=Label(window, text="Created By DigitalEmbark.com", bg='black', fg='cyan',font="helvetica 20 bold")
label2.place(x=950, y=800, height=50, width=600)


window.mainloop()

#print("Width:",window.winfo_screenwidth(),"Height:", window.winfo_screenheight())



