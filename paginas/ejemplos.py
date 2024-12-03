import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

st.title('Explora la Probabilidad: Ejemplos que Ilustran Conceptos Clave')

# ejemplo 1

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


# ejemplo 2
st.header("Probabilidad: Hombre o Ojos Castaños")
st.write("""
    En este ejemplo, tenemos un grupo de  hombres y  mujeres.
    La mitad del numero de hombres y tres cuartos del numero de mujeres tienen los ojos castaños.
    Queremos calcular la probabilidad de que una persona elegida al azar sea un hombre o tenga los ojos castaños.
    """)


hombres = st.number_input("Número de hombres", min_value=1, max_value=100)
mujeres = st.number_input("Número de mujeres", min_value=1, max_value=100)
hombres_ojos_castanos = hombres/2
mujeres_ojos_castanos = 3*mujeres/4


total_personas = hombres + mujeres
total_ojos_castanos = hombres_ojos_castanos + mujeres_ojos_castanos


P_hombre = hombres / total_personas
P_ojos_castanos = total_ojos_castanos / total_personas
P_hombre_y_ojos_castanos = hombres_ojos_castanos / total_personas


P_union = P_hombre + P_ojos_castanos - P_hombre_y_ojos_castanos

st.write(f"Total de personas: {total_personas}")
st.write(f"Total de personas con ojos castaños: {total_ojos_castanos}")
st.write(f"Probabilidad de que sea hombre: {P_hombre:.2f}")
st.write(f"Probabilidad de que tenga ojos castaños: {P_ojos_castanos:.2f}")
st.write(f"Probabilidad de que sea hombre y tenga ojos castaños: {P_hombre_y_ojos_castanos:.2f}")
st.write(f"Probabilidad de que sea hombre o tenga ojos castaños: {P_union:.2f}")


with st.container(border=True):
    labels = ['Hombres', 'Mujeres', 'Ojos Castaños']
    sizes = [hombres, mujeres, total_ojos_castanos]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    st.pyplot(plt)



# ejemplo 3
st.header("¿Es Pares y Nones un Juego Justo? Descúbrelo con la Probabilidad")
st.markdown("""
La probabilidad puede ser una herramienta útil para analizar juegos como *Pares y Nones*. 
Aunque parece un juego justo, ¡no lo es! Aquí exploraremos por qué.
""")

st.subheader("Tabla de resultados")
st.markdown("""
En este juego, cada jugador saca un número de dedos (1 a 5). La tabla de resultados muestra las posibles sumas y resalta en amarillo los números pares.
""")
st.image('https://www.smartick.es/blog/wp-content/uploads/Imagen2-3.png',width=450)


def generate_results_table():
    resultados = []
    for jugador1 in range(6):
        for jugador2 in range(6):
            suma = jugador1 + jugador2
            resultados.append({"Jugador 1": jugador1, "Jugador 2": jugador2, "Suma": suma, "Paridad": "Par" if suma % 2 == 0 else "Impar"})
    return pd.DataFrame(resultados)

tabla_resultados = generate_results_table()


st.subheader("Probabilidades del juego")
pares = len(tabla_resultados[tabla_resultados["Paridad"] == "Par"])
total = len(tabla_resultados)
prob_par = pares / total
prob_impar = 1 - prob_par

st.markdown(f"""
- Probabilidad de que salga **par**: 0,52
- Probabilidad de que salga **impar**: 0,48
""")


st.subheader("Simulación del juego")
st.markdown("Juega con un amigo e ingresa tus elecciones para ver el resultado.")

jugador1 = st.number_input("Dedos jugador 1 (1-5):", min_value=1, max_value=5, step=1)
jugador2 = st.number_input("Dedos jugador 2 (1-5):", min_value=1, max_value=5, step=1)

if st.button("Calcular resultado"):
    suma = jugador1 + jugador2
    paridad = "Par" if suma % 2 == 0 else "Impar"
    st.markdown(f"La suma de los dedos es `{suma}`, que es **{paridad}**.")
    if paridad == "Par":
        st.success("¡Gana quien eligió Par!")
    else:
        st.warning("¡Gana quien eligió Impar!")









