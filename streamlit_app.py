import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import json

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

employee_df = pd.read_csv("data/employees.csv")

st.write(employee_df)

st.divider()  

# Controles de la gráfica
with st.container(horizontal=True, horizontal_alignment="distribute"):
    color = st.color_picker("Elige un color para las barras", "#3475B3")
    show_name = st.toggle("Mostrar el nombre", value=True)
    show_salary = st.toggle("Mostrar sueldo en la barra")


# Gráfico de barras
fig, ax = plt.subplots()
bars = ax.barh(employee_df["full name"], employee_df["salary"], color=color)

if show_name:
    ax.set_yticks(range(len(employee_df["full name"])))
    ax.set_yticklabels(employee_df["full name"])
else:
    ax.set_yticklabels([])

if show_salary:
    for bar, salary in zip(bars, employee_df["salary"]):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f" {salary}€", va="center", ha="left", fontsize=9)

ax.margins(x=0.2)
ax.set_xlim(0, 4500)
ax.tick_params(axis="x", labelrotation=90)

st.pyplot(fig)

st.write("© Álvaro López Guerrero - CPIFP Alan Turing")