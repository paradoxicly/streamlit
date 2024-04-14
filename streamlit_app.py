import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Generate a range of values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')
plt.title('Sine and Cosine from 0 to 2π')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Display the plot in Streamlit
st.pyplot(plt)
