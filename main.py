import streamlit as st

# 1) crear las paginas
intro = st.Page("paginas/intro.py", title="Introducción", icon=":material/key_vertical:", default=True)
ejs = st.Page("paginas/ejemplos.py", title="Ejemplos", icon=":material/lightbulb:")
exc = st.Page("paginas/ejercicios.py", title="Ejercicios", icon=":material/neurology:")
t = st.Page("paginas/text.py", title="Examen", icon=":material/strategy:")
p = st.Page("paginas/presentacion.py", title="¿Quien Soy?", icon=":material/identity_platform:")

# 2) navigation
pg = st.navigation({"Conceptos":[intro,ejs], "Desafia tu mente":[exc], "Ponte a prueba":[t], "Presentacion":[p]})

# 3) ejecutar
pg.run()