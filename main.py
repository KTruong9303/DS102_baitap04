import streamlit as st
import pickle as pkl
from PIL import Image
import numpy as np

class_list = {'0': 'Setosa', '1': 'Versicolor', '2': 'Virginica'}


st.title('Iris classification based on sepal and petal size')

image = Image.open('iris_flower.jpg')
st.image(image)
