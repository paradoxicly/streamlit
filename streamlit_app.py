import os
import pandas as pd
import streamlit as st

# Function to list files in current and parent directories
def list_files_in_directories():
    current_dir = os.getcwd()
    all_files = []
    while current_dir:
        for file in os.listdir(current_dir):
            all_files.append({'Directory': current_dir, 'File': file})
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached the root directory
            break
        current_dir = parent_dir
    df = pd.DataFrame(all_files)
    st.write(df)

list_files_in_directories()
