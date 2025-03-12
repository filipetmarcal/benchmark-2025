import time
import platform
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import psutil
import os
import cv2
import multiprocessing

def benchmark_cpu():
    result_label.config(text="Running benchmark...", foreground="blue")
    root.update_idletasks()
    start_time = time.time()
    total_operations = 10**7
    result = 0
    for i in range(total_operations):
        result += (i ** 2) % 1234567
    end_time = time.time()
    elapsed_time = end_time - start_time
    score_cpu = int((total_operations / elapsed_time) / 1000)
    return score_cpu, elapsed_time

def benchmark_ram():
    size = 100 * 1024 * 1024
    data = bytearray(size)
    start_time = time.time()
    for _ in range(5):
        data[:size//2] = b'1' * (size // 2)
        _ = data[:size//2]
    end_time = time.time()
    score_ram = int(size / (end_time - start_time) / 1024 / 1024)
    return score_ram

def benchmark_storage():
    filename = "benchmark_test.tmp"
    size = 100 * 1024 * 1024
    data = os.urandom(size)
    start_time = time.time()
    with open(filename, "wb") as f:
        f.write(data)
    write_time = time.time() - start_time
    start_time = time.time()
    with open(filename, "rb") as f:
        _ = f.read()
    read_time = time.time() - start_time
    os.remove(filename)
    score_storage = int(size / ((write_time + read_time) / 2) / 1024 / 1024)
    return score_storage

def benchmark_gpu():
    size = 1280
    num_frames = 100
    start_time = time.time()
    for _ in range(num_frames):
        img = np.random.randint(0, 255, (size, size, 3), dtype=np.uint8)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        img = cv2.Canny(img, 100, 200)
    end_time = time.time()
    elapsed_time = end_time - start_time
    fps = int(num_frames / elapsed_time)
    return fps

def evaluate_performance(score):
    if score < 500:
        return "🔴 Low performance. Suitable only for basic tasks.", "red"
    elif score < 2000:
        return "🟡 Medium performance. Good for office work and light gaming.", "orange"
    elif score < 5000:
        return "🟢 Good performance. Supports modern games and video editing.", "green"
    else:
        return "🔥 High performance! Ideal for AAA games and heavy tasks.", "darkgreen"

def run_benchmark():
    cpu_score, cpu_time = benchmark_cpu()
    ram_score = benchmark_ram()
    storage_score = benchmark_storage()
    gpu_fps = benchmark_gpu()
    feedback_text, color = evaluate_performance(cpu_score)
    result_label.config(text=f"⏱️ CPU: {cpu_score} | ⏳ {cpu_time:.2f}s", foreground="black")
    feedback_label.config(text=feedback_text, foreground=color)
    ram_label.config(text=f"💾 RAM: {ram_score} MB/s")
    storage_label.config(text=f"🖴 Storage: {storage_score} MB/s")
    gpu_label.config(text=f"🎮 GPU: {gpu_fps} FPS (simulating a simple game at 1280x720)")
    update_chart(cpu_score)

def update_chart(score):
    ax.clear()
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.spines['polar'].set_visible(False)
    ax.grid(False)
    zones = [500, 2000, 5000, 8000]
    colors = ['red', 'orange', 'green', 'darkgreen']
    for i in range(len(zones)):
        ax.barh(1, np.pi/4, left=np.pi/2 - (i+1)*np.pi/4, color=colors[i], alpha=0.6)
    max_value = 8000
    angle = (score / max_value) * (np.pi)
    ax.arrow(np.pi/2 - angle, 1, 0, -0.5, width=0.08, head_width=0.2, head_length=0.2, fc='black', ec='black')
    canvas.draw()

root = tk.Tk()
root.title("PC Benchmark")
root.geometry("500x600")

# Set icon
system = platform.system()
cpu_info = platform.processor()
mem_info = round(psutil.virtual_memory().total / (1024 ** 3), 1)
info_label = tk.Label(root, text=f"System: {system}\nProcessor: {cpu_info if cpu_info else 'Unknown'}\nTotal RAM: {mem_info} GB", font=("Arial", 10))
info_label.pack(pady=10)
btn_test = ttk.Button(root, text="Run Benchmark", command=run_benchmark)
btn_test.pack(pady=5)
result_label = tk.Label(root, text="Click the button to test.", font=("Arial", 10))
result_label.pack(pady=5)
feedback_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
feedback_label.pack(pady=5)
ram_label = tk.Label(root, text="💾 RAM: --- MB/s", font=("Arial", 10))
ram_label.pack(pady=5)
storage_label = tk.Label(root, text="🖴 Storage: --- MB/s", font=("Arial", 10))
storage_label.pack(pady=5)
gpu_label = tk.Label(root, text="🎮 GPU: --- FPS", font=("Arial", 10))
gpu_label.pack(pady=5)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(4, 2.5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=5)
update_chart(0)
root.mainloop()
