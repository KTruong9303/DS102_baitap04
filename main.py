import streamlit as st
import pickle as pkl
from PIL import Image
import numpy as np

st.markdown(
    """
    <style>
        # .st-eb {
        .streamlit-slider .stSlider > div {
            background-color: purple !important;  /* Change this to your desired color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

NB = st.sidebar.select_slider('', options = [1,10,20,30,40,50,60,70,80,90,100], value = 1)


ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(1 1 1 / 0%); } </style>''', unsafe_allow_html = True)


Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: rgb(14, 38, 74); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)

    
Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: rgb(14, 38, 74); } </style>''', unsafe_allow_html = True)
    

col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
                                rgb(1, 183, 158) {NB}%, 
                                rgba(151, 166, 195, 0.25) {NB}%, 
                                rgba(151, 166, 195, 0.25) 100%); }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True)


class_list = {'0': 'Setosa', '1': 'Versicolor', '2': 'Virginica'}

st.title('Iris classification based on sepal and petal size')

image = Image.open('iris.jpg')
st.image(image)

input = open('lrc_iris(1).pkl', 'rb')
model = pkl.load(input)


st.header('Choose the size of sepal and petal size')

sepal_length = st.slider('Sepal length (cm)', 0.0, 20.0, 3.0, 0.2)
sepal_width = st.slider('Sepal width (cm)', 0.0, 20.0, 2.7, 0.1)
petal_length = st.slider('Petal length (cm)', 0.0, 20.0, 2.7, 0.2)
petal_width = st.slider('Petal width (cm)', 0.0, 20.0, 2.7, 0.1)

if st.button('Predict'):
        feature_vector = np.array([sepal_length, sepal_width, petal_length, petal_width])
        feature_vector = feature_vector.reshape(1, -1)
        label = str((model.predict(feature_vector))[0])

        st.header('Result')
        st.text(class_list[label])
