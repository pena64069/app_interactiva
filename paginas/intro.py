import streamlit as st
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.title('Probabilidad')
with c2:
    st.image("dices-color-icon-probability-theory-gambling-isolated-illustration-vector.jpg", width=250)

st.subheader("1. Definición de Probabilidad")
st.markdown("La probabilidad de un evento es un número entre 0 y 1 que refleja la posibilidad de que dicho evento ocurra. El valor 0 significa que el evento no ocurrirá, mientras que el valor 1 indica que el evento es seguro.")
st.markdown("__✧ Probabilidad de un evento (P(A)):__ Es el cociente entre el número de casos favorables y el número total de posibles resultados. Es decir, si tenemos un experimento con un conjunto de resultados posibles, la probabilidad de un evento __A__ se calcula de la siguiente manera:")
st.latex(r'''
    P(A) = \frac{\text{número de resultados favorables a A}}{\text{número total de resultados posibles}}
''')
st.markdown("La probabilidad se expresa como un número entre 0 y 1.")

st.subheader("2. Conceptos Básicos de Probabilidad")
st.markdown("__✧ Espacio muestral (S):__ Es el conjunto de todos los posibles resultados de un experimento aleatorio. Por ejemplo, en el lanzamiento de un dado, el espacio muestral es __{1,2,3,4,5,6}__.")
st.markdown("__✧ Eventos:__ Son subconjuntos del espacio muestral. Un evento puede ser un solo resultado o varios resultados. Por ejemplo, el evento de obtener un número par al lanzar un dado es __{2,4,6}__.")
st.markdown('__✧ Eventos mutuamente excluyentes:__ Son aquellos que no pueden ocurrir al mismo tiempo. Por ejemplo, al lanzar un dado, los eventos de "sacar un 3" y "sacar un 5" son mutuamente excluyentes, porque no puedes obtener ambos números al mismo tiempo.')
st.markdown('__✧ Eventos complementarios:__ Son eventos opuestos. Si __A__ es un evento, su complemento (__A^c__) es el conjunto de todos los resultados que no están en __A__. Por ejemplo, si __A__ es el evento de obtener un número par al lanzar un dado ({2, 4, 6}), entonces su complemento (__A^c__) sería {1, 3, 5}.')







st.video("https://youtu.be/JDP3mGgBp68")





# Título de la página
st.title("Mi Primera Aplicación con Streamlit")

# Pedir datos al usuario
nombre = st.text_input("Ingrese su nombre:")
edad = st.number_input("Ingrese su edad:", min_value=1, max_value=120)
rango = st.slider("Seleccione un valor", min_value=1, max_value=10)
ini, final = st.slider("Seleccione un rango:", min_value=1, max_value=100, value=(20, 80))

# Mostrar resultados
st.write("¡Hola,", nombre, "!")
st.write("Tu edad es:", edad)

st.write("El rango seleccionado es de", ini, "a", final)

# Agregar una imagen
st.image("https://www.example.com/imagen.jpg", caption="Una imagen para decorar")

# Crear un botón interactivo
if st.button("Enviar"):
    st.write("¡Has enviado tus datos!")