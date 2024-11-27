import streamlit as st

# 1) crear las paginas
intro = st.Page("paginas/intro.py", title="Introducción", icon=":material/key_vertical:", default=True)
ejs = st.Page("paginas/ejercicios.py", title="Ejercicios", icon=":material/neurology:")

# 2) navigation
pg = st.navigation([intro, ejs])

# 3) ejecutar
pg.run()