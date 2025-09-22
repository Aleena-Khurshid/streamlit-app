import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Graphs & Charts in Streamlit")

# Create sample data
np.random.seed(42)
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": np.random.randint(10, 100, 4)
})

st.subheader("1. Bar Chart (Streamlit built-in)")
st.bar_chart(data.set_index("Category"))

st.subheader("2. Line Chart (Streamlit built-in)")
line_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Line 1', 'Line 2', 'Line 3']
)
st.line_chart(line_data)

st.subheader("3. Area Chart (Streamlit built-in)")
st.area_chart(line_data)

# Matplotlib example
st.subheader("4. Pie Chart (Matplotlib)")
fig, ax = plt.subplots()
ax.pie(data["Values"], labels=data["Category"], autopct="%1.1f%%")
ax.set_title("Pie Chart Example")
st.pyplot(fig)

st.subheader("5. Interactive Controls")
if st.checkbox("Show Raw Data"):
    st.write(data)
