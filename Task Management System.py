#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Define the Task Class

class Task:
    def _intit_(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False # task is not completed initially 
    
    def _str_(self):
        return f"Task: {self.description}, priority: {self.priority}, due_date: {self.due_date}, completed: {self.completed}"
    


# In[8]:


# Implement Task Storage (Linked List or Stack)

class Node:
    def _int_(self, task):
        self.task = task
        self.next = None
        
class Tasklist:
    def _int_(self):
        self.head = None
    
    def add_task(self, task):
        new_node = node(task)
        new_node.next = self.head
        self.head = new_node
        
    def view_tasks(self):
        current = self.head
        if not current:
            print("No tasks available.")
            return
        while current:
            print(current.task)
            current = current.next
            
    def mark_task_completed(self, task_description):
        current = self.head
        while current:
            if current.task.description == task_description:
                current.task.completed = True
                print(f"Task '{Task_description}' marked as completed")
                return
            
            current = current.next
        print("Task not found.")
        


# In[11]:


# Add Sorting and Searching
def sort_task_by_priority(task_list):
    tasks = []
    current = task_list.head
    while current:
        tasks.append(current_task)
        current = current.next
    tasks.sort(key=lambda x: x.priority)   # sorting tasks based on priority
    for task in tasks:
        print(task)


# In[12]:


# Searching tasks by priority
def serach_task(task_list, keyword):
    current = task_list.head
    while current:
        if keyword.lower() in current.tast.description.lower() or keyword.lower() in current.task.priority.lower():
            print(current.task)
        current = current.next


# In[16]:


# Add the main Menu

def main():
    task_list = TaskList()
    
    while True:
        print("\n Task Management System")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Completed")
        print("4. Sort Task by Priority")
        print("5. Search Task")
        print("6. Exit")
        
        choice = input("Enter your Choice:")
        
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low, Medium, High): ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            task = Task(description, priority, due_date)
            task_list.add_task(task)
            
        elif choice == "2":
            task_list.view.tasks()
        
        elif choice == "3":
            task_description = input("Enter task description to mark as completed: ")
            task_list.mark_task_completed(task_description)
            
        elif choice == "4":
            print("Task sorted by priority: ")
            sort_task_by_priority(task_list)
            
        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            search_task(task_list, keyword)
            
        elif choice == "6":
            print("Exiting Task Management System.")
            
            break
            
        else:
            print("Invalid Choice. Please try again.")


# In[ ]:





# In[ ]:




