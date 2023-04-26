import tkinter as tk

root = tk.Tk()

selected_option = tk.StringVar(root)

options = ["Option 1", "Option 2", "Option 3"]

selected_option.set(options[0])


def button_click():
    selected_value = selected_option.get()
    target_function(selected_value)


def target_function(selected_value):
    print(f"The selected value is: {selected_value}")

button = tk.Button(root, text="Click me", command=button_click)
button.pack()
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack()

root.mainloop()