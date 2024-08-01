#Import modules and packages
import tkinter
import random
import tkinter.messagebox
#Create window
root = tkinter.Tk()

root.configure(bg="white")
root.title("My Super To Do List")
root.geometry("300x300")

#create emty list
tasks = []

#Test the task
tasks = ["call mom","eating "]


#Functions
def update_listbox():
    #clear list befor insert
    clear_listbox()

    #Populate the listbox
    for task in tasks:
        #insert tasks
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task(): 
    #get the tasknto add
    task = txt_input.get()
    if task!="":
        tasks.append(task)

        #update th listbox
        update_listbox()
    else:
        tkinter.messagebox.showwarning("warning","You need to enter the task")

    txt_input.delete(0,"end")
def del_all():
    confirm = tkinter.messagebox.askyesno("Please confirm","Do you really want to delete all ")
    if confirm == True:
        global tasks
        tasks = []
        update_listbox()

def del_one():
    #get the text of the current selected
    task = lb_tasks.get("active")
    #confirm it is in the lkist
    if task in tasks:
        tasks.remove(task)
    update_listbox()
def sort_acs():
    tasks.sort()
    update_listbox()

def sort_dsc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_rnd():
    #choose random tasks
    task = random.choice(tasks)
    lbl_display["text"]=task

def number_of_task():
    #get number of tasks
    number_of_task = len(tasks)
    msg = "Number of tasks: %s" %number_of_task
    lbl_display["text"]=msg
def quite():
    pass

lbl_title = tkinter.Label(root,text="To-Do-List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root,width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root,text="Add task",fg="green",bg="white",command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root,text="Delete All",fg="green",bg="white",command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root,text="Delete one",fg="green",bg="white",command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_acs = tkinter.Button(root,text="Sort(ASC)",fg="green",bg="white",command=sort_acs)
btn_sort_acs.grid(row=4,column=0)

btn_sort_dsc = tkinter.Button(root,text="Sort(DSC)",fg="green",bg="white",command=sort_dsc)
btn_sort_dsc.grid(row=5,column=0)

btn_choose_random = tkinter.Button(root,text="Choose random",fg="green",bg="white",command=choose_rnd)
btn_choose_random.grid(row=6,column=0)

btn_no_of_task = tkinter.Button(root,text="Number of task",fg="green",bg="white",command=number_of_task)
btn_no_of_task.grid(row=7,column=0)

btn_quite = tkinter.Button(root,text="Exite",fg="green",bg="white",command=quite)
btn_quite.grid(row=8,column=0)
 
lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()