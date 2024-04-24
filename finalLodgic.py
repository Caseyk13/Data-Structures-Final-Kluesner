import heapq
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

class UnitedQueque:

    def __init__(self,jobs ):
        self.jobs = jobs =[[]]
        united = heapq.heapify(self.jobs)



    def heap(self):
        united = heapq
        united.heapify(self.jobs)



    def addJob(self):
        self.jobs.append()


    def deleteAll(self):
        for job in self.jobs:
            heapq.heappushpop(self.jobs)


    def deleteOne(self):
        pass


    def topPirority(self):

        return self.jobs.sort()



    def lowPirority(self):
        united = heapq
        self.jobs.sort()
        self.jobs.reverse()




    def numJobs(self):

        hi = len(self.jobs)
        return f"Your Number Of Current Job's Is:",hi




