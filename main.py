import streamlit as st
import pandas as pd
import numpy as np

st.title('')
input = open('lrc_xray.pkl','rb')
model = pkl.load(input)

st.header('1')
gre = st.number_input('Insert GRE score')
toefl=st.number_input('Insert torfl score')
uni_rate = st.number_input('Insert UNI rate')
sop = st.number_input('Insert SOP')
lor =st.number_input('Insert Lor')
cgpa=st.number_input('Insert CGPA')
reseach= st.radio('choose reseach',)
