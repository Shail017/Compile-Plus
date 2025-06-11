import tkinter as tk
from tkinter import filedialog
import subprocess
import time

def compile_c():
    ts1 = time.time()
    # Get the C file path from the user
    c_file_path = filedialog.askopenfilename(title="Select C File", filetypes=[("C Files", "*.c")])

    # Compile the C file
    subprocess.call(["gcc", c_file_path, "-o", "c_output"])
    ts2 = time.time()
    timediff = t2 - t1
    print(timediff)

def compile_python():
    # Get the Python file path from the user
    python_file_path = filedialog.askopenfilename(title="Select Python File", filetypes=[("Python Files", "*.py")])

    # Compile the Python file
    subprocess.call(["python", python_file_path])

def compile_javascript():
    # Get the JavaScript file path from the user
    javascript_file_path = filedialog.askopenfilename(title="Select JavaScript File", filetypes=[("JavaScript Files", "*.js")])

    # Compile the JavaScript file
    subprocess.call(["node", javascript_file_path])

# Create the main window
root = tk.Tk()
root.title("Desktop Application to Compile C, Python, and JavaScript")

# Create the buttons
c_button = tk.Button(root, text="Compile C", command=compile_c)
python_button = tk.Button(root, text="Compile Python", command=compile_python)
javascript_button = tk.Button(root, text="Compile JavaScript", command=compile_javascript)

# Add the buttons to the window
c_button.pack()
python_button.pack()
javascript_button.pack()

# Run the main loop
root.mainloop()