class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"name": task, "status": "Pending"})

    def list_tasks(self):
        return [task["name"] for task in self.tasks]

    def mark_as_completed(self, task):
        for t in self.tasks:
            if t["name"] == task:
                t["status"] = "Completed"
                break

    def clear_tasks(self):
        self.tasks = []
