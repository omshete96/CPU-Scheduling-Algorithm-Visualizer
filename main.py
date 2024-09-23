import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate and visualize FCFS scheduling
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    start_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    
    for p in processes:
        pid, arrival, burst = p
        start_time = max(start_time, arrival)
        gantt_chart.append((pid, start_time, start_time + burst))
        waiting_times.append(start_time - arrival)
        start_time += burst
        turnaround_times.append(start_time - arrival)
    
    return gantt_chart, np.mean(waiting_times), np.mean(turnaround_times)

# Function to calculate and visualize SJF scheduling
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time and burst time
    start_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    
    while processes:
        # Get all processes that have arrived
        available = [p for p in processes if p[1] <= start_time]
        if available:
            # Pick the process with the shortest burst time
            p = min(available, key=lambda x: x[2])
            processes.remove(p)
            pid, arrival, burst = p
            start_time = max(start_time, arrival)
            gantt_chart.append((pid, start_time, start_time + burst))
            waiting_times.append(start_time - arrival)
            start_time += burst
            turnaround_times.append(start_time - arrival)
        else:
            start_time += 1
    
    return gantt_chart, np.mean(waiting_times), np.mean(turnaround_times)

# Function to calculate and visualize Round Robin scheduling
def round_robin_scheduling(processes, quantum):
    queue = processes[:]
    start_time = 0
    gantt_chart = []
    waiting_times = {p[0]: 0 for p in processes}
    turnaround_times = {p[0]: 0 for p in processes}
    remaining_burst = {p[0]: p[2] for p in processes}
    last_execution_time = {p[0]: 0 for p in processes}
    n = len(processes)
    
    while queue:
        pid, arrival, burst = queue.pop(0)
        if start_time < arrival:
            start_time = arrival
        if remaining_burst[pid] > 0:
            # Calculate the waiting time since the last execution
            waiting_times[pid] += start_time - last_execution_time[pid]
            if remaining_burst[pid] > quantum:
                gantt_chart.append((pid, start_time, start_time + quantum))
                start_time += quantum
                remaining_burst[pid] -= quantum
                queue.append((pid, arrival, burst))
            else:
                gantt_chart.append((pid, start_time, start_time + remaining_burst[pid]))
                start_time += remaining_burst[pid]
                remaining_burst[pid] = 0
                turnaround_times[pid] = start_time - arrival
            last_execution_time[pid] = start_time

    avg_waiting_time = sum(waiting_times.values()) / n
    avg_turnaround_time = sum(turnaround_times.values()) / n
    
    return gantt_chart, avg_waiting_time, avg_turnaround_time

# Function to visualize the Gantt chart using Matplotlib
def visualize_gantt(gantt_chart, title):
    fig, gnt = plt.subplots()
    gnt.set_title(title)
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')
    gnt.set_ylim(0, 10)
    gnt.set_xlim(0, max([end for _, _, end in gantt_chart]) + 1)
    gnt.set_yticks([5])
    gnt.set_yticklabels(['CPU'])
    gnt.grid(True)

    for i, (pid, start, end) in enumerate(gantt_chart):
        gnt.broken_barh([(start, end - start)], (4, 2), facecolors=('tab:blue'))
        gnt.text((start + end) / 2, 5, f'P{pid}', va='center', ha='center', color='white')

    plt.show()

# Main GUI function
def main_gui():
    def schedule():
        processes = []
        try:
            n = int(num_processes_entry.get())
            quantum = int(quantum_entry.get())
            for i in range(n):
                pid = i + 1
                arrival = int(entries[i][0].get())
                burst = int(entries[i][1].get())
                processes.append((pid, arrival, burst))
            
            if algorithm_var.get() == 'FCFS':
                gantt_chart, avg_wt, avg_tt = fcfs_scheduling(processes)
                visualize_gantt(gantt_chart, "FCFS Scheduling")
            elif algorithm_var.get() == 'SJF':
                gantt_chart, avg_wt, avg_tt = sjf_scheduling(processes)
                visualize_gantt(gantt_chart, "SJF Scheduling")
            elif algorithm_var.get() == 'Round Robin':
                gantt_chart, avg_wt, avg_tt = round_robin_scheduling(processes, quantum)
                visualize_gantt(gantt_chart, "Round Robin Scheduling")
            
            result_label.config(text=f"Average Waiting Time: {avg_wt:.2f}\nAverage Turnaround Time: {avg_tt:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for all fields.")

    window = tk.Tk()
    window.title("CPU Scheduling Algorithm Visualizer")
    window.geometry("600x400")

    tk.Label(window, text="Number of Processes:").grid(row=0, column=0, padx=10, pady=10)
    num_processes_entry = tk.Entry(window)
    num_processes_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="Quantum (for RR):").grid(row=1, column=0, padx=10, pady=10)
    quantum_entry = tk.Entry(window)
    quantum_entry.grid(row=1, column=1, padx=10, pady=10)
    quantum_entry.insert(0, "2")  # Default value for quantum

    tk.Label(window, text="Algorithm:").grid(row=2, column=0, padx=10, pady=10)
    algorithm_var = tk.StringVar()
    algorithm_var.set("FCFS")
    algorithm_menu = tk.OptionMenu(window, algorithm_var, "FCFS", "SJF", "Round Robin")
    algorithm_menu.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(window, text="Process Table").grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    tk.Label(window, text="Arrival Time").grid(row=4, column=0, padx=10, pady=10)
    tk.Label(window, text="Burst Time").grid(row=4, column=1, padx=10, pady=10)

    entries = []
    for i in range(5):  # Assume a maximum of 5 processes for simplicity
        arrival_entry = tk.Entry(window)
        burst_entry = tk.Entry(window)
        arrival_entry.grid(row=5+i, column=0, padx=10, pady=5)
        burst_entry.grid(row=5+i, column=1, padx=10, pady=5)
        entries.append((arrival_entry, burst_entry))

    schedule_button = tk.Button(window, text="Schedule", command=schedule)
    schedule_button.grid(row=10, column=0, columnspan=2, padx=10, pady=20)

    result_label = tk.Label(window, text="")
    result_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main_gui()
