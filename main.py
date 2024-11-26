import streamlit as st

st.title("Transformaciones Geometricas")
st.caption("soy estudiante de la materia programacion 1")
st.title("titulo de nivel 1")
st.header("titulo de nivel 2")
st.subheader("titulo de nivel 3")

#textos
st.markdown("""
En una etiqueta de tipo markdown pueden poner cualquier texto en el formato markdon.

**negrilla**, en *italica*, o en ***ambos***.

esto es otra linea.

Enumeraciones:
1. Primer item
2. Segundo item
3. Tercer item 

Items:
+ Item 1
+ Item 2
+ Item 3

Podemos dar color al texto por ejemplo: red[rojo], :blue[azul], :green[verde],
""")

# ecuaciones

st.latex("a^2 + b^2 = c^2")

st.image("https://www.neurochispas.com/wp-content/uploads/2021/05/como-aplicar-el-teorema-de-pitagoras.png")

st.video("https://www.google.com/search?sca_esv=a602e8e6c3755c23&sxsrf=ADLYWILx4DAkQOWf_69A7wwS6w9spiaBuA:1732652289250&q=pitagoras&udm=7&fbs=AEQNm0CbCVgAZ5mWEJDg6aoPVcBgWizR0-0aFOH11Sb5tlNhdwiPJWZFf-MdNGF5cE7ER6ksc8uP1I2s59dA09Tzf42VMjnL_A2uH57sHixrm0pJcgyf3h4R_ilo9WjPx21-slulsS5VKuO6XuohSzlfxaQ7I1wIpiZH_OzbeluVNvZIRLVCVtZLMZF2WK32JO8o3XFhHBbmpe-tojdA4Yf3rPJ8zeRJJQ&sa=X&sqi=2&ved=2ahUKEwik_eDh6PqJAxV7QzABHQSnGy0QtKgLegQIEBAB&biw=958&bih=952&dpr=1#")