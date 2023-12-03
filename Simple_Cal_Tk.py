import tkinter as tk
import math
# window = tk() 
def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Task2_Calculator")

root.configure(bg='#000000')

#border_color = Frame(window, background="#8B0A50")


entry = tk.Entry(root, width=19, font=('Arial', 14), borderwidth=5, relief="solid", bg='#ffffff')
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', '==', '/'
]

row_val = 1
col_val = 0

button_styles = {
    'bg': '#8B0A50', 
    'fg': '#FFFFFF', 
    'font': ('Arial', 12, 'bold'),
    'width': 5,
    'height': 2,
}

for button in buttons:
    tk.Button(root, text=button, command=lambda b=button: on_click(b), **button_styles).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='√', command=calculate_sqrt, **button_styles).grid(row=row_val, column=col_val + 3)

tk.Button(root, text='C', command=clear_entry, **button_styles).grid(row=row_val, column=col_val)

tk.Button(root, text='CE', command=clear_entry, **button_styles).grid(row=row_val, column=col_val + 1)

tk.Button(root, text='=', command=calculate, **button_styles).grid(row=row_val, column=col_val + 2)

root.mainloop()
