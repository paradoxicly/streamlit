import pandas as pd
from pathlib import Path
import streamlit as st

import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception as e:
        IP = e
    finally:
        s.close()
    return IP


st.write(get_ip_address())

# Specify the directory
dir_path = Path('/home/adminuser/venv/lib/python3.11/site-packages/')

# Get a list of all files in the directory
files = [file.name for file in dir_path.iterdir() if file.is_file()]

# Display the list of files
st.write(files)

code = st.text_input('Enter some Python code')

# Execute the code
if code:
    try:
        exec(code)
    except Exception as e:
        st.write(f"Error: {e}")

def list_files_in_directories():
    cwd = Path.cwd()
    directories = [cwd] + list(cwd.parents)
    for directory in directories:
        files = [f.name for f in directory.iterdir() if f.is_file()]
        df = pd.DataFrame(files, columns=['Files'])
        st.write(f'Files in {directory}:', df)

list_files_in_directories()

import sys

st.write(sys.executable)

import streamlit as st
import pandas as pd

st.write(st.__file__, pd.__file__)

import traceback

st.write(traceback.format_stack())

import os

container_id = os.getenv('HOSTNAME')
st.write(container_id)

