"""GUI  
entries are : ISBN title author and year
view 
search entry 
add 
update
delete
close 
"""
from tkinter.constants import END
import backend as b
import tkinter as tk
from typing import Text 
def get_selected(event=None):
    global selected
    #gets the index of the row we are clicking 
    index=lb.curselection()[0]
    #get the line from the list which has the given index
    selected=lb.get(index)
    print (selected)
    e1.delete(0,END)
    e1.insert(END, selected[1])
    e2.delete(0,END)
    e2.insert(END, selected[2])
    e3.delete(0,END)
    e3.insert(END, selected[3])
    e4.delete(0,END)
    e4.insert(END, selected[4])

def view_command():
    lb.delete(0,END)
    for row in b.view():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in b.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        lb.insert(END,row)

def add_command():
    
    b.add(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    lb.delete(0,END)
    lb.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))



def delete_command():
    b.delete(selected[0])

def update_command():
    b.update(selected[0],selected[1],selected[2],selected[3],selected()[4])

window=tk.Tk()
window.title("Bookstore")
l1=tk.Label(window,text="Title")
l1.grid(row=0,column=0)
l2=tk.Label(window,text="Author")
l2.grid(row=0,column=2)
l3=tk.Label(window,text="Year")
l3.grid(row=1,column=0)
l4=tk.Label(window,text="ISBN")
l4.grid(row=1,column=2)

e1_value=tk.StringVar()
e1=tk.Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
e2_value=tk.StringVar()
e2=tk.Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3)
e3_value=tk.StringVar()
e3=tk.Entry(window,textvariable=e3_value)
e3.grid(row=1,column=1)
e4_value=tk.StringVar()

e4=tk.Entry(window,textvariable=e4_value)
e4.grid(row=1,column=3)
lb=tk.Listbox(window,height=6, width=35)
lb.grid(row=2, column=0,rowspan=6, columnspan=2)
lb.bind('<<LisboxSelect>>', get_selected)
sc=tk.Scrollbar(window)
sc.grid(row=2,column=2,rowspan=6)
lb.configure(yscrollcommand=sc.set)
sc.configure(command=lb.yview)

b1=tk.Button(window,text="View all",height=1,width=12, command=view_command)
b1.grid(row=2,column=3)


b2=tk.Button(window,text="Search entry",height=1,width=12, command=search_command)
b2.grid(row=3,column=3)


b3=tk.Button(window,text="Add entry",height=1,width=12,command=add_command)
b3.grid(row=4,column=3)


b4=tk.Button(window,text="Update",height=1,width=12,command=update_command)
b4.grid(row=5,column=3)


b5=tk.Button(window,text="Delete",height=1,width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=tk.Button(window,text="Close",height=1,width=12)
b6.grid(row=7,column=3)



window.mainloop()

