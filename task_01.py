##############################
#                            #
# MD MEZBAH UDDIN            #
# Nantong University(China)  #
# CSE                        #
#                            #
##############################

import datetime
import uuid
 
class Task:
    tasks = {}
    task_count = 0
 
    def __init__(self, task, id=None):
        self.task = task
        self.created_time = datetime.datetime.now()
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False
        self.id = id or uuid.uuid4()
        Task.tasks[Task.task_count] = self
 
        Task.task_count += 1
 
    def update_task(self,task):
        self.task = task
        self.updated_time = datetime.datetime.now()
 
    def complete_task(self):
        self.task_done = True
        self.completed_time = datetime.datetime.now()
 
    def __str__ ( self ):
        return f"\nID: {self.id}" \
               f"\nTask: {self.task}" \
               f"\nCreated Time: {self.created_time}"\
               f"\nUpdated Time: {self.updated_time}"\
               f"\ncomplete Task: {self.task_done}"\
               f"\nCompleted Time: {self.completed_time}\n"\
 
    @classmethod
    def show_tasks(clas):
        for task_number,task in clas.tasks.items():
            print(task)
 
    @classmethod
    def show_tasks_with_No(clas):
        for task_number, task in clas.tasks.items ():
            if task.task_done == False:
                print(f"Select yout task ")
                print(f"Task No - {task_number}{task}")
               
 
    @classmethod
    def update_task_by_No(clas, task_number,task):
        if task_number in clas.tasks:
            clas.tasks[task_number].update_task(task)
        else:
            print("your Task not found")
    @classmethod
    def complete_task_by_No(cls, task_number):
        if task_number in cls.tasks:
            cls.tasks[task_number].complete_task()
        else:
            print("Your Task not found")
 
    @classmethod
    def show_incomplete_tasks(cls):
        data = False
        for task_number,task in cls.tasks.items():
            if task.task_done == False:
                print (task)
                data = True
        if not data:
            print ("your all task  Completed.")
 
    @classmethod
    def show_complete_tasks(cls):
        data = True
        for task_number,task in cls.tasks.items():
            if task.task_done == True:
                print (task)
                data = False
        if data:
            print("Not complete your task....")
 
while True:
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Task")    
    print("4. Show complete Task")    
    print("5. Update Task")    
    print("6. Mark a Task Complete")  
 
    ent_option = int(input("Enter Option: "))
 
    if ent_option == 1:
        Task(input("enter your New task: "))
        print("Task created Successfully")
        
    if ent_option == 2:
        Task.show_tasks()
 
    if ent_option == 3:
        Task.show_incomplete_tasks()
 
    if ent_option == 4:
        Task.show_complete_tasks()
 
    if ent_option == 5:
        Task.show_tasks_with_No()
        get_option = int (input ("Enter task No: "))
        get_task = input("Enter New Task: ")
        
 
        Task.update_task_by_No(get_option,  get_task)
 
    if ent_option == 6:
        Task.show_tasks_with_No()
        Task.complete_task_by_No(int(input("Enter task No: ")))
 

