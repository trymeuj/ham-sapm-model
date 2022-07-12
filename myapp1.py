import streamlit as st
import joblib

model_mode = joblib.load('ham-spam')

st.title("spam or ham let's check")
ip = st.text_input("enter ur text")

op = model_mode.predict([ip])
if st.button('DO_PREDICT'):
  st.title(op[0])
         
