import pandas as pd
import re
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.configure(background='light green')
root.title('GLA Online attedance absentee(based on official Email ID)')
root.geometry("500x250")

def browsefunc():
    root.mainfile = 'sec'+section.get()+'.csv'  # local csv file having all the details of the students with official emails 
    
    root.filename = askopenfilename() # browse csv file for from zoom 
def calc():    
    data = pd.read_csv(root.filename)
    data_main = pd.read_csv(root.mainfile)
    useremail = set(data['User Email'])
    main1 = data_main['Official Email-ID']
    main2 = data_main['Class Roll No']
    main_dict = dict(zip(main1, main2))
    
    data = list(set(main1)-set(useremail))
    ls = []
    for i in data:
        ls.append(main_dict.get(i))
    ls.sort()    
    pathlabel.config(text=str(ls))

##lastrolln = IntVar()
##lastrolln.set(70)
section = StringVar()
section.set('A')


ll1 = Label(root, text="Enter the section")
ll1.pack()
entry2 = Entry(root, textvariable=section )
entry2.pack()
##entry.grid(columnspan=4, ipadx=70) 

browsebutton = Button(root, text="Browse CSV file", command=browsefunc)
browsebutton.pack()
browsebutton = Button(root, text="show Absentee", command=calc)
browsebutton.pack()
pathlabel = Label(root)
pathlabel.pack()
