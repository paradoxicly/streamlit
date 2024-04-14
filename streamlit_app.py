import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Create a sidebar slider for the amplitude of the sine wave
amplitude = st.slider('Amplitude of Sine', 0.1, 5.0, 1.0)

# Generate a range of values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine and cosine values with the given amplitude for sine
y_sin = np.sin(x) * amplitude
y_cos = np.cos(x) # The amplitude of cosine is fixed at 1

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label=f'Sine with amplitude {amplitude}')
plt.plot(x, y_cos, label='Cosine with fixed amplitude 1')
plt.title('Sine and Cosine from 0 to 2\u03c0 with Variable Amplitude for Sine')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Display the plot in Streamlit
st.pyplot(plt)
