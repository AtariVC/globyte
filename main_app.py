import streamlit as st
import pandas as pd


st.write("""
# My first app
Hello *world!*
""")

# Генерация случайных данных
num_records = 100
data = {
    'RandomNumber1': [1, 2, 3],
    'RandomNumber2': [1, 2, 3]
}

# Создание DataFrame
df = pd.DataFrame(data)

df = pd.read_csv('random_numbers.csv')
st.line_chart(df)
