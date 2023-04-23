import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["brownie", "cytoolz", "multiaddr", "black", "eth_hash"],
    # "packages": ["tkinter"],
    "excludes": [],
    "include_files": ["/Users/imadhui/Documents/GitHub/ChipNet/brownie-config.yml"],
    "zip_include_packages": [],
}

setup(
    name="ChipNet",
    version="1.0",
    description="A Platform for trading computational power",
    options={"build_exe": build_exe_options},
    executables=[Executable("start.py", base=None)],
)
