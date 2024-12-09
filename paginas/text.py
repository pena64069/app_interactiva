import streamlit as st

# Definimos las preguntas, las opciones y las respuestas correctas
preguntas = [
    {
        "pregunta": "¿Cuál es la probabilidad de que salga un número par al lanzar un dado de seis caras?",
        "opciones": ["1/6", "1/3", "1/2", "2/3"],
        "respuesta_correcta": "1/2"
    },
    {
        "pregunta": "Si tenemos una bolsa con 3 bolas rojas y 5 bolas azules, ¿cuál es la probabilidad de sacar una bola roja?",
        "opciones": ["3/5", "5/8", "3/8", "1/2"],
        "respuesta_correcta": "3/8"
    },
    {
        "pregunta": "En una baraja de 52 cartas, ¿cuál es la probabilidad de sacar un as?",
        "opciones": ["1/52", "1/13", "1/26", "4/52"],
        "respuesta_correcta": "1/13"
    },
    {
        "pregunta": "En una urna con 5 bolas rojas y 3 bolas verdes, ¿cuál es la probabilidad de sacar una bola verde?",
        "opciones": ["5/8", "3/8", "3/5", "8/3"],
        "respuesta_correcta": "3/8"
    },
    {
        "pregunta": "Si lanzo una moneda 3 veces, ¿cuál es la probabilidad de obtener exactamente 2 caras?",
        "opciones": ["1/8", "3/8", "1/2", "1/4"],
        "respuesta_correcta": "3/8"
    },
    {
        "pregunta": "Si un dado se lanza 2 veces, ¿cuál es la probabilidad de que la suma de los dos dados sea 7?",
        "opciones": ["1/6", "1/36", "5/36", "1/12"],
        "respuesta_correcta": "1/6"
    },
    {
        "pregunta": "En una urna con 4 bolas rojas, 6 bolas verdes y 10 bolas azules, ¿cuál es la probabilidad de sacar una bola azul?",
        "opciones": ["10/20", "4/10", "6/20", "10/30"],
        "respuesta_correcta": "10/20"
    },
    {
        "pregunta": "¿Cuál es la probabilidad de sacar un número mayor que 4 en un dado de seis caras?",
        "opciones": ["2/6", "1/3", "1/2", "1/6"],
        "respuesta_correcta": "2/6"
    },
    {
        "pregunta": "En un experimento de lanzar una moneda y un dado, ¿cuál es la probabilidad de que salga cara y el dado muestre un número impar?",
        "opciones": ["1/12", "1/6", "1/4", "1/3"],
        "respuesta_correcta": "1/4"
    },
    {
        "pregunta": "Si un dado se lanza, ¿cuál es la probabilidad de que salga un número menor que 3?",
        "opciones": ["2/6", "1/3", "1/6", "1/2"],
        "respuesta_correcta": "2/6"
    }
]

# Función para mostrar el examen y capturar las respuestas
def mostrar_examen():
    respuestas_usuario = []
    for pregunta in preguntas:
        # Mostramos la pregunta y las opciones como un radio button
        respuesta = st.radio(pregunta['pregunta'], pregunta['opciones'], key=pregunta['pregunta'])
        respuestas_usuario.append((pregunta['respuesta_correcta'], respuesta))
    
    return respuestas_usuario

# Función para calcular la puntuación
def calcular_puntaje(respuestas_usuario):
    correctas = sum([1 for correcto, respuesta in respuestas_usuario if correcto == respuesta])
    incorrectas = len(respuestas_usuario) - correctas
    return correctas, incorrectas

# Mostrar el examen
st.title("Examen de Probabilidad")
respuestas_usuario = mostrar_examen()

# Mostrar botón para calcular puntaje
if st.button('Calificar'):
    correctas, incorrectas = calcular_puntaje(respuestas_usuario)
    st.write(f"Respuestas correctas: {correctas}")
    st.write(f"Respuestas incorrectas: {incorrectas}")
    st.write(f"Puntaje: {correctas} de {len(preguntas)}")
