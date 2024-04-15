from pathlib import Path
import streamlit as st

for path in Path('.').iterdir():
    st.write(path.name)
  
