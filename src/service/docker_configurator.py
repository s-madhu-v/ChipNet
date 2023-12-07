import json
import tkinter as tk
from tkinter import ttk, Label, Entry, Button, Frame

with open('templates.json', 'r') as f:
    templates = json.load(f)

build_frame_colour = "#F3B664"
run_frame_colour = "#F3B664"
orange_colour = "#EE7214"
light_yellow_colour = "#F1EB90"
label_colour = orange_colour
button1_colour = "?"
button2_colour = "?"

# Helper function to add label and entry in grid layout
def add_labeled_entry(container, label_text, row, column=0, padx=(10, 0), pady=5, entry_var=None):
    label = Label(container, text=label_text, bg=label_colour).grid(row=row, column=column, sticky="we", padx=padx, pady=pady)
    entry = Entry(container)
    entry.grid(row=row, column=column+1, sticky="we", padx=(0, 10), pady=pady)
    return entry

def show_docker_configurator(bid_submission_func):
    # Function to populate the UI with the selected template
    def populate_ui(template_name):
        template = templates[template_name]
        build_path_entry.delete(0, tk.END)
        build_path_entry.insert(0, template["path"])
        build_tag_entry.delete(0, tk.END)
        build_tag_entry.insert(0, template["tag"])
        build_args_entry.delete(0, tk.END)
        build_args_entry.insert(0, template["build_args"])
        run_image_entry.delete(0, tk.END)
        run_image_entry.insert(0, template["image"])
        run_command_entry.delete(0, tk.END)
        run_command_entry.insert(0, template["command"])
        run_ports_entry.delete(0, tk.END)
        run_ports_entry.insert(0, template["ports"])
        run_volumes_entry.delete(0, tk.END)
        run_volumes_entry.insert(0, template["volumes"])
        run_environment_entry.delete(0, tk.END)
        run_environment_entry.insert(0, template["environment"])
        run_memory_entry.delete(0, tk.END)
        run_memory_entry.insert(0, template["memory"])
        run_cpus_entry.delete(0, tk.END)
        run_cpus_entry.insert(0, template["cpus"])
        run_cap_add_entry.delete(0, tk.END)
        run_cap_add_entry.insert(0, template["cap_add"])
        run_network_entry.delete(0, tk.END)
        run_network_entry.insert(0, template["network"])
        run_name_entry.delete(0, tk.END)
        run_name_entry.insert(0, template["name"])

    # Create the main window
    docker_configurator_window = tk.Toplevel()
    docker_configurator_window.title("Docker Configurator")
    docker_configurator_window.geometry("600x1000")  # Set the initial size of the window
    docker_configurator_window.configure(bg='#9FBB73')

    # Dropdown for template selection
    template_var = tk.StringVar(docker_configurator_window)
    template_dropdown = ttk.Combobox(docker_configurator_window, textvariable=template_var, values=list(templates.keys()))
    template_dropdown.place(relx=0.05, rely=0.02, relwidth=0.9, height=25)
    template_dropdown.bind('<<ComboboxSelected>>', lambda event: populate_ui(template_var.get()))

    # Define the build frame
    build_frame = Frame(docker_configurator_window, bg=build_frame_colour, bd=2, relief="groove")
    build_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.2)
    build_frame.columnconfigure(1, weight=1)

    # Define the run frame
    run_frame = Frame(docker_configurator_window, bg=run_frame_colour, bd=2, relief="groove")
    run_frame.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.5)
    run_frame.columnconfigure(1, weight=1)

    # Add components to the build frame
    build_path_entry = add_labeled_entry(build_frame, "Path:", 0)
    build_tag_entry = add_labeled_entry(build_frame, "Tag:", 1)
    build_args_entry = add_labeled_entry(build_frame, "Build Arguments for the image:", 2)

    # Add components to the run frame
    run_image_entry = add_labeled_entry(run_frame, "Image:", 0)
    run_command_entry = add_labeled_entry(run_frame, "Command:", 1)
    run_ports_entry = add_labeled_entry(run_frame, "Ports:", 2)
    run_volumes_entry = add_labeled_entry(run_frame, "Volumes:", 3)
    run_environment_entry = add_labeled_entry(run_frame, "Environment:", 4)
    run_memory_entry = add_labeled_entry(run_frame, "Memory:", 5)
    run_cpus_entry = add_labeled_entry(run_frame, "CPUs:", 6)
    run_cap_add_entry = add_labeled_entry(run_frame, "Capabilities (comma-separated):", 7)
    run_network_entry = add_labeled_entry(run_frame, "Network:", 8)
    run_name_entry = add_labeled_entry(run_frame, "Container Name:", 9)

    def output_json_template():
        template = {
            "path": build_path_entry.get(),
            "tag": build_tag_entry.get(),
            "build_args": build_args_entry.get(),
            "image": run_image_entry.get(),
            "command": run_command_entry.get(),
            "ports": run_ports_entry.get(),
            "volumes": run_volumes_entry.get(),
            "environment": run_environment_entry.get(),
            "memory": run_memory_entry.get(),
            "cpus": run_cpus_entry.get(),
            "cap_add": run_cap_add_entry.get(),
            "network": run_network_entry.get(),
            "name": run_name_entry.get()
        }
        json_template = json.dumps(template, indent=4)
        print(json_template)
        return json_template

    def submit_bid():
        current_template = output_json_template()
        print(current_template)
        bid_submission_func(current_template)
        docker_configurator_window.destroy()
        # print("Bid Fake Submitted")

    make_bid_button = Button(docker_configurator_window, text="Submit Bid", command=submit_bid)
    make_bid_button.place(relx=0.05, rely=0.92, relwidth=0.9, height=30)

    # Start the Tkinter loop
    docker_configurator_window.mainloop()










