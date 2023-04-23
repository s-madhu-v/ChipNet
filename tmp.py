import tkinter as tk

# Define the function to be called when the button is clicked
def button_click():
    # Get the value entered in the Entry widget
    value = entry.get()

    # Do something with the value, e.g. print it to the console
    print(value)

# Create a new window
window = tk.Tk()

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button and bind it to the button_click function
button = tk.Button(window, text="Click me", command=button_click)
button.pack()

# Run the main event loop
window.mainloop()

