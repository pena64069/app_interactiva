import streamlit as st
import random

# Título de la aplicación
st.title("Desafíos de Probabilidad: ¡Diviértete Aprendiendo! 🎮🕹️👾")



# Título de la aplicación
st.header("Ejercicio de Probabilidad: Lanzamiento de dos monedas 🥮")
with st.container(border=True):
    c1, c2 = st.columns(2, vertical_alignment="center")
    with c1:
        # Descripción del problema
        st.subheader("Descripción del problema:")
        st.write("""
        Se lanzan dos monedas al aire. Los posibles resultados son:
        1. Cara
        2. Cruz
        
        Las posibles combinaciones al lanzar dos monedas son:
        - Cara y Cara
        - Cara y Cruz
        - Cruz y Cara
        - Cruz y Cruz
        """)
    with c2:
        st.image('https://cdn.pixabay.com/photo/2020/12/11/09/05/coin-flipping-5822271_640.png', width=220)
# Ejercicio A: Probabilidad de que salga dos caras
st.subheader("A) ¿Cuál es la probabilidad de que salga dos caras?")

# Preguntar al usuario por su respuesta
respuesta_a = st.text_input("Ingresa tu respuesta (por ejemplo, 1/3 o 0.33):")

if respuesta_a:
    # Respuesta correcta
    if respuesta_a == "1/4" or respuesta_a == "0.25" or respuesta_a == "2/8":
        st.write("¡Correcto!🎉 La probabilidad de que salga dos caras es 1/4 (o 0.25).")
    else:
        st.write("Respuesta incorrecta. La probabilidad es 1/4 (o 0.25).")

# Ejercicio B: Probabilidad de que salga dos cruces
st.subheader("B) ¿Cuál es la probabilidad de que salga dos cruces?")

# Preguntar al usuario por su respuesta
respuesta_b = st.text_input("Ingresa tu respuesta (por ejemplo, 1/8 o 0.23):")

if respuesta_b:
    # Respuesta correcta
    if respuesta_b == "1/4" or respuesta_b == "0.25" or respuesta_b == "2/8":
        st.write("¡Correcto! 🎉 La probabilidad de que salga dos cruces es 1/4 (o 0.25).")
    else:
        st.write("Respuesta incorrecta. La probabilidad es 1/4 (o 0.25).")

# Ejercicio C: Probabilidad de que salga una cara y una cruz
st.subheader("C) ¿Cuál es la probabilidad de que salga una cara y una cruz?")

# Preguntar al usuario por su respuesta
respuesta_c = st.text_input("Ingresa tu respuesta (por ejemplo, 1/4 o 0.25):")

if respuesta_c:
    # Respuesta correcta
    if respuesta_c == "2/4" or respuesta_c == "0.5" or respuesta_c == "1/2":
        st.write("¡Correcto! 🎉 La probabilidad de que salga una cara y una cruz es 2/4 (o 0.5).")
    else:
        st.write("Respuesta incorrecta. La probabilidad es 1/2 (o 0.5).")

# Explicación adicional
st.write("""
**Explicación:**

- En el caso de las dos primeras preguntas, se tienen 4 resultados posibles (Cara y Cara, Cara y Cruz, Cruz y Cara, Cruz y Cruz). La probabilidad de que salga **dos caras** o **dos cruces** es 1/4, ya que es solo uno de los 4 resultados posibles.

- En la tercera pregunta, la probabilidad de que salga **una cara y una cruz** se refiere a dos combinaciones posibles: **Cara y Cruz**, o **Cruz y Cara**. La probabilidad total de este evento es la suma de las probabilidades de cada una de estas dos combinaciones, es decir, 2/4, lo que equivale a 0.5.

""")

# Título de la aplicación
st.header("Ejercicio de Probabilidad con Bolas en una Urna")

with st.container(border=True):
    c1, c2 = st.columns(2, vertical_alignment="center")
    with c1:
        # Descripción del problema
        st.subheader("Descripción del problema:")
        st.write("""
        Una urna contiene:
        - 7 bolas rojas
        - 6 bolas azules
        - 5 bolas amarillas
        - 4 bolas verdes
        """)


    with c2:

        st.image('https://media.istockphoto.com/id/1391911336/es/vector/tarro-de-cristal-con-piruletas-redondas-de-caramelo-dulce.jpg?s=612x612&w=0&k=20&c=7pVFJI7oWpoLJWPbSL9sYUQNE__8uZtEKVyexeVF64c=', width=500)

                

# Ejercicio A: Probabilidad de que la bola sea roja o verde
st.subheader("A) ¿Cuál es la probabilidad de que la bola sea roja o verde?")

# Preguntar al usuario por su respuesta
respuesta_a = st.text_input("Ingresa tu respuesta (por ejemplo, 3/8 o 0.3):")

if respuesta_a:
    # Respuesta correcta
    if respuesta_a == "1/2" or respuesta_a == "0.5" or respuesta_a == "11/22":
        st.write("¡Correcto! 🎉 La probabilidad de que la bola sea roja o verde es 0.5 o 11/22.")
    else:
        st.write("Respuesta incorrecta. La probabilidad es 0.5 o 11/22.")

# Ejercicio B: Probabilidad de que no sea amarilla
st.subheader("B) ¿Cuál es la probabilidad de que la bola no sea amarilla?")

# Preguntar al usuario por su respuesta
respuesta_b = st.text_input("Ingresa tu respuesta (por ejemplo, 5/15 o 0.333):", key=1)

if respuesta_b:
    # Respuesta correcta
    if respuesta_b == "17/22" or respuesta_b == "0.77":
        st.write("¡Correcto! 🎉 La probabilidad de que no sea amarilla es 0.77 o 17/22.")
    else:
        st.write("Respuesta incorrecta. La probabilidad es 0.77 o 17/22.")
    
# Ejercicio C: Probabilidad de que sea azul 
st.subheader("C) ¿Cuál es la probabilidad de que la bola sea azul?")

# Preguntar al usuario por su respuesta
respuesta_c = st.text_input("Ingresa tu respuesta (por ejemplo, 5/15 o 0.333):", key=2)

if respuesta_c:
    # Respuesta correcta
    if respuesta_c == "2/11" or respuesta_c == "0.18" or respuesta_c == "4/22":
        st.write("¡Correcto! 🎉 La probabilidad de que sea azul es 0.18 o 2/11.")
    else:
        st.write("Respuesta incorrecta. La probabilidad es 0.18 o 2/11.")
    
# Explicación adicional
st.write("""
**Explicación:**

- Para la primera pregunta, se suman las probabilidades de obtener una bola roja o verde. Como estos son eventos mutuamente excluyentes (no tienen intersección), la probabilidad total es la suma de sus probabilidades individuales.

- Para la segunda pregunta, usamos la probabilidad complementaria. La probabilidad de no sacar una bola amarilla es igual a 1 menos la probabilidad de sacar una bola amarilla.

""")



