import json
import shlex
import subprocess

def generate_docker_build_command(template):
    template = json.loads(template)
    path = template["path"]
    tag = template["tag"]
    build_args = template["build_args"]
    cmd = f"docker build {path}"
    if tag:
        cmd += f" -t {tag}"
    if build_args:
        for build_arg in build_args.split(','):
            cmd += f" --build-arg {build_arg}"
    return cmd

def generate_docker_run_command(template):
    template = json.loads(template)
    image = template["image"]
    command = template["command"]
    ports = template["ports"]
    volumes = template["volumes"]
    environment = template["environment"]
    memory = template["memory"]
    cpus = template["cpus"]
    cap_add =  template["cap_add"]
    network = template["network"]
    name = template["name"]
    cmd = "docker run"
    # if interactive:
        # cmd += " -i"
    # if tty:
        # cmd += " -t"
    if cap_add:
        for cap in cap_add:
            cmd += f" --cap-add={cap}"
    if volumes != ['']:
        for volume in volumes:
            cmd += f" -v {volume}"
    if network:
        cmd += f" --network {network}"
    if name:
        cmd += f" --name {name}"
    if ports != ['']:
        print(f"The ports are {ports}")
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

def execute_bash_command(command):
    # Split the command string into a list of arguments
    split_command = shlex.split(command)

    # Run the command using subprocess
    try:
        result = subprocess.run(
            split_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        # Print the command's output
        print("Command Output:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Handle any errors that may occur
        print("Error executing command:")
        print(e.stderr)

def execute_docker_template(template):
    # Define the Docker command as a single string
    docker_build_command = generate_docker_build_command(template)
    docker_run_command = generate_docker_run_command(template)

    # Split the command string into a list of arguments
    # split_docker_build_command = shlex.split(docker_build_command)
    # split_docker_run_command = shlex.split(docker_run_command)
    print("Executing the build command:")
    execute_bash_command(docker_build_command)
    print("Executing the run command:")
    execute_bash_command(docker_run_command)
    print("Docker template executed!")
