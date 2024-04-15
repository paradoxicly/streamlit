import pandas as pd
from pathlib import Path
import streamlit as st

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
