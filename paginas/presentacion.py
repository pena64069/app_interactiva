import streamlit as st

c1, c2 = st.columns([1,2], vertical_alignment="center")

with c1:
    with st.container(border=True):
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAM5N0qJOJxWJ6KwSY6jHQa-c3wiANFCAgdwju-5zUUkEsnZPBii8vRATcl6ERaBlxXmo&usqp=CAU", width=300)
        st.header("José Nícolas Ortega Peña")
with c2:
    st.subheader('Presentación personal ')
    st.markdown("""¡Hola! Mi nombre es Nicolás, y estoy muy contento de estar aquí para presentarme. Actualmente, soy estudiante de Matematicas, de la Universidad Industrial de Santander (UIS) y tengo una gran pasión por superarme cada dia. Me gustaría contarles un poco más sobre mí.

Nací en Bucaramanga, y desde pequeño siempre me ha interesado los números y los deportes.

En mi tiempo libre, disfruto de ver peliculas, jugar futbol, pasar tiempo en familia, entre otras actividades; lo cual me ayuda a mantenerme equilibrado y motivado. Soy una persona disciplinada, responsable, y siempre trato de dar lo mejor de mí en todo lo que hago.

Mi objetivo para el futuro es terminar mi carrera universitaria, y estoy buscando constantemente oportunidades para seguir aprendiendo y desarrollándome como persona. Estoy muy entusiasmado con lo que viene y con las personas y proyectos que podré conocer en el camino.

El área de la matematica en la que me considero con mayor afinidad, es en el área del algebra lineal.

Gracias por tomarte el tiempo de leer.""")



with st.container(border=True):
    st.subheader("¿Qué aprendizaje me deja la materia de programación I?")
    st.markdown("""La materia de Programación I me enseñó a pensar de manera lógica y estructurada para resolver problemas, comprendiendo la sintaxis y las estructuras del lenguaje, como variables, operadores y estructuras de control. Aprendí a escribir mis primeros programas, depurar errores y organizar el código de manera eficiente mediante la utilización con funciones. Además, entendí que la programación no solo consiste en escribir código, sino en hacerlo claro, eficiente y comprensible para otros. Programación I me proporcionó una base sólida para seguir aprendiendo y mejorar mis habilidades como programador.
     """)