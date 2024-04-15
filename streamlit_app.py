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

