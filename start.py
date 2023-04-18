import sys
import os
import subprocess
from scripts.gui.gui import main

# Construct the path to the data file
data_path = os.path.join(sys._MEIPASS, 'brownie')

print(f"\n\nData path: {data_path}\n\n")

# Run a command and capture its output
output = subprocess.check_output([data_path, 'run'])

# Print the output
print(output)
