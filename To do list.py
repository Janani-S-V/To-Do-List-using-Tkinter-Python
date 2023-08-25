import tkinter
from tkinter import *
root=Tk()
root.configure(bg="white")
root.title("To do list")
root.geometry("200x500")
tasks=[]
def update_listbox():
    clear_listbox()
    for task in tasks:
        ltasks.insert("end",task)
def clear_listbox():
    ltasks.delete(0,"end")
def add():
    task=input.get()
    if task !="":
       tasks.append(task)
       update_listbox()
    else:
        display["text"]="Please enter any task"
    input.delete(0,"end")
def dele():
    display["text"]="Please enter any task"
    task=ltasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()
def delall():
    display["text"]="Please enter any task"
    global tasks
    tasks=[]
    update_listbox()
def asort():
    tasks.sort()
    update_listbox()
def dsort():
    tasks.sort()
    tasks.reverse()
    update_listbox()
def total():
    total_task=len(tasks)
    msg="Number of tasks:%s" %total_task
    display["text"]=msg
display=Label(root,text="To do list",bg="white")
display.pack()
input=Entry(root,width=15)
input.pack()
add_task=Button(root,text="Add",bg="green",width=8,height=1,command=add)
add_task.pack()
total_task=Button(root,text="Total",bg="purple",width=8,height=1,command=total)
total_task.pack()
asort_task=Button(root,text="Sort asc",bg="brown",width=8,height=1,command=asort)
asort_task.pack()
del_task=Button(root,text="Remove",bg="olive",width=8,height=1,command=dele)
del_task.pack()
dsort_task=Button(root,text="Sort desc",bg="teal",width=8,height=1,command=dsort)
dsort_task.pack()
delall_task=Button(root,text="Remove all",bg="brown",width=8,height=1,command=delall)
delall_task.pack()
quit_task=Button(root,text="Exit",bg="orange",width=8,height=1,command=exit)
quit_task.pack()
ltasks=Listbox(root)
ltasks.pack()
root.mainloop()


