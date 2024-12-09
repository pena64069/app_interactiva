import streamlit as st
c1, c2 = st.columns(2, vertical_alignment="center")
with c1:
    st.title('Probabilidad')
with c2:
    st.image("dices-color-icon-probability-theory-gambling-isolated-illustration-vector.jpg", width=250)

st.subheader("1. Definición de Probabilidad")
st.markdown('La probabilidad es una rama de las matemáticas que se encarga de estudiar la posibilidad de que ocurra un evento en particular. Es un concepto fundamental en estadísticas, y se utiliza para predecir la ocurrencia de eventos en situaciones de incertidumbre.')
st.subheader("2. Conceptos Básicos de Probabilidad")
st.markdown("__✧ Espacio muestral (S):__ Es el conjunto de todos los posibles resultados de un experimento aleatorio. Por ejemplo, en el lanzamiento de un dado, el espacio muestral es __{1,2,3,4,5,6}__.")
st.markdown("__✧ Eventos:__ Son subconjuntos del espacio muestral. Un evento puede ser un solo resultado o varios resultados. Por ejemplo, el evento de obtener un número par al lanzar un dado es __{2,4,6}__.")
st.markdown('__✧ Probabilidad de un Evento:__ La probabilidad de que un evento ocurra se define como la razón entre el número de resultados favorables y el número total de resultados posibles, siempre que los resultados sean igualmente probables. ')
st.markdown("La fórmula básica para calcular la probabilidad de un evento es:")

st.latex(r'''

    P(A) = \frac{\text{número de resultados favorables a A}}{\text{número total de resultados posibles}}

''')
st.markdown('Donde:')
st.markdown('+ P(A) es la probabilidad de que ocurra el evento A.')
st.markdown('+ Los resultados favorables son aquellos que conducen al evento deseado.')
st.markdown('+ Los resultados posibles son todos los resultados posibles en el espacio muestral.')
st.markdown("La probabilidad se expresa como un número entre 0 y 1.")
st.subheader('Ejemplo:')
st.markdown('Imagina que lanzas un dado. ¿Cuál es la probabilidad de que salga un número par?')
st.markdown('+ El espacio muestral es: __{1,2,3,4,5,6}__')
st.markdown('+ Los resultados favorables para un número par son: __{2,4,6}__')
st.markdown('Entonces, la probabilidad de que salga un número par es:')
st.latex(r'P(\text{número par}) = \frac{3}{6} = 0.5')
st.markdown('Esto significa que hay un 50% de probabilidad de que salga un número par.')
st.markdown('__✧ Eventos mutuamente excluyentes:__ Son aquellos que no pueden ocurrir al mismo tiempo. Por ejemplo, al lanzar un dado, los eventos de "sacar un 3" y "sacar un 5" son mutuamente excluyentes, porque no puedes obtener ambos números al mismo tiempo.')
st.markdown('__✧ Eventos Independientes:__ Dos eventos son independientes si la ocurrencia de uno no afecta la probabilidad de que ocurra el otro. Por ejemplo, al lanzar una moneda y un dado al mismo tiempo, los eventos "salir cara" en la moneda y "salir 4" en el dado son independientes.')
st.subheader("3. Reglas Básicas de la Probabilidad")


st.markdown('__✧ Regla de la Suma para eventos mutuamente excluyentes:__ Si los eventos A y B son mutuamente excluyentes, la probabilidad de que ocurra uno u otro es la suma de sus probabilidades individuales:')
st.latex(r'P(A \cup B) = P(A) + P(B)')


st.markdown('__✧ Regla del Producto para eventos independientes:__ Si los eventos A y B son independientes, la probabilidad de que ambos ocurran es el producto de sus probabilidades individuales:')
st.latex(r'P(A \cap B) = P(A) \times P(B)')
st.subheader('Ejemplo de Cálculos Básicos de Probabilidad:')


st.markdown('+ __Lanzar un dado__')
st.markdown('¿Cuál es la probabilidad de que salga un número mayor que 4?')
st.markdown('El espacio muestral es: __{1,2,3,4,5,6}__ Los resultados favorables son: __{5,6}__')
st.markdown('Entonces:')
st.latex(r'P(\text{número mayor que 4}) = \frac{3}{6} = \frac{1}{2} \approx 0.3333')


st.markdown('+ __Lanzar una moneda__')
st.markdown('¿Cuál es la probabilidad de obtener "cara"?')
st.markdown('El espacio muestral es: __{cara,cruz}__ El número de resultados favorables es 1 (cara).')
st.markdown('Entonces:')
st.latex(r'P(\text{cara}) = \frac{1}{2} = 0.5')

st.subheader('Video De Apoyo')
st.video("https://youtu.be/WeeEE8o1aqM?si=MbW_MQBOHveUnsqw")
