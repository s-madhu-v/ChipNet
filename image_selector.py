import tkinter as tk
from tkinter import StringVar, OptionMenu, Label, Entry, Scale

def update_options(*args):
    selection = primary_option.get()
    # Clear the previous widgets in the frame
    for widget in frame.winfo_children():
        widget.destroy()

    if selection == "Option 1":
        # Add multiple widgets for Option 1
        Label(frame, text="Setting 1A:").pack()
        Entry(frame).pack()
        Label(frame, text="Setting 1B:").pack()
        Scale(frame, from_=0, to=50).pack()
        Label(frame, text="Setting 1C:").pack()
        tk.Checkbutton(frame, text="Enable 1C").pack()

    elif selection == "Option 2":
        # Add multiple widgets for Option 2
        Label(frame, text="Setting 2A:").pack()
        tk.Spinbox(frame, from_=0, to=10).pack()
        Label(frame, text="Setting 2B:").pack()
        tk.Text(frame, height=2, width=20).pack()
        Label(frame, text="Setting 2C:").pack()
        secondary_option_2 = StringVar(frame)
        secondary_options_2 = ["Suboption 2A", "Suboption 2B"]
        secondary_option_2.set(secondary_options_2[0])
        OptionMenu(frame, secondary_option_2, *secondary_options_2).pack()

    elif selection == "Option 3":
        # Add multiple widgets for Option 3
        Label(frame, text="Setting 3A:").pack()
        tk.Radiobutton(frame, text="Choice 1", value=1).pack()
        tk.Radiobutton(frame, text="Choice 2", value=2).pack()
        Label(frame, text="Setting 3B:").pack()
        tk.Listbox(frame, height=2).pack()
        Label(frame, text="Setting 3C:").pack()
        tk.Button(frame, text="Button 3C").pack()

root = tk.Tk()
root.title("Dynamic Configuration Options")
root.minsize(width=500, height=300)


primary_option = StringVar(root)
primary_options = ["Option 1", "Option 2", "Option 3"]
primary_option.set(primary_options[0])
primary_option.trace("w", update_options)

primary_dropdown = OptionMenu(root, primary_option, *primary_options)
primary_dropdown.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

root.mainloop()
