
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