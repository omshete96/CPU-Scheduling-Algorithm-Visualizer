#CPU Scheduling Algorithm Visualizer
**Description**
The CPU Scheduling Algorithm Visualizer is a command-line tool designed to help users understand the working of various CPU scheduling algorithms, including:

First-Come-First-Serve (FCFS)
Shortest Job First (SJF)
Priority Scheduling
Round Robin
This tool allows users to input process details and visually understand how processes are scheduled, providing key metrics such as waiting time and turnaround time for each algorithm.

**Features**
🖥️ Simulation of major CPU scheduling algorithms: FCFS, SJF, Priority, and Round Robin.
🕒 Custom input for process burst time, arrival time, and priority (for priority scheduling).
📊 Output includes Gantt Chart representation, average waiting time, and turnaround time for each process.
Installation
To run this project locally, follow these steps:

bash
Copy code
# Clone the repository
git clone https://github.com/omshete96/CPU-Scheduling-Algorithm-Visualizer.git

# Navigate to the project directory
cd CPU-Scheduling-Algorithm-Visualizer

# Compile the code (if using C++ or Java, for example)
g++ -o cpu_scheduler main.cpp

# Run the executable
./cpu_scheduler
Usage
Input Parameters: The tool will prompt you to enter the following details for each process:

Process ID
Arrival Time
Burst Time
Priority (for Priority Scheduling)
Time Quantum (for Round Robin Scheduling)
Algorithm Selection: You can choose from the available algorithms to simulate and visualize CPU scheduling behavior.

Output: The program outputs:

The Gantt chart-like sequence showing the order of process execution.
Average waiting time and turnaround time for the selected scheduling algorithm.
Example
bash
Copy code
Enter the number of processes: 3
Enter process 1 details: (Arrival time, Burst time, Priority)
Enter process 2 details: (Arrival time, Burst time, Priority)
...
Select the scheduling algorithm:
1. FCFS
2. SJF
3. Priority
4. Round Robin

# The output will show the order of execution, Gantt chart, and performance metrics.

**Technologies**
Programming Language: C++ (or Java, Python, etc., depending on your actual implementation)
Concepts: CPU Scheduling, Gantt Charts, Process Management

**Contributing**
Contributions are welcome! Please follow these steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes and commit (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
