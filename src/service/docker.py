import tkinter as tk
from tkinter import StringVar, Entry, Label, Button, Frame

def build_docker_build_command(path, tag=None, build_args=None):
    # Dummy function to emulate build command creation
    cmd = f"docker build {path}"
    if tag:
        cmd += f" -t {tag}"
    if build_args:
        cmd += f" --build-arg {build_args}"
    return cmd

def build_docker_run_command(image, command=None, volumes=None, ports=None, environment=None, memory=None, cpus=None, interactive=False, tty=False, cap_add=None, network=None, name=None):
    cmd = "docker run"

    if interactive:
        cmd += " -i"
    if tty:
        cmd += " -t"
    if cap_add:
        for cap in cap_add:
            cmd += f" --cap-add={cap}"
    if volumes:
        for volume in volumes:
            cmd += f" -v {volume}"
    if network:
        cmd += f" --network {network}"
    if name:
        cmd += f" --name {name}"
    if ports:
        for port in ports:
            cmd += f" -p {port}"
    if environment:
        for key, value in environment.items():
            cmd += f" -e {key}={value}"
    if memory:
        cmd += f" --memory {memory}"
    if cpus:
        cmd += f" --cpus {cpus}"
    cmd += f" {image}"
    if command:
        cmd += f" {command}"

    return cmd

# Create the main window
root = tk.Tk()
root.title("Docker Dashboard")
root.configure(bg='#527853')
root.geometry("500x1000")  # Consider increasing the size if necessary

build_frame_colour = "#F7B787"
run_frame_colour = "#F7B787"
orange_colour = "#EE7214"
label1_colour = orange_colour
label2_colour = orange_colour
label3_colour = orange_colour
label4_colour = orange_colour
button1_colour = "?"

label5_colour = orange_colour
label6_colour = orange_colour
label7_colour = orange_colour
label8_colour = orange_colour
label9_colour = orange_colour
label10_colour = orange_colour
label11_colour = orange_colour
label12_colour = orange_colour
label13_colour = orange_colour
label14_colour = orange_colour
label15_colour = orange_colour
button2_colour = "?"

# Define the build frame
build_frame = Frame(root, bg=build_frame_colour, bd=2, relief="groove")
build_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

# Define the run frame
run_frame = Frame(root, bg=run_frame_colour, bd=2, relief="groove")
run_frame.place(relx=0.05, rely=0.39, relwidth=0.9, relheight=0.6)

# Add components to the build frame
Label(build_frame, text="Build Docker Image", bg=label1_colour).pack(fill='x', pady=5)
Label(build_frame, text="Path:", bg=label2_colour).pack(anchor='w')
build_path_entry = Entry(build_frame)
build_path_entry.pack(fill='x', padx=10, pady=2)
Label(build_frame, text="Tag:", bg=label3_colour).pack(anchor='w')
build_tag_entry = Entry(build_frame)
build_tag_entry.pack(fill='x', padx=10, pady=2)
Label(build_frame, text="Build Args:", bg=label4_colour).pack(anchor='w')
build_args_entry = Entry(build_frame)
build_args_entry.pack(fill='x', padx=10, pady=2)
build_button = Button(build_frame, text="Generate Build Command", command=lambda: print(build_docker_build_command(build_path_entry.get(), build_tag_entry.get(), build_args_entry.get())))
build_button.pack(pady=5)

# Add components to the run frame
Label(run_frame, text="Run Docker Container", bg=label5_colour).pack(fill='x', pady=5)
Label(run_frame, text="Image:", bg=label6_colour).pack(anchor='w')
run_image_entry = Entry(run_frame)
run_image_entry.pack(fill='x', padx=10, pady=2)
Label(run_frame, text="Command:", bg=label7_colour).pack(anchor='w')
run_command_entry = Entry(run_frame)
run_command_entry.pack(fill='x', padx=10, pady=2)
Label(run_frame, text="Ports:", bg=label8_colour).pack(anchor='w')
run_ports_entry = Entry(run_frame)
run_ports_entry.pack(fill='x', padx=10, pady=2)
Label(run_frame, text="Volumes:", bg=label9_colour).pack(anchor='w')
run_volumes_entry = Entry(run_frame)
run_volumes_entry.pack(fill='x', padx=10, pady=2)
Label(run_frame, text="Environment:", bg=label10_colour).pack(anchor='w')
run_environment_entry = Entry(run_frame)
run_environment_entry.pack(fill='x', padx=10, pady=2)
Label(run_frame, text="Memory:", bg=label11_colour).pack(anchor='w')
run_memory_entry = Entry(run_frame)
run_memory_entry.pack(fill='x', padx=10, pady=2)
Label(run_frame, text="CPUs:", bg=label12_colour).pack(anchor='w')
run_cpus_entry = Entry(run_frame)
run_cpus_entry.pack(fill='x', padx=10, pady=2)

# Add fields for capabilities, network, and container name
Label(run_frame, text="Capabilities (comma-separated, e.g., NET_ADMIN,SYS_MODULE):", bg=label13_colour).pack(anchor='w')
run_cap_add_entry = Entry(run_frame)
run_cap_add_entry.pack(fill='x', padx=10, pady=2)

Label(run_frame, text="Network:", bg=label14_colour).pack(anchor='w')
run_network_entry = Entry(run_frame)
run_network_entry.pack(fill='x', padx=10, pady=2)

Label(run_frame, text="Container Name:", bg=label15_colour).pack(anchor='w')
run_name_entry = Entry(run_frame)
run_name_entry.pack(fill='x', padx=10, pady=2)

# Update the button command to include the new fields
run_button = Button(run_frame, text="Generate Run Command", command=lambda: print(build_docker_run_command(
    run_image_entry.get(),
    run_command_entry.get(),
    run_ports_entry.get().split(','),  # Splitting string input into list
    run_volumes_entry.get().split(','),
    # Convert comma-separated key=value to dictionary
    dict(env.split('=') for env in run_environment_entry.get().split(',')) if run_environment_entry.get() else {},
    run_memory_entry.get(),
    run_cpus_entry.get(),
    interactive=True,  # Assuming you always want interactive mode
    tty=True,  # Assuming you always want TTY
    cap_add=run_cap_add_entry.get().split(',') if run_cap_add_entry.get() else [],
    network=run_network_entry.get(),
    name=run_name_entry.get()
)))
run_button.pack(pady=5)

# Start the Tkinter loop
root.mainloop()