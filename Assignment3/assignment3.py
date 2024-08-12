class Task:
    def __init__(self, title, description=""):
        self.title=title
        self.description= description
        self.status="incomplete"
        
    def mark_complete(self):
        self.status="complete"
        
    def __str__(self):
        return f"Task:{self.title}\nDescription:{self.description}\nStatus:{self.status}"
    
        
class TaskList:  
    def __init__(self):
        self.tasks=[]
        
    def add_task(self, title, description=None):
        if description is None:
            task= Task(title)
        else:
            task= Task(title, description)
        self.tasks.append(task)
        
    def remove_task(self, title):
        self.tasks=[task for task in self.tasks if task.title != title]
        
    def list_all_tasks(self):
        for task in self.tasks:
            print(task)
            print("-" *30)
            
    def find_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
            
# PriorityTask class inherits from Task and adds priority
class PriorityTask(Task):
    def __init__(self, title, description="", priority="low"):
        super().__init__(title, description)
        self.priority = priority
        
    # Override __str__ method to include priority
    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nStatus: {self.status}\nPriority: {self.priority}"    


def main():
    task_list = TaskList()

    task_list.add_task("Do homework")

    task_list.add_task("Go to the gym", "Cardio workout")

    # Adding a priority task
    priority_task = PriorityTask("Buy groceries", "Milk and eggs", "high")
    task_list.tasks.append(priority_task)

    task_list.list_all_tasks()

    task_list.find_by_title("Go to the gym").mark_complete()

    print(task_list.find_by_title("Do homework"))
    
    print("#" *30)

    print(task_list.find_by_title("Buy groceries"))


if __name__ == "__main__":
    main()