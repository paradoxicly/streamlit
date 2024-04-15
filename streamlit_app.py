import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Create sidebar sliders for the amplitude of the sine and cosine waves
amplitude_sine = st.slider('Amplitude of Sine', 0.1, 5.0, 1.0)
amplitude_cosine = st.slider('Amplitude of Cosine', 0.1, 5.0, 1.0)

# Generate a range of values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine and cosine values with the given amplitudes
y_sin = np.sin(x) * amplitude_sine
y_cos = np.cos(x) * amplitude_cosine

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label=f'Sine with amplitude {amplitude_sine}')
plt.plot(x, y_cos, label=f'Cosine with amplitude {amplitude_cosine}')
plt.title('Sine and Cosine from 0 to 2\u03c0 with Variable Amplitudes')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Display the plot in Streamlit
st.pyplot(plt)
