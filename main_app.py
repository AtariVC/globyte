import streamlit as st
import pandas as pd
import random


st.write("""
# My first app
Hello *world!*
""")

# Генерация случайных данных
num_records = 100
data = {
    'RandomNumber1': [random.randint(0, 100) for _ in range(num_records)],
    'RandomNumber2': [random.randint(0, 100) for _ in range(num_records)]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Запись в CSV файл
df.to_csv('random_numbers.csv', index=False)

df = pd.read_csv('random_numbers.csv')
st.line_chart(df)
