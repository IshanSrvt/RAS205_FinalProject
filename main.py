'''
RAS205 Final Project
Dynamic Task Scheduler for Smart Manufacturing
Team: Write your team name here
'''

'''
Ishan did this part: created the TaskScheduler class and stored the task list.
'''
class TaskScheduler:

    '''
    Ishan did this part: this function starts the object with the given tasks.
    '''
    def __init__(self, tasks):
        self.tasks = tasks

    '''
    Aadi did this part: this function makes an empty timeline using max deadline.
    '''
    def make_empty_schedule(self):
        if len(self.tasks) == 0:
            return []

        max_deadline = max(task[1] for task in self.tasks)

        if max_deadline <= 0:
            return []

        return ["Free"] * max_deadline

    '''
    Aadi did this part: this function prints the schedule in a simple way.
    '''
    def print_schedule(self, schedule):
        for i in range(len(schedule)):
            print("Time Slot", i + 1, ":", schedule[i])

    '''
    Ishan and Aadi did this part: this function schedules tasks using greedy method.
    '''
    def schedule_tasks(self):
        schedule = self.make_empty_schedule()
        total_profit = 0

        '''
        Sort tasks by highest profit first.
        '''
        sorted_tasks = sorted(self.tasks, key=lambda x: x[2], reverse=True)

        '''
        Try to place each task in the latest free slot before its deadline.
        '''
        for task in sorted_tasks:
            task_id = task[0]
            deadline = task[1]
            profit = task[2]

            '''
            Skip task if deadline is not valid.
            '''
            if deadline <= 0:
                continue

            '''
            Start from the last possible slot for this task.
            '''
            last_slot = min(deadline, len(schedule)) - 1

            '''
            Move backward until a free slot is found.
            '''
            for i in range(last_slot, -1, -1):
                if schedule[i] == "Free":
                    schedule[i] = task_id
                    total_profit += profit
                    break

        return total_profit, schedule

    '''
    Ishan did this part: this function runs and prints the full result.
    '''
    def show_result(self):
        empty_schedule = self.make_empty_schedule()

        print("Initial Empty Timeline:")
        self.print_schedule(empty_schedule)

        print()

        total_profit, final_schedule = self.schedule_tasks()

        if total_profit == 0:
            print("No feasible tasks could be scheduled")
        else:
            print("Final Filled Schedule:")
            self.print_schedule(final_schedule)
            print()
            print("Total Profit:", total_profit)


'''
Aadi did this part: this function runs one test case.
'''
def run_case(case_name, tasks):
    print()
    print(case_name)
    print()

    scheduler = TaskScheduler(tasks)
    scheduler.show_result()


'''
Original problem task list.
'''
original_tasks = [
    ("T1", 5, 35),
    ("T2", 3, 30),
    ("T3", 4, 25),
    ("T4", 2, 20),
    ("T5", 7, 15),
    ("T6", 6, 40),
    ("T7", 5, 50)
]

'''
Test case A: no conflicts.
'''
test_a = [
    ("T1", 3, 15),
    ("T2", 2, 20),
    ("T3", 4, 30),
    ("T4", 1, 10)
]

'''
Test case B: conflicting deadlines.
'''
test_b = [
    ("T1", 4, 20),
    ("T2", 1, 10),
    ("T3", 1, 40),
    ("T4", 1, 30)
]

'''
Test case C: infeasible scheduling.
'''
test_c = [
    ("T1", 0, 25),
    ("T2", 0, 15)
]


'''
Ishan and Aadi did this part: running original problem and all test cases.
'''
run_case("Original Problem", original_tasks)
run_case("Test Case A: No Conflicts", test_a)
run_case("Test Case B: Conflicting Deadlines", test_b)
run_case("Test Case C: Infeasible Scheduling", test_c)