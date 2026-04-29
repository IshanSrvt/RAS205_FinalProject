# 🚀 Dynamic Task Scheduler for Smart Manufacturing  
### Greedy Algorithm | RAS205 Final Project  

<p align="center">
  <b>Maximize profit. Minimize chaos. Schedule smart ⚙️</b>
</p>

---

## 👥 Team

| Name | Role |
|------|------|
| Ishan Srivastava | Core Algorithm |
| Aadi Kadam | Sorting Logic |
| Jared Chapman | Output & Formatting |
| Sara Doyle | Testing & Debugging |
| Sakiya Mason | Initialization & Setup |
| Becks | Documentation & Integration |

---

## 📌 Problem Statement

A smart manufacturing plant must schedule tasks where:

- Each task has a **deadline** ⏳  
- Each task gives a **profit** 💰  
- Only **one task per time slot** is allowed  

### 🎯 Goal:
Maximize total profit while completing tasks **before deadlines**

---

## 🧠 Algorithm Strategy: Greedy

The algorithm follows a greedy approach:

1. Sort tasks by **profit (highest first)**  
2. Pick the most profitable task  
3. Place it in the **latest available slot before its deadline**  
4. Repeat for remaining tasks  

---

## ⚙️ How It Works (Flowchart)

flowchart TD
    A[Start] --> B[Store Task List]
    B --> C[Find Maximum Deadline]
    C --> D[Create Empty Schedule]
    D --> E[Sort Tasks by Profit Descending]
    E --> F[Select Next Task]
    F --> G{Deadline > 0?}
    G -->|No| F
    G -->|Yes| H[Find Latest Free Slot]
    H --> I{Slot Available?}
    I -->|Yes| J[Assign Task to Slot]
    I -->|No| K[Move Backward]
    K --> I
    J --> L[Add Profit]
    L --> M{More Tasks?}
    M -->|Yes| F
    M -->|No| N[Print Schedule & Total Profit]
    N --> O[End]

TaskScheduler
│
├── __init__()              → store tasks
├── find_max_deadline()     → timeline size
├── make_empty_schedule()   → create slots
├── sort_tasks()            → sort by profit
├── schedule_tasks()        → greedy logic
├── print_schedule()        → display output
└── show_result()           → final result

## 👨‍💻 Contributions

### 🟦 Sakiya Mason — Initialization & Setup
- Created the `TaskScheduler` class  
- Implemented `__init__` method  
- Stored task list (task_id, deadline, profit)  
- Found maximum deadline  
- Built empty schedule (timeline)  

---

### 🟩 Aadi Kadam — Sorting Logic
- Sorted tasks in descending order of profit  
- Used Python sorting (`sorted()`)  
- Prepared task list for greedy scheduling  

---

### 🟥 Ishan Srivastava — Core Algorithm
- Implemented greedy scheduling logic  
- Assigned tasks to latest valid slots  
- Handled backward slot searching  
- Ensured maximum profit selection  

---

### 🟨 Jared Chapman — Output & Formatting
- Printed initial empty schedule  
- Displayed final scheduled timeline  
- Calculated total profit  
- Formatted output clearly  

---

### 🟪 Sara Doyle — Testing & Debugging
- Created all required test cases  
- Verified correctness of outputs  
- Handled edge cases (e.g., deadline = 0)  
- Debugged and validated results  

---

### 🟧 Becks — Documentation & Integration
- Explained algorithm and approach  
- Combined all parts into final code  
- Prepared README and report  
- Assisted with presentation/video  
