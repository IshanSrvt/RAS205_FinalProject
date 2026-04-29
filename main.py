'''
RAS205 Final Project
Dynamic Task Scheduler for Smart Manufacturing
Team members: Ishan Srivastava, Aadi Kadam, Jared Chapman, Sara Doyle, Sakiya Mason, Becky Baker
'''

''' Sakiya: created the TaskScheduler class and started the system '''
class TaskScheduler:


    ''' Sakiya: stores the task list and finds the max deadline '''
    def __init__(self, tasks):
        self.tasks = tasks
        self.max_deadline = self.find_max_deadline()

    ''' Sakiya: finds the biggest deadline from all tasks '''
    def find_max_deadline(self):
        if len(self.tasks) == 0:
            return 0

        return max(task[1] for task in self.tasks)

    ''' Sakiya: makes an empty timeline using max deadline '''
    def make_empty_schedule(self):
        if self.max_deadline <= 0:
            return []

        return ["Free"] * self.max_deadline

    ''' Jared: this function prints the schedule clearly '''
    def print_schedule(self, schedule):
        for i in range(len(schedule)):
            print("Time Slot", i + 1, ":", schedule[i])

    ''' Aadi: sorts tasks by highest profit first '''
    def sort_tasks(self):
        return sorted(self.tasks, key=lambda x: x[2], reverse=True)

    ''' Ishan: schedules tasks using greedy method '''
    def schedule_tasks(self):
        schedule = self.make_empty_schedule()
        total_profit = 0

        ''' Aadi: prepared the sorted task list for scheduling '''
        sorted_tasks = self.sort_tasks()

        ''' Ishan: checks each task and tries to place it before its deadline '''
        for task in sorted_tasks:
            task_id = task[0]
            deadline = task[1]
            profit = task[2]

            ''' Sara: handles invalid deadline edge case '''
            if deadline <= 0:
                continue

            ''' Ishan: starts from the latest possible time slot '''
            last_slot = min(deadline, len(schedule)) - 1

            ''' Ishan: moves backward until a free slot is found '''
            for i in range(last_slot, -1, -1):
                if schedule[i] == "Free":
                    schedule[i] = task_id
                    total_profit += profit
                    break

        return total_profit, schedule

    ''' Jared: prints the initial schedule, final schedule, and total profit '''
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


''' Sara: runs one test case and helps verify output '''
def run_case(case_name, tasks):
    print()
    print(case_name)
    print()

    scheduler = TaskScheduler(tasks)
    scheduler.show_result()


''' Becks: combined the original problem input into the final code file '''
original_tasks = [
    ("T1", 5, 35),
    ("T2", 3, 30),
    ("T3", 4, 25),
    ("T4", 2, 20),
    ("T5", 7, 15),
    ("T6", 6, 40),
    ("T7", 5, 50)
]

''' Sara: test case A checks no conflict case '''
test_a = [
    ("T1", 3, 15),
    ("T2", 2, 20),
    ("T3", 4, 30),
    ("T4", 1, 10)
]

''' Sara: test case B checks conflicting deadline case '''
test_b = [
    ("T1", 4, 20),
    ("T2", 1, 10),
    ("T3", 1, 40),
    ("T4", 1, 30)
]

''' Sara: test case C checks infeasible scheduling case '''
test_c = [
    ("T1", 0, 25),
    ("T2", 0, 15)
]


''' Becks: final integration runs original problem and all test cases '''
run_case("Original Problem", original_tasks)
run_case("Test Case A: No Conflicts", test_a)
run_case("Test Case B: Conflicting Deadlines", test_b)
run_case("Test Case C: Infeasible Scheduling", test_c)
