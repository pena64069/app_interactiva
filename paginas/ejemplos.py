import streamlit as st

st.title('Explora la Probabilidad: Ejemplos que Ilustran Conceptos Clave')

import random
import streamlit as st
st.header('Ruleta de Probabilidad')

intentos = st.slider("¿Cuántas veces quieres girar la ruleta?", 10, 1000, 100)

with st.container(border=True):
    c1, c2 = st.columns(2, vertical_alignment="center")
    with c1:
        st.image('https://play-lh.googleusercontent.com/ffamZbyiKd8_lHlNCebq1f8GziHWOWR3NUVUDsp1ji-lrbD20VaaK2UMZZvrPqOIGNZD', width=500)
    with c2:
        def girar_ruleta():
            colores = ["Rojo", "Verde", "Azul", "Amarillo", "Morado", "Naranja"]
            return random.choice(colores)

        colores = ["Rojo", "Verde", "Azul", "Amarillo", "Morado", "Naranja"]
        frecuencia_colores = {color: 0 for color in colores}

        for _ in range(intentos):
            resultado = girar_ruleta()
            frecuencia_colores[resultado] += 1

        for color in colores:
            probabilidad_estimacion = frecuencia_colores[color] / intentos
            st.write(f"El color {color} salió {frecuencia_colores[color]} veces.")
            st.write(f"Probabilidad estimada de {color}: {probabilidad_estimacion:.4f}")


# Título y descripción de la página
st.header("Probabilidad: Hombre o Ojos Castaños")
st.write("""
    En este ejemplo, tenemos un grupo de  hombres y  mujeres.
    La mitad del numero de hombres y tres cuartos del numero de mujeres tienen los ojos castaños.
    Queremos calcular la probabilidad de que una persona elegida al azar sea un hombre o tenga los ojos castaños.
    """)

# Entrada de datos interactiva para los números
hombres = st.number_input("Número de hombres", min_value=1, max_value=100)
mujeres = st.number_input("Número de mujeres", min_value=1, max_value=100)
hombres_ojos_castanos = hombres/2
mujeres_ojos_castanos = 3*mujeres/4

# Cálculo de la probabilidad
total_personas = hombres + mujeres
total_ojos_castanos = hombres_ojos_castanos + mujeres_ojos_castanos

# Probabilidades
P_hombre = hombres / total_personas
P_ojos_castanos = total_ojos_castanos / total_personas
P_hombre_y_ojos_castanos = hombres_ojos_castanos / total_personas

# Fórmula de la probabilidad de la unión
P_union = P_hombre + P_ojos_castanos - P_hombre_y_ojos_castanos

# Mostrar resultados
st.write(f"Total de personas: {total_personas}")
st.write(f"Total de personas con ojos castaños: {total_ojos_castanos}")
st.write(f"Probabilidad de que sea hombre: {P_hombre:.2f}")
st.write(f"Probabilidad de que tenga ojos castaños: {P_ojos_castanos:.2f}")
st.write(f"Probabilidad de que sea hombre y tenga ojos castaños: {P_hombre_y_ojos_castanos:.2f}")
st.write(f"Probabilidad de que sea hombre o tenga ojos castaños: {P_union:.2f}")

# Gráfico opcional (si deseas agregar algo visual)
import matplotlib.pyplot as plt

labels = ['Hombres', 'Mujeres', 'Ojos Castaños']
sizes = [hombres, mujeres, total_ojos_castanos]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
st.pyplot(plt)






