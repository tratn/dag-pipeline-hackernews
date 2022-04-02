from dag import DAG

class Pipeline:
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        """Add task to graph"""
        def inner(f):
            # call the add() method to add tasks to graph
            self.tasks.add(f)
            if depends_on: 
                self.tasks.add(depends_on, f)
            return f
        return inner
    
     def run(self):
        """Run the dag"""
        # sort the tasks from most depended to least depended 
        sorted_tasks = self.tasks.sort()    
        completed = {}       # keep track of completed tasks
        # iterate through each task
        for task in sorted_tasks: 
            # check in each node of the graph if the task is referenced
            for node, linked_to in self.tasks.graph.items():
                # if referenced, it means the current node must be run first 
                if task in linked_to:
                    completed[task] = task(completed[node])    # run the current node and add to completed 
            # if the task is not referenced, it does not depended on current node 
            if task not in completed:
                completed[task] = task()     # run the task and add to completed 
        return completed