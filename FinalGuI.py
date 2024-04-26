import heapq
import tkinter
import finalLodgic
from finalLodgic import UnitedQueque


''''
* Name : Program Name
* Author: Casey Kluesner 
* Created : 04/30/2022
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 10
* IDE: , PyCharm 2023.2, 
* Copyright : This is my own original work 
* based onspecifications issued by our instructor
* Description : An app that builds a job list based on the user input implementing a heap to do so.
*            Input: user input.
*            Ouput: a job list GUI.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
'''

root = tkinter.Tk()
jobs = [["Please InPut Your Job's"]]

u = UnitedQueque(jobs)

root.configure(bg="White")

root.geometry("200x500")

lblTitle = tkinter.Label(root, text="United Services Job List", bg="Red")
lblTitle.pack()



def updateListBox():
    clearList()
    for job in jobs:
        listBoxone.insert("end",job)

def clearList():
   listBoxone.delete(0,"end")

def addJob():

  job = textInput.get()

  jobs.append(job)

  updateListBox()
  u.heap()


def deleteAll():
    global jobs
    jobs = [[]]
    a = "You Have No More Job's Yay !!!!!!"
    lblDisply["text"] = a
    updateListBox()

def lowPirority():
    u.lowPirority()
    jobs.reverse()
    updateListBox()
def numJobs():
    u.numJobs(jobs, u.heap())

def topPirority():
    u.topPirority()
    jobs.reverse()
    jobs

    updateListBox()
    u.heap()

def numJobs():
 num = f"Your Number Of Job's Is:", len(jobs)-1
 lblDisply["text"] = num
 updateListBox()

def deleteOne():
 job =listBoxone.get("active")
 if job in jobs:
  jobs.remove(job)

 updateListBox()
 u.heap()



lblDisply = tkinter.Label(root, text=" ", bg="White")
lblDisply.pack()


textInput = tkinter.Entry(root, width=25)
textInput.pack()

listBoxone = tkinter.Listbox(root)
listBoxone.pack()

bttnAdd = tkinter.Button(root, text="Add A Job", fg="red", bg="white", command=addJob)
bttnAdd.pack()

bttnDeletAll = tkinter.Button(root, text="Delete All", fg="red", bg="white", command=deleteAll)
bttnDeletAll.pack()

bttnDeleteJob = tkinter.Button(root, text="Remove Job", fg="red", bg="white", command=deleteOne)
bttnDeleteJob.pack()

bttnSorthi = tkinter.Button(root, text="Sort By Newest", fg="red", bg="white", command= topPirority)
bttnSorthi.pack()

bttnsortLow = tkinter.Button(root, text="Sort By Oldest", fg="red", bg="white", command=lowPirority)
bttnsortLow.pack()

bttnnumJobs = tkinter.Button(root, text="Number Of Jobs", fg="red", bg="white",command=lambda :numJobs())
bttnnumJobs.pack()

bttnexit = tkinter.Button(root, text="Exit", fg="red", bg="white", command=exit)
bttnexit.pack()



root.mainloop()
