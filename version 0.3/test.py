import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello, world!", font=("TkDefaultFont", 20))
label.pack(fill='x', padx=10, pady=10)

root.mainloop()