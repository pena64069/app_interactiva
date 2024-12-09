import streamlit as st

# Título
st.title("Examen de Probabilidad 📃🧠📚✍🏼")

st.write("""
Bienvenido al examen de cálculo de probabilidades. Responde las preguntas y al finalizar, obtendrás tu calificación.
""")

# Preguntas del examen
preguntas = [
    {
        "pregunta": "1. ¿Cuál de los siguientes experimentos no es aleatorio?",
        "opciones": [
            "A) Observar un semáforo y ver si está en rojo.",
            "B) En una carrera de caballos, que gane el caballo Emperador.",
            "C) La cantidad de pasajeros que se bajan en una estación de metro.",
            "D) Pulsar un interruptor y que se encienda la luz."
        ],
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "2. Se da el conjunto D = {1,2,3,4,5,6,7,8,9}. ¿Cual es la probabilidad de que, al elegir un digito al azar de D, se obtenga un multiplo de 3?",
        "opciones": ["A) 1/2", "B) 1/3", "C) 1/4", "D) 1/5"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "3. Se elige al azar una ficha de un grupo de ellas en una bolsa negra, numeradas desde el 1 al 15. Si todas las fichas tienen la misma forma y tamaño ¿cual es la probabilidad de que laficha extraida contenga un numero que es multiplo de 2?",
        "opciones": ["A) 1/15", "B) 2/15", "C) 7/15", "D) 8/15"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "4. En una urna hay 14 fichas en total, de colores blanco, rojo y negro. Si hay 5 fichas blancas y la probabilidad de sacar una ficha blanca o negra es 4/7, entonces, ¿Cuantas fichas son negras?",
        "opciones": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "5. Se tienen dos cajas, una con 4 bolas blancas y 2 negras y la otra con 3 blancas y 5 negras. Si se saca una bola de cada caja. ¿Cual es la probabilidad de que ambas sean blancas?",
        "opciones": ["A) 1/6", "B) 1/5", "C) 1/4", "D) 3/4"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "6. Al lanzar un dado, la probabilidad de que el resultado sea impar o primo es:",
        "opciones": ["A) 1", "B) 2/3", "C) 2/5", "D) 3/5"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "7. Se lanzan tres monedas. ¿Cual es la probabilidad de obtener dos sellos y una cara?",
        "opciones": ["A) 3/4", "B) 5/8", "C) 1/2", "D) 3/8"],
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "8. Se elige al azar un numero entero positivo de dos digitos. ¿Cual es la probabilidad de queen el numero elegido, sus digitos sumen 10?",
        "opciones": ["A) 1/100", "B) 9/100", "C) 1/10", "D) 1/9"],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "9. Un jugador de futbol tiene tres oportunidades de hacer goles de penal. Si la probabilidad deque no acierte es 0.2, entonces la probabilidad de que acierte los tres penales es:",
        "opciones": ["A) 1/5", "B) 1/125", "C) 0,04", "D) 0,512"],
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "10. En una oficina trabajan 8 hombres y 6 mujeres. Si se va a elegir una comision formada por tres integrantes, ¿cual es la probabilidad de que este integrada por 2 hombres y una mujer?",
        "opciones": ["A) 2/13", "B) 6/13", "C) 8/13", "D) 6/49"],
        "respuesta_correcta": "B"
    },
    
]

# Variables para almacenar respuestas y calificación
respuestas_usuario = []
calificacion = 0

# Mostrar preguntas al usuario
st.subheader("Responde las siguientes preguntas:")

for i, pregunta in enumerate(preguntas):
    st.write(pregunta["pregunta"])
    respuesta = st.radio(f"Pregunta {i+1}", pregunta["opciones"], key=f"pregunta_{i}")
    respuestas_usuario.append(respuesta.split(")")[0])  # Captura solo la letra (A, B, etc.)

# Botón para calificar
if st.button("Calificar", key="calificar"):
    for i, respuesta_usuario in enumerate(respuestas_usuario):
        correcta = preguntas[i]["respuesta_correcta"]
        if respuesta_usuario == correcta:
            calificacion += 1
        else:
            st.error(f"Pregunta {i+1}: Incorrecta ❌😔. La respuesta correcta era {correcta}.")
        

    # Calificación final
    st.success(f"Tu calificación es {calificacion}/{len(preguntas)}.")
    if calificacion == len(preguntas):
        st.balloons()
        st.write("¡Excelente! 🏆👍🏻😎🤑 Has respondido todo correctamente.")
    else:
        st.write("¡Sigue practicando para mejorar tus conocimientos!😄")




